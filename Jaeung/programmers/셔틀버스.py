def solution(n, t, m, timetable):
    
    # timetable 내 모든 시간을 분 단위 변환하고 크기 순으로 정렬
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    
    # 버스가 출발하는 시간을 따로 배열로 만들어서 저장
    bus_times = [9 * 60 + i * t for i in range(n)]
    
    crew = 0
    for bus in bus_times:
        bus_crew = []
        
        # 현재 버스에 탈 수 있는 인원 만큼 태우기 
        while crew < len(timetable) and timetable[crew] <= bus and len(bus_crew) < m:
            bus_crew.append(timetable[crew])
            crew += 1

    # 마지막 버스에 자리가 남았다면, 버스 출발 시간에 맞춰서 오기
    if len(bus_crew) < m:
        con_time = bus_times[-1]
    # 마지막 버스가 다 찼다면, 마지막 탑승자보다 1분 먼저 오기
    else:
        con_time = bus_crew[-1] - 1
        
    h = con_time // 60
    m = con_time % 60
    # 분 단위 시각을 다시 HH:MM 문자열로 변환
    answer = f"{h:02d}:{m:02d}"
    
    return answer
            