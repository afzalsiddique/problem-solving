select distinct title from content
    join tvprogram using(content_id)
where left(program_date,7)='2020-06'
    and kids_content='Y'
    and content_type='Movies'