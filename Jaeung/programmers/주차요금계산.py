from math import ceil

def to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(fees, records):
    recs = {}
    fee = {}
    
    for record in records:
        time, num, inout = record.split()
        
        if num in recs:
            recs[num].append([time, inout])
        else:
            recs[num] = [[time, inout]]
            
    for rec in recs:
        total = 0
        
        # 입차한 기록이 있는데 출차한 기록이 없는 경우 23:59 추가
        if len(recs[rec]) % 2 != 0:
            recs[rec].append(["23:59", "OUT"])
        
        # (총 주차시간 = 출차시간 - 입차시간) 이므로, 기록이 IN이면 total에서 시간을 빼고 기록이 OUT이면 total에 시간을 더한다.
        for r in recs[rec]:
            if r[1] == "IN":
                total -= to_minutes(r[0])
            elif r[1] == "OUT":
                total += to_minutes(r[0])
                
        # 총 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해 초과한 시간에 대해서 단위 시간마다 단위 요금을 청구한다.           
        # 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림한다.
        pay = fees[1]
        if total > fees[0]:
            pay += ceil((total - fees[0]) / fees[2]) * fees[3]
        fee[rec] = pay
        
    # 차량 번호가 작은 자동차부터 청구할 주차 요금을 정렬한다.
    sorted_fee = sorted(fee.items())
    
    answer = []
    for n, f in sorted_fee:
        answer.append(f)
    return answer