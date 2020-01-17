import os

from sqlalchemy import text, create_engine

mysql_host = "mysql+pymysql://{0}/himama".format(os.getenv("MYSQL_HOST"))

engine = create_engine(mysql_host, pool_size=20, pool_recycle=3600)


def execute(statement, *multiparams, **params):
    with engine.connect() as conn:
        return conn.execute(statement, *multiparams, **params)


def get_user_by_id(user_id):
    sql = text("SELECT email, name, avatar FROM user WHERE id=:user_id")
    return execute(sql, user_id=user_id).fetchont()


def validate_user(email, password):
    # TBD(hard coding for now)
    # SHA-256 or BCrypt + salt
    return True


def create_clock_event(user_id, event_type, timestamp, created_at):
    sql = text("INSERT INTO clock_events (user_id, event_type, timestamp, created_at) \
               VALUES (:user_id, :event_type, :timestamp, :created_at)")
    execute(sql,
            user_id=user_id,
            event_type=event_type,
            timestamp=timestamp,
            created_at=created_at)


def get_all_clock_events():
    sql = text("SELECT event_type, timestamp FROM clock_events WHERE is_deleted=0")
    return execute(sql).fetchall()


def get_clock_event_by_user(user_id):
    sql = text("SELECT event_type, timestamp FROM clock_events WHERE user_id=:user_id AND is_deleted=0")
    return execute(sql, user_id=user_id).fetchall()


def get_event(event_id):
    sql = text("SELECT event_type, timestamp FROM clock_events WHERE id=:event_id AND is_deleted=0")
    return execute(sql, event_id=event_id).fetchone()


def delete_clock_event(event_id):
    sql = text("UPDATE clock_events SET is_deleted=1 WHERE id=:event_id")
    return execute(sql, event_id=event_id)
