from sonnendauer import get_sonnendauer
from windstaerke import get_windstaerke

def get_wetterbericht():
    return f"{get_sonnendauer()} {get_windstaerke()}"

if __name__ == "__main__":
    print(get_wetterbericht())
