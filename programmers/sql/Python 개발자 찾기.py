select ID, EMAIL, FIRST_NAME, LAST_NAME
from developer_infos
where skill_1 = "Python" or skill_2 = "Python" or skill_3 = "Python"
ORDER BY ID ASC;