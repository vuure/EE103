from list_tools import get_stats

list_odd_nums = [i for i in range(10) if not(i%2 == 0)]
print(list_odd_nums)

m_getStats = get_stats(list_odd_nums)
print(f'Min: {m_getStats[0]}, Max: {m_getStats[1]}, Average: {m_getStats[2]:.2f}')