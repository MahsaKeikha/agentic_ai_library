# F117 Three-Minute Demonstration Script

## 0:00 to 0:30 | The problem

"This packaging-line motor is still producing, but its temperature, vibration, and current have crossed declared limits. A conventional dashboard can show the signals. The harder question is what the organization should do next, what evidence supports that decision, and who has authority to act."

Show the synthetic telemetry input and state `TRIP_THRESHOLD_EXCEEDED`.

## 0:30 to 1:10 | The agent team

"Five specialist agents now work from the same traceable input. The interface agent validates the telemetry contract. The state estimator establishes the present condition. The diagnosis agent ranks competing causes. The simulation agent compares response options. The deployment gatekeeper enforces the authority boundary."

Show the five trace events and the ranked hypotheses.

## 1:10 to 1:50 | The what-if comparison

"The twin does not claim to predict the future with certainty. It declares its assumptions and compares three bounded scenarios: continue and monitor, derate to 70 percent, or perform a controlled stop and inspection."

Show the projected risk, temperature, throughput, and assumptions for all three options.

## 1:50 to 2:25 | The human boundary

"The lowest-risk option is a controlled stop and inspection. That is a protected action. The system cannot issue a PLC command, change a setpoint, or bypass the site procedure. It stops here and requests an authorized engineer."

Show `AWAITING AUTHORIZED ENGINEER APPROVAL` and `command_issued: false`.

## 2:25 to 2:45 | The controlled next step

Run the demonstration with `--approve`.

"A complete synthetic approval record changes the governance status, but it does not give the model equipment authority. The result says `AUTHORIZED FOR SITE PROCEDURE - NO COMMAND ISSUED`."

## 2:45 to 3:00 | The message

"This is what the Multi-Agent AI Atlas is designed to make visible. Intelligence is only one layer. Production trust also requires evidence, coordination, failure behavior, traceability, and human authority."
