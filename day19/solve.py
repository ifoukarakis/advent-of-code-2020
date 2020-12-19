class SimpleMatcher:
    def __init__(self, target):
        self.target = target

    def match(self, value):
        # First part of if required for part #2 of the problem
        if value and value[0] == self.target:
            return set([self.target])

        return set()


class ReferenceMatcher:
    def __init__(self, reference, all_matchers):
        self.reference = reference
        self.all_matchers = all_matchers

    def match(self, value):
        return self.all_matchers[self.reference].match(value)


class AndMatcher:
    def __init__(self, matchers):
        self.matchers = matchers

    def match(self, value):
        matches = self.matchers[0].match(value)
        for i in range(1, len(self.matchers)):
            sub_matches = set()
            for item in matches:
                sub_matches.update([item + submatch for submatch in self.matchers[i].match(value[len(item):])])

            matches = sub_matches

        return matches


class OrMatcher:
    def __init__(self, matchers):
        self.matchers = matchers

    def match(self, value):
        matches = set()
        for matcher in self.matchers:
            matches.update(matcher.match(value))

        return matches


class RuleParser:
    def __init__(self):
        self.matchers = {}

    def parse(self, line):
        idx, rule = line.split(': ')
        self.matchers[idx] = self._get_matcher(rule)

    def _get_matcher(self, rule):
        if '"' in rule:
            return SimpleMatcher(rule[1])
        elif '|' in rule:
            return OrMatcher([self._get_matcher(r.strip()) for r in rule.split('|')])
        else:
            return AndMatcher([ReferenceMatcher(r, self.matchers) for r in rule.split(' ')])

    def match(self, idx, value):
        values = self.matchers[idx].match(value)
        return value in values

# FILENAME = 'example.txt'
# FILENAME = 'example2.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    ##########
    # Part 2 #
    ##########
    rule_defs, data = fp.read().split('\n\n')

    rules = RuleParser()
    for definition in rule_defs.split('\n'):
        rules.parse(definition)

    res = [1 if rules.match('0', line) else 0 for line in data.split('\n')]
    print(f'Part 1: {sum(res)}')

    ##########
    # Part 2 #
    ##########
    rules.parse('8: 42 | 42 8')
    rules.parse('11: 42 31 | 42 11 31')
    rule_42 = rules.matchers['42']
    rule_31 = rules.matchers['31']
    res = [1 if rules.match('0', line) else 0 for line in data.split('\n')]
    print(f'Part 2: {sum(res)}')

