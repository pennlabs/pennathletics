import collections

Sport = collections.namedtuple('Sport', 'SPID SPSID')

SPORTS = {
    'M_Baseball': Sport(548, 8834),
    'M_Basketball': Sport(539, 8627),
    'M_Track_Cross': Sport(542, 8699),
    'M_Fencing': Sport(607, 10603),
    'M_Football': Sport(537, 8571),
    'M_Sprint_Football': (612, 10618),
    'M_Golf': Sport(550, 8895),
    'M_Lacrosse': Sport(544, 8745),
    'M_Heavy_Rowing': Sport(610, 10659),
    'M_Light_Rowing': Sport(613, 10647),
    'M_Soccer': Sport(604, 10672),
    'M_Squash': Sport(605, 10685),
    'M_Swimming': Sport(611, 10698),
    'M_Tennis': Sport(552, 8927),
    'M_Wrestling': Sport(543, 8720),
    'W_Basketball': Sport(540, 8650),
    'W_Track_Cross': Sport(558, 10758),
    'W_Fencing': Sport(608, 10715),
    'W_Hockey': Sport(609, 10583),
    'W_Golf': Sport(551, 8903),
    'W_Gymnastics': Sport(545, 8763),
    'W_Lacrosse': Sport(554, 8966),
    'W_Rowing': Sport(555, 8993),
    'W_Soccer': Sport(541, 8673),
    'W_Softball': Sport(549, 8856),
    'W_Squash': Sport(606, 10741),
    'W_Swimming': Sport(546, 8790),
    'W_Tennis': Sport(553, 8943),
    'W_Volleyball': Sport(538, 8606)
}

# print (W_Volleyball.SPID)
