import json

from scenedetect import open_video, ContentDetector, SceneManager

# process the file to split the scenes
# https://scenedetect.com/projects/Manual/en/latest/api.html
def get_scene_manager(video_path, threshold=27.0, min_scene_len=15) -> SceneManager:
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold, min_scene_len=min_scene_len))
    # Detect all scenes in video from current position to end.
    scene_manager.detect_scenes(video, show_progress=True)
    # `get_scene_list` returns a list of start/end timecode pairs
    # for each scene that was found.
    return scene_manager  # .get_scene_list()


def get_scene_list(video_path, threshold=27.0, min_scene_len=15) -> list:
    return get_scene_manager(video_path, threshold, min_scene_len).get_scene_list()


def scenes_extraction(event, context):
    print('bbbbbbooooooooooooorrraaa, carai!!!!')
    print(get_scene_list('teste.mp4'))

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully! teste",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
