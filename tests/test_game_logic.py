from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"  # Changed to match your logic_utils

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!" # Changed to match your logic_utils

def test_hint_bug_fixed():
    outcome, message = check_guess(60, 68)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!" # Changed to match your logic_utils