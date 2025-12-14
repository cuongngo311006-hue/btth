
def benefit(t, n, k):
    

    if t < 0 or n <= 0 or k <= 0:
        print("Dữ liệu nhập vào không hợp lệ")
        return

    so_tien = n
    for i in range(k):
        so_tien += so_tien * t / 100

    return so_tien


t = float(input("Nhập lãi suất (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

ket_qua = benefit(t, n, k)
if ket_qua is not None:
    print("Số tiền nhận được sau", k, "tháng là:", ket_qua)
