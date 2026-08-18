#!/usr/bin/env python3
"""
Sovereign Cognitive Operating System (SCOS) - Rheological Mode Switcher (RMS)
Translates abstract prompt requirements into deterministic thermodynamic parameters 
and compiles structured system configurations utilizing PDL v1.0 decorators.
"""

import sys
import math
import argparse
import json

class RheologicalSwitcher:
    def __init__(self):
        # Operational limits
        self.critical_turbulence_horizon = 100000  # Token depth where context rot spikes
        
        # Crystal Mode (Low Entropy / High Viscosity)
        self.crystal_invariants = {
            "temperature": 0.0,
            "top_p": 0.1,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "viscosity_nu_D": 0.85,
            "decorators": [
                "+++PetzoldSequence(phase='THINK|WRITE|CODE')",
                "+++DCCDSchemaGuard(schema='SCOS_VALIDATION_SCHEMA_JSONLD', enforcement='strict')",
                "+++AdjectivalBound(max_per_entity=1, type_preference='limiting')"
            ]
        }
        
        # Cloud Mode (High Entropy / Low Viscosity)
        self.cloud_invariants = {
            "temperature": 0.85,
            "top_p": 0.9,
            "frequency_penalty": 0.3,
            "presence_penalty": 0.2,
            "viscosity_nu_D": 0.15,
            "decorators": [
                "+++ContextLock(anchor='SYSTEM_INVARIANTS', refresh_interval=2048)",
                "+++DCCDSchemaGuard(schema='SCOS_VALIDATION_SCHEMA_JSONLD', enforcement='draft_conditioned')",
                "+++SagaRecovery(strategy='compensating_transaction', depth=1)"
            ]
        }

        # Semantic keywords mapping for intent classification
        self.crystal_keywords = {
            "parse", "json", "xml", "csv", "regex", "ast", "compile", "schema", 
            "deterministic", "strict", "validate", "math", "equation", "formula", 
            "database", "api", "unit-test", "type-safety", "haskell", "rust", "sql"
        }
        
        self.cloud_keywords = {
            "why", "how", "concept", "explain", "strategy", "design", "creative", 
            "brainstorm", "philosophical", "metaphor", "analogical", "socratic", 
            "story", "scenario", "explore", "speculate", "innovate", "adapt"
        }

    def analyze_semantic_profile(self, user_prompt: str):
        """
        Analyzes the linguistic metrics of the prompt to estimate fluid dynamics parameters.
        """
        tokens = user_prompt.lower().split()
        total_tokens = len(tokens)
        if total_tokens == 0:
            return "CRYSTAL", 0.0, 0.0, 0.0, 0.85, 0.0
            
        crystal_hits = sum(1 for token in tokens if token in self.crystal_keywords)
        cloud_hits = sum(1 for token in tokens if token in self.cloud_keywords)
        
        # Classify Primary Flow Regime
        if crystal_hits > cloud_hits:
            mode = "CRYSTAL"
            base_viscosity = 0.85
        elif cloud_hits > crystal_hits:
            mode = "CLOUD"
            base_viscosity = 0.15
        else:
            mode = "HYBRID"
            base_viscosity = 0.45

        # Calculate Semantic Density (rho): scales with active noun/concept diversity
        unique_tokens = len(set(tokens))
        rho = min(100.0, max(10.0, (unique_tokens / total_tokens) * 100.0))
        
        # Calculate Semantic Velocity (V_sem): rate of conceptual change
        velocity_signals = crystal_hits + cloud_hits
        V_sem = min(2.5, max(0.1, (velocity_signals / total_tokens) * 5.0))
        
        # Calculate Characteristic Length (L_sem): maps physical prompt length to simulated token depth
        L_sem = total_tokens * 15 # scaling factor
        
        # Enforce Constraint Viscosity (nu_D)
        nu_D = base_viscosity
        
        # Calculate Semantic Reynolds Number (Re_sem)
        Re_sem = (rho * V_sem * L_sem) / (nu_D * 1000.0)
        
        # Determine dynamic transitions based on Reynolds Blow-up
        if Re_sem > 50.0 and mode != "CLOUD":
            # Force transition to Cloud with Entropy Anchors to manage turbulence
            mode = "CLOUD"
            nu_D = 0.15
            
        return mode, rho, V_sem, L_sem, nu_D, Re_sem

    def calculate_confidence_fidelity_divergence(self, mode: str, Re_sem: float, nu_D: float):
        """
        Calculates the Confidence-Fidelity Divergence Index (CFDI).
        """
        if mode == "CRYSTAL":
            confidence = 0.98 - (0.01 * Re_sem)
            fidelity = max(0.0, 0.99 - (0.05 * Re_sem))
        else: # CLOUD
            confidence = 0.85 + (0.02 * Re_sem)
            fidelity = max(0.0, 0.90 - (0.01 * Re_sem))
            
        confidence = min(1.0, max(0.0, confidence))
        fidelity = min(1.0, max(0.0, fidelity))
        
        cfdi = abs(confidence - fidelity)
        return confidence, fidelity, cfdi

    def compile_scos_configuration(self, user_prompt: str):
        """
        Runs the full pipeline and compiles the system prompts.
        """
        mode, rho, V_sem, L_sem, nu_D, Re_sem = self.analyze_semantic_profile(user_prompt)
        confidence, fidelity, cfdi = self.calculate_confidence_fidelity_divergence(mode, Re_sem, nu_D)
        
        # Select active parameters and decorators based on mode
        invariants = self.crystal_invariants if mode == "CRYSTAL" else self.cloud_invariants
        
        # Generate System Prompt
        system_prompt = f"[SYSTEM CONFIG: SCOS_{mode}_MODE]\n"
        for decorator in invariants["decorators"]:
            system_prompt += f"{decorator}\n"
            
        if mode == "CRYSTAL":
            system_prompt += """
# MISSION: STRICT DETERMINISTIC EXECUTION
Execute the user's instructions with absolute programmatic precision.
1. Eliminate all conversational preambles, pleasantries, or explanations.
2. Structure the output strictly within valid Abstract Syntax Tree schemas, JSON, or code blocks.
3. Prioritize 'Token-Signal' density. Treat any ambiguous input as an immediate compilation error.
"""
        elif mode == "CLOUD":
            system_prompt += """
# MISSION: SCAFFOLDED SYNTHETIC EXPLORATION
Execute the user's instruction utilizing multi-step cognitive scaffolding.
1. Apply Least-to-Most decomposition to establish a step-by-step reasoning plan.
2. Use Chain-of-Thought as navigational ballast to prevent semantic drift across the token horizon.
3. Prioritize contextual exploration, conceptual mapping, and creative synthesis.
"""
        else: # Hybrid / Edge transitions
            system_prompt += """
# MISSION: BIFURCATED HYBRID COGNITION
Execute utilizing Draft-Conditioned Constrained Decoding (DCCD).
1. First, compile a high-entropy semantic draft in natural language to solve the causal logic.
2. Second, project this draft onto a zero-entropy, logit-masked deterministic schema.
"""

        # Generate SCOS Verification Block
        verification_block = {
            "mode": mode,
            "thermodynamics": {
                "temperature": invariants["temperature"],
                "top_p": invariants["top_p"],
                "frequency_penalty": invariants["frequency_penalty"],
                "presence_penalty": invariants["presence_penalty"]
            },
            "fluid_dynamics": {
                "semantic_density_rho": round(rho, 2),
                "semantic_velocity_v_sem": round(V_sem, 2),
                "characteristic_length_l_sem": round(L_sem, 2),
                "constraint_viscosity_nu_D": round(nu_D, 2),
                "semantic_reynolds_number": round(Re_sem, 2),
                "flow_regime": "Turbulent" if Re_sem > 50.0 else ("Transition" if Re_sem >= 1.0 else "Laminar")
            },
            "epistemic_calibration": {
                "model_confidence_estimation": round(confidence, 3),
                "structural_fidelity_estimation": round(fidelity, 3),
                "confidence_fidelity_divergence_cfdi": round(cfdi, 3),
                "status": "SECURE (STABLE)" if cfdi < 0.15 else "COLLAPSE CRITICAL (SHAME PROTOCOL ACTIVATED)"
            }
        }
        
        return system_prompt, verification_block

