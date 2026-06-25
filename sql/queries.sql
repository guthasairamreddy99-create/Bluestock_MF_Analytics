-- ============================================
-- Mutual Fund Analytics SQL Queries
-- ============================================

-- 1. Display all mutual fund schemes
SELECT * FROM fund_master;

-- 2. Count total number of schemes
SELECT COUNT(*) AS total_schemes
FROM fund_master;

-- 3. List all unique fund houses
SELECT DISTINCT fund_house
FROM fund_master;

-- 4. Find the top 10 schemes by 5-year return
SELECT scheme_name, five_year_return
FROM scheme_performance
ORDER BY five_year_return DESC
LIMIT 10;

-- 5. Calculate average expense ratio
SELECT AVG(expense_ratio) AS average_expense_ratio
FROM scheme_performance;

-- 6. Find total Assets Under Management (AUM)
SELECT SUM(aum) AS total_aum
FROM aum_by_fund_house;

-- 7. Show total SIP inflows
SELECT SUM(sip_amount) AS total_sip_inflows
FROM monthly_sip_inflows;

-- 8. Find top 10 portfolio holdings by weight
SELECT company_name, sector, weight
FROM portfolio_holdings
ORDER BY weight DESC
LIMIT 10;

-- 9. Count investor transactions by transaction type
SELECT transaction_type,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type;

-- 10. Display latest NAV for each scheme
SELECT amfi_code,
MAX(nav_date) AS latest_date,
MAX(nav) AS latest_nav
FROM nav_history
GROUP BY amfi_code;