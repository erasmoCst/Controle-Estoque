-- Move tabelas para tablespace
DECLARE
  v_tablespace_to_move VARCHAR2(100) := 'USERS';
  v_schema VARCHAR2(100) :=  'CTL_ESTOQUE';
  v_sql VARCHAR2(1000);
BEGIN
  FOR t IN (SELECT table_name FROM all_tables WHERE owner = 'CTL_ESTOQUE') LOOP
    v_sql := 'ALTER TABLE ' || v_schema ||'.' || t.table_name || ' MOVE TABLESPACE ' || v_tablespace_to_move;
    EXECUTE IMMEDIATE v_sql;
    DBMS_OUTPUT.PUT_LINE(v_sql);
  END LOOP;
END;

-- Permissão para insert nas tabelas
DECLARE
  v_tablespace_to_move VARCHAR2(100) := 'USERS';
  v_schema VARCHAR2(100) :=  'CTL_ESTOQUE';
  v_sql VARCHAR2(1000);
BEGIN
  FOR t IN (SELECT table_name FROM all_tables WHERE owner = 'CTL_ESTOQUE') LOOP
    v_sql := 'GRANT INSERT ON ' || v_schema ||'.' || t.table_name || ' TO ' || v_schema;
    EXECUTE IMMEDIATE v_sql;
    DBMS_OUTPUT.PUT_LINE(v_sql);
  END LOOP;
END;


ALTER USER CTL_ESTOQUE QUOTA UNLIMITED ON USERS;
