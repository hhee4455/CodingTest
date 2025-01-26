def solution(book_time):
    book = []
    
    for time in book_time:
        start, end = time
        s_HH, s_MM = map(int, start.split(":"))
        e_HH, e_MM = map(int, end.split(":"))
        book.append((s_HH * 60 + s_MM, e_HH * 60 + e_MM + 10))  
    
    book = sorted(book, key=lambda x: x[0])
    
    def count_overlaps(intervals):
        events = []

        for start, end in intervals:
            events.append((start, 1)) 
            events.append((end, -1))
            
        events.sort(key=lambda x: (x[0], x[1]))

        max_overlaps = 0
        current_overlaps = 0

        for _, event in events:
            current_overlaps += event 
            max_overlaps = max(max_overlaps, current_overlaps)

        return max_overlaps

    return count_overlaps(book)
