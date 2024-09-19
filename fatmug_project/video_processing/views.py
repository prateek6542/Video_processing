import subprocess
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoUploadForm
from django.http import JsonResponse

def process_video(video):
    video_path = video.video_file.path  

    try:
        result = subprocess.run(
            ['ffmpeg', '-i', video_path, 'output.srt'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True 
        )

        
        if result.returncode != 0:
            print(f"Error in ffmpeg: {result.stderr}")
            return None

       
        with open('output.srt', 'rb') as subtitle_file:
            subtitle_content = subtitle_file.read()

        subtitles = subtitle_content.decode('utf-8')

        video.subtitles = subtitles
        video.save()

    except FileNotFoundError:
        # Handle the case where ffmpeg is not installed
        print("ffmpeg not found or not installed")
        return None


def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            process_video(video)  
            return redirect('video_list')
    else:
        form = VideoUploadForm()

    return render(request, 'upload_video.html', {'form': form})

# List view for displaying uploaded videos
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

# Search subtitles within a video
def search_subtitles(request):
    query = request.GET.get('q', '').lower()  
    results = []

   
    videos = Video.objects.all()

    for video in videos:
        # Check if the video has subtitles
        if video.subtitles:
            
            if query in video.subtitles.lower():
                
                timestamps = find_timestamp_in_subtitles(video.subtitles, query)
                results.append({
                    'video': video,
                    'timestamps': timestamps
                })
        else:
            continue

    return render(request, 'search_results.html', {'results': results, 'query': query})
