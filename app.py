import streamlit as st
import os
import glob

#handling moviepy version differnces
try:
  from moviepy.editor import ImageClip,concatenate_videoclips,AudiofileClip
except ImportError:
  from moviepy import ImageClip,concatenan
