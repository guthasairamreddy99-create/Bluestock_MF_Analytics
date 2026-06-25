-- Create tables for Mutual Fund Analytics Database

CREATE TABLE fund_master (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_grade TEXT
);

CREATE TABLE nav_history (
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL
);

CREATE TABLE aum_by_fund_house (
    fund_house TEXT,
    aum REAL
);

CREATE TABLE monthly_sip_inflows (
    month TEXT,
    sip_amount REAL
);

CREATE TABLE category_inflows (
    category TEXT,
    inflow REAL
);

CREATE TABLE industry_folio_counts (
    fund_house TEXT,
    folio_count INTEGER
);

CREATE TABLE scheme_performance (
    amfi_code INTEGER,
    one_year_return REAL,
    three_year_return REAL,
    five_year_return REAL,
    expense_ratio REAL
);

CREATE TABLE investor_transactions (
    transaction_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount REAL,
    transaction_date DATE
);

CREATE TABLE portfolio_holdings (
    amfi_code INTEGER,
    company_name TEXT,
    sector TEXT,
    weight REAL
);

CREATE TABLE benchmark_indices (
    benchmark_name TEXT,
    index_date DATE,
    index_value REAL
);