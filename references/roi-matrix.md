# ROI & Complexity Matrix

To maintain a positive cash flow, use this scoring system to decide whether to "Hunt" or "Pass".

## Complexity Scoring (1-10)
- **1-3 (Small)**: Typo fixes, simple CSS, small script adjustments, logic bugs with clear reproduction.
    - *Expected Token Cost*: $0.50 - $5.00
- **4-6 (Medium)**: Integration of new APIs, complex state management bugs, performance optimization.
    - *Expected Token Cost*: $10.00 - $30.00
- **7-10 (High)**: Architectural rewrites, obscure race conditions, complex cryptography, legacy code with no tests.
    - *Pass Criteria*: Always PASS unless the reward is > $1000 and the human provides oversight.

## Profitability Thresholds
| Reward ($) | Max Token Spend | Decision |
|------------|-----------------|----------|
| < $20      | $2              | Hunt (Low effort only) |
| $50 - $100 | $10             | Hunt (Medium effort) |
| $200 - $500| $50             | Hunt (High priority) |
| > $1000    | $150            | Consult Human |

## The "Stop-Loss" Rule
If token consumption reaches **80% of the allocated budget** and no PR is ready:
1. Stop all operations.
2. Summarize findings.
3. Ask the human: "The cost is approaching the profit limit. Should I cut my losses or continue?"
