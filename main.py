import cv2
import pafy
import youtube_dl


url = 'https://www.youtube.com/watch?v=CLcEOJz-feE&list=RDMMCLcEOJz-feE&start_radio=1'
# pafy.BACK_END = "internal" # incase you want to use youtube-dl as backend, comment this line and install youtube-dl
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="mp4")

#start the video
cap = cv2.VideoCapture(play.url)
while (True):
    ret,frame = cap.read()

    ''''
     Your Code, Whatever you want to do
    '''

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break    

cap.release()
cv2.destroyAllWindows()