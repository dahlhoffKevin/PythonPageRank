USE MediaWiki;

SELECT old_text 
  FROM text as t 
  LEFT JOIN revision as r ON r.rev_parent_id = t.old_id 
  LEFT JOIN page as p ON p.page_latest = r.rev_id 
  WHERE 
    p.page_title = "Hauptseite"; 
