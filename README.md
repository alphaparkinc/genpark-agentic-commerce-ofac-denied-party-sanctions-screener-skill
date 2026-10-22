# Trade Sanctions OFAC SDN & Denied Party Compliance Screener Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

OFAC Specially Designated Nationals (SDN), BIS Entity List fuzzy string Levenshtein compliance, and automated international embargo blocker. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `screen_entity_against_sanctions_registry`: Fuzzy match individual or corporate entity name and country against international export control databases.
- `generate_compliance_hold_blocking_memo`: Generate formal AML/OFAC transaction hold memo for flagged payment or shipment export.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_ofac_denied_party_sanctions_screener_skill.server --test
```
