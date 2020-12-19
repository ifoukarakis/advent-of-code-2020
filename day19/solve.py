class SimpleMatcher:
    def __init__(self, target):
        self.target = target

    def match(self, value):
        if value[0] == self.target:
            return True, value[1:]

        return False, value


class ReferenceMatcher:
    def __init__(self, reference, all_matchers):
        self.reference = reference
        self.all_matchers = all_matchers

    def match(self, value):
        return self.all_matchers[self.reference].match(value)


class ListMatcher:
    def __init__(self, matchers):
        self.matchers = matchers

    def match(self, value):
        remaining = value
        for matcher in self.matchers:
            is_match, remaining = matcher.match(remaining)
            if not is_match:
                return False, value

        return True, remaining


class OrMatcher:
    def __init__(self, matchers):
        self.matchers = matchers

    def match(self, value):
        remaining = value
        for matcher in self.matchers:
            is_match, remaining = matcher.match(remaining)
            if is_match:
                return True, remaining

        return False, value


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
            return ListMatcher([ReferenceMatcher(r, self.matchers) for r in rule.split(' ')])

    def match(self, idx, value):
        res, remaining = self.matchers[idx].match(value)
        return res and not remaining


FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    rule_defs, data = fp.read().split('\n\n')

    rules = RuleParser()
    for definition in rule_defs.split('\n'):
        rules.parse(definition)

    for item in data.split('\n'):
        print(rules.match('0', item))
    res = [1 if rules.match('0', line) else 0 for line in data.split('\n')]
    print(sum(res))