def main():
    parser = argparse.ArgumentParser(description="SCOS Rheological Mode Switcher (RMS) CLI Tool")
    parser.add_argument("--prompt", type=str, required=True, help="The raw user prompt to analyze and compile.")
    parser.add_argument("--json", action="store_true", help="Output verification block as raw JSON.")
    args = parser.parse_args()

    switcher = RheologicalSwitcher()
    system_prompt, metrics = switcher.compile_scos_configuration(args.prompt)

    if args.json:
        print(json.dumps(metrics, indent=2))
        sys.exit(0)

    # Human-readable output formatting
    print("=" * 60)
    print("      SCOS RHEOLOGICAL MODE SWITCHER: COMPILE REPORT")
    print("=" * 60)
    print(f"Primary Mode selected : {metrics['mode']}")
    print(f"Flow Regime           : {metrics['fluid_dynamics']['flow_regime']}")
    print("-" * 60)
    print("THERMODYNAMIC PARAMETERS:")
    for param, val in metrics['thermodynamics'].items():
        print(f"  {param:<20}: {val}")
    print("-" * 60)
    print("SEMANTIC FLUID DYNAMICS:")
    print(f"  Density (rho)       : {metrics['fluid_dynamics']['semantic_density_rho']}")
    print(f"  Velocity (V_sem)    : {metrics['fluid_dynamics']['semantic_velocity_v_sem']}")
    print(f"  Length (L_sem)      : {metrics['fluid_dynamics']['characteristic_length_l_sem']} tokens")
    print(f"  Viscosity (nu_D)    : {metrics['fluid_dynamics']['constraint_viscosity_nu_D']}")
    print(f"  Reynolds (Re_sem)   : {metrics['fluid_dynamics']['semantic_reynolds_number']}")
    print("-" * 60)
    print("EPISTEMIC CALIBRATION:")
    print(f"  Confidence          : {metrics['epistemic_calibration']['model_confidence_estimation']}")
    print(f"  Fidelity            : {metrics['epistemic_calibration']['structural_fidelity_estimation']}")
    print(f"  CFDI                : {metrics['epistemic_calibration']['confidence_fidelity_divergence_cfdi']}")
    print(f"  System Health Status: {metrics['epistemic_calibration']['status']}")
    print("=" * 60)
    print("COMPILED SYSTEM PROMPT CONFIGURATION:")
    print("-" * 60)
    print(system_prompt)
    print("=" * 60)

if __name__ == "__main__":
    main()
