import json

global_secret = "---|||---|||---|||---"

class Score:
    def __init__(self, max, weight, test_name):
        self.secret = global_secret
        self.test_name = test_name
        self.score = 0
        self.max_score = max
        self.weight = weight

    def increment_by(self, n):
        if self.score + n < self.max_score:
            self.score += n
        else:
            self.score = self.max_score

    def increment(self):
        if self.score < self.max_score:
            self.score += 1

    def decrement(self):
        if self.score > 0:
            self.score -= 1

    def decrement_by(self, n):
        if self.score - n > 0:
            self.score -= n
        else:
            self.score = 0

    def string(self):
        return '%s: %d/%d cases passed'.format(self.test_name, self.score, self.max_score)

    def write_string(self):
        return str({
            'Secret': self.secret,
            'TestName': self.test_name,
            'Score': self.score,
            'MaxScore': self.max_score,
            'Weight': self.weight,
        })

    def write_json(self):
        return json.dumps({
            'Secret': self.secret,
            'TestName': self.test_name,
            'Score': self.score,
            'MaxScore': self.max_score,
            'Weight': self.weight,
        })
