def convert_melody(melody):
    replaces = {
        'C#': 'c', 'D#': 'd', 'F#': 'f',
        'G#': 'g', 'A#': 'a', 'E#': 'e', 'B#': 'b'
    }
    for k, v in replaces.items():
        melody = melody.replace(k, v)
    return melody

def get_play_time(start, end):
    h1, m1 = map(int, start.split(":"))
    h2, m2 = map(int, end.split(":"))
    return (h2 * 60 + m2) - (h1 * 60 + m1)

def solution(m, musicinfos):
    m = convert_melody(m)
    candidates = []

    for info in musicinfos:
        start, end, name, melody = info.split(",")
        duration = get_play_time(start, end)
        melody = convert_melody(melody)

        # 재생된 전체 멜로디 구성
        full_melody = (melody * (duration // len(melody))) + melody[:duration % len(melody)]

        if m in full_melody:
            candidates.append((duration, name))

    # 조건에 맞는 곡이 없으면 "(None)" 반환
    if not candidates:
        return "(None)"

    # 재생 시간 기준으로 가장 긴 곡 반환
    candidates.sort(key=lambda x: -x[0])
    return candidates[0][1]
