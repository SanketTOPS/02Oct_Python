from pytubefix import YouTube

url="https://www.youtube.com/watch?v=p_4o2haEQsE"

YouTube(url).streams.filter().download()