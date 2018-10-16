from inspect import isfunction
from KPC import KPC


class Rule:

    def __init__(self, state1, state2, trigger_signal, action):
        self.state1 = state1
        self.state2 = state2
        self.trigger_signal = trigger_signal
        self.action = action

    def matching(self, FSM):
        """Checks if rule matches the context of FSM. That is if rule.trigger_signal matches FSM.signal
        and rule.state1 matches FSM.current_state"""
        if isfunction(self.state1) and isfunction(self.trigger_signal):
            return self.state1(FSM.current_state) and self.trigger_signal(FSM.signal)
        elif isfunction(self.trigger_signal):
            return self.state1 == FSM.current_state and self.trigger_signal(FSM.signal)
        elif isfunction(self.state1):
            return self.state1(FSM.current_state) and self.trigger_signal == FSM.signal
        else:
            return self.state1 == FSM.current_state and self.trigger_signal == FSM.signal


class FSM:

    def __init__(self):
        self.rules = []
        self.signal = None
        self.current_state = "s0"
        self.KPC = KPC()

    def add_rule(self, rule):
        """Adds a rule to the rule-list of fsm"""
        self.rules.append(rule)

    def get_next_signal(self):
        self.signal = input("input: ")

    def run_rules(self):
        """Runs through the rule list and fires first matching"""
        for rule in self.rules:
            if rule.matching(self):
                self.fire_rule(rule)
                break

    def fire_rule(self, rule):
        """Calls the appropriate KPC method"""
        self.current_state = rule.state2
        print(rule.action)

    def main_loop(self):
        """Continuously collects next signal from KPC and searches for matching rule"""
        while True:
            self.get_next_signal()
            self.run_rules()

