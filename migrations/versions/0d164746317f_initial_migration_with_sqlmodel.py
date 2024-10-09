"""Initial migration with SQLModel

Revision ID: 0d164746317f
Revises: 91b1e5ed5171
Create Date: 2024-10-09 23:55:30.040284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0d164746317f'
down_revision: Union[str, None] = '91b1e5ed5171'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'content',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('notes', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('notes', 'task_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index('ix_notes_id', table_name='notes')
    op.alter_column('projects', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('projects', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('projects', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index('ix_projects_id', table_name='projects')
    op.drop_index('ix_projects_title', table_name='projects')
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('tasks', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('tasks', 'due_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('tasks', 'status',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('tasks', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('tasks', 'project_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index('ix_tasks_id', table_name='tasks')
    op.drop_index('ix_tasks_title', table_name='tasks')
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_name', table_name='users')
    op.drop_index('ix_users_email', table_name='users')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_index('ix_tasks_title', 'tasks', ['title'], unique=False)
    op.create_index('ix_tasks_id', 'tasks', ['id'], unique=False)
    op.alter_column('tasks', 'project_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('tasks', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('tasks', 'status',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('tasks', 'due_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('tasks', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_index('ix_projects_title', 'projects', ['title'], unique=False)
    op.create_index('ix_projects_id', 'projects', ['id'], unique=False)
    op.alter_column('projects', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('projects', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('projects', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_index('ix_notes_id', 'notes', ['id'], unique=False)
    op.alter_column('notes', 'task_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('notes', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('notes', 'content',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
