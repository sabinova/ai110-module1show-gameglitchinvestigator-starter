# 💭 Reflection: Game Glitch Investigator


## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The first time I ran the app, the UI loaded properly, but the gameplay felt unresponsive and completely out of sync. I noticed I sometimes had to click "Submit Guess" twice just to see the output update. On top of the laggy UI, the game gave mathematically incorrect hints and had completely broken win/loss states that made it impossible to play multiple rounds.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    - Wrong Hints: When the secret number was 88 and I guessed 80, the hint told me to "GO LOWER" instead of higher. The hints seem stuck or completely inverted on certain turns.
    - Laggy UI: The Attempts Left text doesn;t match the actual game state. It says I have 1 attempt left, but then immediately hits "Out of attempts". I also have to click Submit twice to see an update.
    - Broken New Game Button: When the game ends, clicking New Game updates the attampts to 8, but the game is still stuck in a Game Over state and won't actually let me play a new round.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude via the VS Code extension (using both standard chat and Agent Mode) to assist with debugging, refactoring, and generating test cases.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I asked Claude to help fix a bug where the game hints gave backward advice (e.g., "Go LOWER" when guessing 80 for a secret of 88). Claude correctly identified that on even-numbered attempts, the original code intentionally converted the secret into a string, causing a faulty string comparison in a TypeError block. It successfully moved a clean, integer-only check_guess function into logic_utils.py and removed the string conversion in app.py, which I verified by playing the game and seeing accurate hints.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - When fixing the broken "New Game" button, Claude suggested adding st.session_state.status = "playing" to unfreeze the game state. However, this suggestion was misleading because it was incomplete; Claude completely forgot to clear out st.session_state.score and st.session_state.history. I discovered this when I started a new game and saw my old guesses and previous negative score carrying over, forcing me to manually add the reset lines.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I knew a bug was fully resolved when the UI behavior accurately matched the mathematical logic without requiring workarounds. For example, moving the submit logic above the UI rendering meant I no longer had to click twice to see my attempts update, proving the rendering cycle was finally synced.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran a pytest suite for the check_guess function, specifically adding a test for check_guess(60, 68) to ensure it returned the tuple ("Too Low", "📈 Go HIGHER!"). Running this initially failed because the original starter test was poorly written and expected a simple string instead of a tuple. Fixing and passing this test proved the core game logic was sound independently of the Streamlit UI.
- Did AI help you design or understand any tests? How?
  - Yes, I used Claude to generate the specific pytest case for the hint bug I fixed. Claude also helped me understand why my tests wouldn't run initially, suggesting the python -m pytest command to fix my directory import path so the test file could find logic_utils.py

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - Streamlit reruns the entire Python script from top to bottom every time a user interacts with a widget. Because the original app didn't properly manage the session state for every variable across these reruns, the variables kept resetting.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - If we imagine Streamlit as someone reading a set of instructions from top to bottom, but every time we push a button, they start reading from the very top all over again. "Session State" is like giving them a notepad to write down important things (like the score or the secret number) so they remember them during the next read-through.
- What change did you make that finally gave the game a stable secret number?
  - By explicitly initializing st.session_state.secret and ensuring the new_game block updated all state variables before triggering an st.rerun(), the game became completely stable. I also implemented an st.form to batch the guess submission, preventing premature reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I want to maintain the habit of reviewing AI-generated code diffs line-by-line (or use plan mode) rather than blindly accepting Agent Mode changes. Testing the isolated logic using pytest was a great strategy to prove the math worked independently of the front-end UI.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Next time, I won't assume the AI is keeping track of the entire context. When dealing with session state, I will explicitly prompt the AI to account for all variables, rather than assuming it will remember to clear out arrays like history or reset scores.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project highlighted that AI can write code that looks entirely functional and production-ready on the surface, but is actually filled with structural logic traps. It taught me that I have to be a skeptical investigator and thoroughly test edge cases rather than just acting as a copy-paster.