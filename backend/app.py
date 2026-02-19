import sys

print("Đang khởi động hệ thống Backend...")
print(f"Phiên bản Python đang dùng là: {sys.version}")

# Giả lập một bài test đơn giản
def phep_cong(a, b):
    return a + b

ket_qua = phep_cong(5, 10)
if ket_qua == 15:
    print("✅ Test thành công: 5 + 10 = 15")
else:
    print("❌ Test thất bại!")
    exit(1) # Lệnh này báo cho GitHub Action biết là job bị lỗi