from datetime import datetime

def generate_faktur(last_number: int = 0, current_date: datetime = None) -> str:
    """
    Membuat nomor faktur dengan format: 4digit/FP/tanggal/YYMM
    Contoh: 1202/FP/18/2506

    Args:
        last_number (int): Nomor urut terakhir (akan dinaikkan 1)
        current_date (datetime, optional): Tanggal faktur. Default: hari ini.

    Returns:
        str: Nomor faktur yang sudah diformat
    """
    if current_date is None:
        current_date = datetime.now()

    new_number = last_number + 1
    nomor_urut = f"{new_number:04d}"  # 4 digit leading zero
    tanggal = f"{current_date.day:02d}"
    tahun_bulan = current_date.strftime("%y%m")  # Format YYMM

    return f"{nomor_urut}/FP/{tanggal}/{tahun_bulan}"
