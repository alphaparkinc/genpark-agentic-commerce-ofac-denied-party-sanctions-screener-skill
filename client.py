# -*- coding: utf-8 -*-
"""Trade Sanctions OFAC Screener for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class OFACDeniedPartySanctionsScreener:
    @staticmethod
    def screen_entity_against_sanctions_registry(entity_name: str, country_code: str, fuzzy_threshold_pct: float = 85.0) -> Dict[str, Any]:
        # Comprehensive embargoed regions
        embargoed = ["CU", "IR", "KP", "SY", "RU"]
        is_embargoed_jurisdiction = country_code.upper() in embargoed
        
        name_lower = entity_name.lower()
        sdn_hits = []
        mock_sdn_targets = ["rosneft", "sberbank", "al-qaeda", "irgc", "wagner group", "huawei technologies"]
        for target in mock_sdn_targets:
            if target in name_lower:
                sdn_hits.append(target.upper())
                
        is_hit = is_embargoed_jurisdiction or len(sdn_hits) > 0
        status = "CRITICAL_SANCTIONS_MATCH_TRANSACTION_BLOCKED" if is_hit else "CLEARED_FOR_EXPORT"
        
        return {
            "entity": entity_name,
            "country": country_code,
            "embargoed_jurisdiction": is_embargoed_jurisdiction,
            "registry_hits": sdn_hits,
            "compliance_status": status,
            "regulatory_mandate": "Immediate transaction freeze per 31 C.F.R. Chapter V" if is_hit else "Export clearance granted."
        }

    @staticmethod
    def generate_compliance_hold_blocking_memo(transaction_id: str, entity_name: str, match_score_pct: float, matched_list: str = "OFAC SDN") -> Dict[str, Any]:
        return {
            "transaction_reference": transaction_id,
            "restricted_party": entity_name,
            "matched_sanctions_list": matched_list,
            "match_confidence_pct": match_score_pct,
            "legal_directive": "Escrow funds and halt fulfillment. File formal disclosure with US Treasury OFAC within 10 business days."
        }
