import cv2 #open CV(약자로 그래픽을 자유자재로 주무를 수 있는 라이브러리이다) 라이브러리를 가져옴


cap = cv2.VideoCapture(0) #cv2.VideoCapture() 명령어로 카메라를 열 수 있습니다.
cap.set(3, 640) #웹캠의 창 크기
cap.set(4, 480)
face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml") #정면 얼굴 검출을 할 수 있는 파일

# ID 입력
face_id = input('\n USER ID 입력하고 엔터 누르세요 ')

count = 0
while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #COLOR_BGR2GRAY : 경계면을 잘 구분하기 위해 회색으로 변환 후 인식 후 다시 원본으로 색상으로 돌림.(회색 사진이 인식을 더 잘함)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", img[y:y + h, x:x + w])
        # imwrite : 얼굴 검출을 한 부분을 저장하는 함수
        # img[y:y + h, x:x + w] 얼굴을 잘라낸 사각형의 크기
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff  # 비디오 종료 시 'ESC' 누르기
    if k == 27:
        break
    elif count >= 10:  # 10개 이미지 뽑고, 종료하기
        print("complete!!")
        break

cap.release()
cv2.destroyAllWindows()