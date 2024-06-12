class Team:
    def __init__(self, name, over_0_5, over_1_5, over_2_5, over_3_5, under_0_5, under_1_5, under_2_5, under_3_5) -> None:
        self.name = name
        self.over_0_5 = over_0_5
        self.over_1_5 = over_1_5
        self.over_2_5 = over_2_5
        self.over_3_5 = over_3_5
        self.under_0_5 = under_0_5
        self.under_1_5 = under_1_5
        self.under_2_5 = under_2_5
        self.under_3_5 = under_3_5

    def most_likely_score(self) -> int:
        # There is no guarantee that a score will be always less than 5 but it is always unlikely to go over 4
        goals_prob = {
            0: self.under_0_5,
            1: self.over_0_5 * self.under_1_5,
            2: self.over_1_5 * self.under_2_5,
            3: self.over_2_5 * self.under_3_5,
            4: self.over_3_5
        }

        max_prob = 0
        likely_goals = 0

        for goals, prob in goals_prob.items():
            if prob > max_prob:
                max_prob = prob
                likely_goals = goals

        return likely_goals

