def resistivity(salinity, temperature):
    table = {
        (1, 0): 0.001839, (1, 5): 0.002134, (1, 10): 0.002439, (1, 15): 0.002763, (1, 20): 0.003091, (1, 30): 0.003431,
    (2, 0): 0.003556, (2, 5): 0.004125, (2, 10): 0.004714, (2, 15): 0.005338, (2, 20): 0.005971, (2, 30): 0.006628,
    (3, 0): 0.005187, (3, 5): 0.006016, (3, 10): 0.006872, (3, 15): 0.007778, (3, 20): 0.008702, (3, 30): 0.009658,
    (4, 0): 0.006758, (4, 5): 0.007845, (4, 10): 0.008958, (4, 15): 0.010133, (4, 20): 0.011337, (4, 30): 0.012583,
    (5, 0): 0.008327, (5, 5): 0.009653, (5, 10): 0.011019, (5, 15): 0.012459, (5, 20): 0.013939, (5, 30): 0.015471,
    (6, 0): 0.009878, (6, 5): 0.011444, (6, 10): 0.013063, (6, 15): 0.014758, (6, 20): 0.016512, (6, 30): 0.018324,
    (7, 0): 0.011404, (7, 5): 0.013203, (7, 10): 0.015069, (7, 15): 0.017015, (7, 20): 0.019035, (7, 30): 0.021121,
    (8, 0): 0.012905, (8, 5): 0.014934, (8, 10): 0.017042, (8, 15): 0.019235, (8, 20): 0.021514, (8, 30): 0.023868,
    (9, 0): 0.014388, (9, 5): 0.016641, (9, 10): 0.018986, (9, 15): 0.021423, (9, 20): 0.023957, (9, 30): 0.026573,
    (10, 0): 0.015852, (10, 5): 0.018329, (10, 10): 0.020906, (10, 15): 0.023584, (10, 20): 0.026367, (10, 30): 0.029242,
    (11, 0): 0.017304, (11, 5): 0.020000, (11, 10): 0.022804, (11, 15): 0.025722, (11, 20): 0.028749, (11, 30): 0.031879,
    (12, 0): 0.018741, (12, 5): 0.021655, (12, 10): 0.024684, (12, 15): 0.027841, (12, 20): 0.031109, (12, 30): 0.034489,
    (13, 0): 0.020167, (13, 5): 0.023297, (13, 10): 0.026548, (13, 15): 0.029940, (13, 20): 0.033447, (13, 30): 0.037075,
    (14, 0): 0.021585, (14, 5): 0.024929, (14, 10): 0.028397, (14, 15): 0.032024, (14, 20): 0.035765, (14, 30): 0.039638,
    (15, 0): 0.022993, (15, 5): 0.026548, (15, 10): 0.030231, (15, 15): 0.034090, (15, 20): 0.038065, (15, 30): 0.042180,
    (16, 0): 0.024393, (16, 5): 0.028156, (16, 10): 0.032050, (16, 15): 0.036138, (16, 20): 0.040345, (16, 30): 0.044701,
    (17, 0): 0.025783, (17, 5): 0.029753, (17, 10): 0.033855, (17, 15): 0.038168, (17, 20): 0.042606, (17, 30): 0.047201,
    (18, 0): 0.027162, (18, 5): 0.031336, (18, 10): 0.035644, (18, 15): 0.040176, (18, 20): 0.044844, (18, 30): 0.049677,
    (19, 0): 0.028530, (19, 5): 0.032903, (19, 10): 0.037415, (19, 15): 0.042158, (19, 20): 0.047058, (19, 30): 0.052127,
    (20, 0): 0.029885, (20, 5): 0.034454, (20, 10): 0.039167, (20, 15): 0.044114, (20, 20): 0.049248, (20, 30): 0.054551,
    (21, 0): 0.031227, (21, 5): 0.035989, (21, 10): 0.040900, (21, 15): 0.046044, (21, 20): 0.051414, (21, 30): 0.056949,
    (22, 0): 0.032556, (22, 5): 0.037508, (22, 10): 0.042614, (22, 15): 0.047948, (22, 20): 0.053556, (22, 30): 0.059321
    }

    # nearest temperatures from the table
    temp_lower = None
    temp_higher = None
    for temp in sorted(table[salinity].keys()):
        if temp <= temperature:
            temp_lower = temp
        else:
            temp_higher = temp
            break

    # interpolation
    sp_cond_lower = table[salinity][temp_lower]
    sp_cond_higher = table[salinity][temp_higher]
    sp_conductance = sp_cond_lower + (sp_cond_higher - sp_cond_lower) * (temperature - temp_lower) / (temp_higher - temp_lower)

    resistivity = 1 / sp_conductance
    
    return resistivity

salinity = int(input("enter salinity value :"))
temperature = int(input("enter temperature value :"))

result = resistivity(salinity, temperature)

print("The Resistivity for the given salinity and temperature is", round(result,2))
