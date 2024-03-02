import cv2
import dlib


def main():

    # Đọc ảnh RGB vào biến img
    RGB_img = cv2.imread(
        "ML_DL_Projects\Computer_Vision\First_Face_Recognization\src_img.jpg"
    )

    # Convert to grayscale: 3D(RGB) -> 2D(BW)
    # Nhận diện khuôn mặt chỉ cần ảnh trắng đen (2D)
    gray_img = cv2.cvtColor(src=RGB_img, code=cv2.COLOR_BGR2GRAY)

    # Lấy hàm phát hiện khuôn mặt phía trước
    face_detector = dlib.get_frontal_face_detector()
    # Trả về 1 danh sách các rectangle đại diện cho các khuôn mặt
    faces = face_detector(gray_img)

    # Nạp model nhận diện đặc điểm khuôn mặt
    predictor = dlib.shape_predictor(
        "ML_DL_Projects\Computer_Vision\First_Face_Recognization\shape_predictor_68_face_landmarks.dat"
    )

    for face in faces:

        # Top left
        x1, y1 = face.left(), face.top()
        # Right bottom
        x2, y2 = face.right(), face.bottom()

        # Draw Rectangle với khuôn mặt nhận dạng được lên ảnh RGB
        cv2.rectangle(
            img=RGB_img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=1
        )

        # Gồm 68 điểm tọa độ trên khuôn mặt, nhận dạng trên ảnh đen trắng
        face_features = predictor(image=gray_img, box=face)

        # Duyệt qua 68 điểm trên khuôn mặt
        for i in range(0, 68):
            # Lấy tọa độ từng điểm trên khuôn mặt
            x, y = face_features.part(i).x, face_features.part(i).y
            # Vẽ 1 điểm hình tròn với mỗi điểm
            cv2.circle(
                img=RGB_img, center=(x, y), radius=1, color=(0, 0, 255), thickness=1
            )

    # Hiển thị ảnh lên 1 khung cửa sổ
    cv2.imshow(winname="Face Recognization", mat=RGB_img)

    # Đợi user nhấn phím bất kỳ
    cv2.waitKey(delay=0)

    # Tắt hết cửa sổ
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
