import scripts.dockerize_platypus as dockerize_platypus


organism = 'Leuconostoc'
filepath = './'
database = 'dump.sql'
dbname = 'leuconostoc_db'
init = './init.sql'


def test_create_image():
    """Method used for test image creation"""
    dockerfile = dockerize_platypus.create_image(
            organism,
            filepath,
            database,
            dbname,
            init)
    assert 'wendelhime/platypus' in dockerfile
    assert organism in dockerfile
    assert filepath in dockerfile
    assert database in dockerfile
    assert dbname in dockerfile
    assert init in dockerfile
    assert 'ENTRYPOINT' in dockerfile
    assert 'CMD' in dockerfile


def test_generate_init():
    """Method used for test generation of init"""
    content = dockerize_platypus.generate_init(
            'chadouser',
            'egene_chado',
            'leuconostoc_db')
    assert 'CREATE ROLE' in content
    assert 'ALTER USER' in content
    assert 'CREATE DATABASE' in content
    assert 'GRANT CONNECT' in content
