#a beginner's practice code
import hashlib

# 비밀번호 해쉬 생성 함수
def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

# 저장
saved_hash = hash_password("1234")

# 로그인
input_pw = input("비밀번호: ")
if hash_password(input_pw) == saved_hash:
    print("로그인 성공!")
else:
    print("비밀번호 틀림")