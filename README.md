# IT System Troubleshooting Expert System

A rule-based expert system that diagnoses common IT problems using forward chaining inference.

## Features

- **Knowledge Base**: 8 diagnostic rules covering hardware, software, and network issues
- **Inference Engine**: Forward chaining algorithm for automated reasoning
- **Interactive UI**: Console-based question/answer interface
- **Explanation Facility**: Detailed reasoning chain showing why conclusions were reached

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone or download `it_expert_system.py`
2. Ensure Python 3 is installed:
   ```bash
   python3 --version
   ```

## Usage

Run the expert system:
```bash
python3 it_expert_system.py
```

Answer yes/no questions about your system's symptoms. The system will:
1. Gather facts through targeted questions
2. Apply diagnostic rules
3. Provide diagnosis with confidence scores
4. Explain the reasoning behind conclusions
5. Suggest specific solutions

## Example Scenarios

**Network Issue:**
- Computer powers on → Boots normally → No internet → Other devices connected
- **Diagnosis**: Network adapter or driver problem

**Malware Suspicion:**
- System boots → Slow performance → Strange pop-ups appearing
- **Diagnosis**: Potential malware infection

**Hardware Failure:**
- Computer does not power on
- **Diagnosis**: Hardware power issue

## System Architecture

```
User Input → Fact Collection → Inference Engine → Rule Matching → Diagnosis + Explanation
```

## Rule Base Summary

- **R1**: Hardware power issues
- **R2**: Boot failures
- **R3**: Disk bottleneck
- **R4**: Network adapter problems
- **R5**: Router/ISP issues
- **R6**: Driver/hardware faults
- **R7**: Insufficient resources
- **R8**: Malware detection

