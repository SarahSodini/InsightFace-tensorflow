from scipy import stats

balanced_mixed = [
	0.87924, 
	0.87055, 
	0.88073, 
    0.86469, 
	0.87973
]

balanced_uniform1 = [
    0.87142,
	0.86311,
	0.86811,
	0.86776,
	0.87166,
]

balanced_uniform3 = [
    0.85022,
	0.84653,
	0.85829,
	0.8398,
	0.85466
]

unbalanced_mixed = [
	0.88165, 
	0.86883, 
	0.87962, 
    0.87003, 
	0.87013
]

unbalanced_uniform1 = [
    0.86171,
	0.84071,
	0.85714,
	0.8529,
	0.84769,
]

unbalanced_uniform3 = [
    0.87119,
	0.86871,
	0.86347,
	0.86445,
	0.86755
]

test = stats.friedmanchisquare(balanced_mixed, balanced_uniform1, balanced_uniform3)

print(test)