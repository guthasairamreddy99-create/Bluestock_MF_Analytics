# Data Dictionary

## fund_master
| Column | Description |
|--------|-------------|
| amfi_code | Unique AMFI Scheme Code |
| scheme_name | Mutual Fund Scheme Name |
| fund_house | Asset Management Company |
| category | Fund Category |
| sub_category | Fund Sub Category |
| risk_grade | Risk Level |

## nav_history
| Column | Description |
|--------|-------------|
| amfi_code | AMFI Scheme Code |
| nav_date | NAV Date |
| nav | Net Asset Value |

## aum_by_fund_house
| Column | Description |
|--------|-------------|
| fund_house | Fund House |
| aum | Assets Under Management |

## monthly_sip_inflows
| Column | Description |
|--------|-------------|
| month | Month |
| sip_amount | SIP Amount |

## investor_transactions
| Column | Description |
|--------|-------------|
| transaction_id | Transaction ID |
| transaction_type | Purchase/Redemption |
| amount | Transaction Amount |
| transaction_date | Date of Transaction |