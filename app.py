import streamlit as st
import os
import glob

#handling moviepy version differnces
try:
  from moviepy.editor import ImageClip,concatenate_videoclips,AudiofileClip
except ImportError:
  from moviepy import ImageClip,concatenate_videoclips,AudioFileClip
import yt_dlp

#---1.INITIALIZE STATE ---
if 'audio_path'not in st.session_state:
  st.session_state['audio_path']=None
if 'yt error' in st.session_states:
  pass #keep it for display logic

#---2.DEFINE ALL FUNCTIONS ---

def cleanup_temp_files():
  """Removes temporary files and resets memory."""
  files=glob.glob("temp_*")+["output_video.mp4"]
  for f in files:
    try:
      os.remove(f)
    except:
      pass
  st.session_state['audio_path'] = None
  if 'yt_error' in st.session_state:
    del st.session_state['yt_error']

def download_youtube_audio(url):
  """Downloads only audio from  youtube using reliable browser impersonation."""
  audio_opts={
    'format':'bestaudio/best',
    
