from sklearn.datasets import load_digits  # 패키지 임포트

class Number:
    def __init__(self):
        self.digits = load_digits()  # 데이터 로드
        self.samples = [0, 10, 20, 30, 1, 11, 21, 31]  # 선택된 이미지 번호
        self.d = []



# for i in range(8):
#     d.append(digits.images[samples[i]])
#
# plt.figure(figsize=(8, 2))
# for i in range(8):
#     plt.subplot(1, 8, i + 1)
#     plt.imshow(d[i], interpolation='nearest', cmap=plt.cm.bone_r)
#     plt.grid(False); plt.xticks([]); plt.yticks([])
#     plt.title("image {}".format(i + 1))
# plt.suptitle("숫자 0과 1 이미지")
# plt.tight_layout()
# plt.show()