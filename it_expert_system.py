class ITExpertSystem:
    def __init__(self):
        # Knowledge Base: Store facts gathered from user
        self.facts = {}
        
        # Store the reasoning path for explanation
        self.reasoning_chain = []
        
        # Define the rule base
        self.rules = {
            'R1': {
                'condition': lambda f: not f.get('power_on', True),
                'conclusion': 'hardware_power_issue',
                'message': 'Hardware Power Issue Detected',
                'solution': 'Check power cable, outlet, and power supply unit. Try a different power outlet.',
                'confidence': 95
            },
            'R2': {
                'condition': lambda f: f.get('power_on') and not f.get('boots'),
                'conclusion': 'boot_failure',
                'message': 'Boot Failure - Hardware or OS Issue',
                'solution': 'Check BIOS settings, verify boot device, or reinstall operating system.',
                'confidence': 90
            },
            'R3': {
                'condition': lambda f: f.get('boots') and f.get('slow_performance') and f.get('high_disk_usage'),
                'conclusion': 'disk_bottleneck',
                'message': 'System Bottleneck - Disk Performance Issue',
                'solution': 'Run disk cleanup, check for malware, consider upgrading to SSD, or add more RAM.',
                'confidence': 85
            },
            'R4': {
                'condition': lambda f: f.get('boots') and not f.get('internet_connection') and f.get('other_devices_connected'),
                'conclusion': 'network_adapter_issue',
                'message': 'Network Adapter or Driver Problem',
                'solution': 'Update network drivers, reset network adapter, check firewall settings.',
                'confidence': 80
            },
            'R5': {
                'condition': lambda f: f.get('boots') and not f.get('internet_connection') and not f.get('other_devices_connected'),
                'conclusion': 'router_isp_issue',
                'message': 'Router or ISP Connection Problem',
                'solution': 'Restart router/modem, check ISP service status, verify cable connections.',
                'confidence': 90
            },
            'R6': {
                'condition': lambda f: f.get('boots') and f.get('frequent_crashes') and f.get('blue_screen'),
                'conclusion': 'driver_or_hardware_fault',
                'message': 'Critical System Error - Driver or Hardware Fault',
                'solution': 'Update all drivers, run memory diagnostic, check for overheating, test hardware components.',
                'confidence': 85
            },
            'R7': {
                'condition': lambda f: f.get('boots') and f.get('slow_performance') and not f.get('high_disk_usage') and f.get('many_programs'),
                'conclusion': 'insufficient_resources',
                'message': 'Insufficient System Resources',
                'solution': 'Close unnecessary programs, upgrade RAM, check for resource-heavy background processes.',
                'confidence': 80
            },
            'R8': {
                'condition': lambda f: f.get('boots') and f.get('strange_popups') and f.get('slow_performance'),
                'conclusion': 'malware_infection',
                'message': 'Potential Malware or Virus Infection',
                'solution': 'Run full antivirus scan, use malware removal tools, enable real-time protection.',
                'confidence': 88
            }
        }
    
    def gather_facts(self):
        """User Interface: Collect information from user"""
        print("\n" + "="*60)
        print("   IT SYSTEM TROUBLESHOOTING EXPERT SYSTEM")
        print("="*60)
        print("\nPlease answer the following questions (yes/no):\n")
        
        questions = [
            ('power_on', "Does the computer power on when you press the power button?"),
            ('boots', "Does the system boot to the operating system?", 'power_on', True),
            ('internet_connection', "Is there an internet connection?", 'boots', True),
            ('other_devices_connected', "Are other devices able to connect to the internet?", 'internet_connection', False),
            ('slow_performance', "Is the system running slowly?", 'boots', True),
            ('high_disk_usage', "Is disk usage consistently high (>90%)?", 'slow_performance', True),
            ('many_programs', "Are many programs running simultaneously?", 'slow_performance', True),
            ('frequent_crashes', "Does the system crash frequently?", 'boots', True),
            ('blue_screen', "Do you see blue screen errors (BSOD)?", 'frequent_crashes', True),
            ('strange_popups', "Are there strange pop-ups or unexpected behaviors?", 'boots', True)
        ]
        
        for question_data in questions:
            key = question_data[0]
            question = question_data[1]
            
            # Check if this question should be asked based on previous answers
            if len(question_data) > 2:
                prerequisite_key = question_data[2]
                required_value = question_data[3]
                if self.facts.get(prerequisite_key) != required_value:
                    continue
            
            while True:
                answer = input(f"{question} (yes/no): ").strip().lower()
                if answer in ['yes', 'y']:
                    self.facts[key] = True
                    break
                elif answer in ['no', 'n']:
                    self.facts[key] = False
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
    
    def forward_chaining(self):
        """Inference Engine: Apply rules using forward chaining"""
        print("\n" + "-"*60)
        print("   ANALYZING SYMPTOMS...")
        print("-"*60)
        
        diagnoses = []
        
        # Apply each rule and collect matching diagnoses
        for rule_id, rule in self.rules.items():
            if rule['condition'](self.facts):
                self.reasoning_chain.append({
                    'rule_id': rule_id,
                    'conclusion': rule['conclusion'],
                    'message': rule['message'],
                    'solution': rule['solution'],
                    'confidence': rule['confidence']
                })
                diagnoses.append(rule)
        
        return diagnoses
    
    def explain_reasoning(self, diagnoses):
        """Explanation Facility: Show reasoning behind conclusions"""
        print("\n" + "="*60)
        print("   DIAGNOSTIC REPORT")
        print("="*60)
        
        if not diagnoses:
            print("\n❌ No specific issue identified based on the symptoms provided.")
            print("\nGeneral Recommendations:")
            print("  • Run a complete system diagnostic")
            print("  • Check system logs for errors")
            print("  • Consult with IT support for in-depth analysis")
            return
        
        print(f"\n✓ Found {len(diagnoses)} potential issue(s):\n")
        
        # Sort by confidence level
        diagnoses.sort(key=lambda x: x['confidence'], reverse=True)
        
        for idx, diagnosis in enumerate(diagnoses, 1):
            print(f"--- Issue #{idx} ---")
            print(f"Diagnosis: {diagnosis['message']}")
            print(f"Confidence: {diagnosis['confidence']}%")
            print(f"Solution: {diagnosis['solution']}")
            print()
        
        # Show detailed reasoning
        print("-"*60)
        print("   REASONING CHAIN")
        print("-"*60)
        print("\nThe expert system evaluated the following facts:\n")
        
        for key, value in self.facts.items():
            status = "✓ YES" if value else "✗ NO"
            print(f"  • {key.replace('_', ' ').title()}: {status}")
        
        print("\nBased on these facts, the following rules were triggered:\n")
        
        for step in self.reasoning_chain:
            print(f"  • Rule {step['rule_id']}: {step['message']}")
            print(f"    → Confidence: {step['confidence']}%")
        
        print("\n" + "="*60)
        print("   END OF DIAGNOSTIC REPORT")
        print("="*60)
    
    def run(self):
        """Main execution method"""
        self.gather_facts()
        diagnoses = self.forward_chaining()
        self.explain_reasoning(diagnoses)
        
        # Ask if user wants to start over
        print("\n")
        restart = input("Would you like to diagnose another issue? (yes/no): ").strip().lower()
        if restart in ['yes', 'y']:
            self.facts = {}
            self.reasoning_chain = []
            print("\n" * 2)
            self.run()
        else:
            print("\nThank you for using the IT Troubleshooting Expert System!")
            print("Stay tech-savvy! 💻")


# Run the expert system
if __name__ == "__main__":
    expert_system = ITExpertSystem()
    expert_system.run()