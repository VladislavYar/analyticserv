"""Init models.

Revision ID: 87e7fe407b55
Revises: 
Create Date: 2025-02-10 08:45:55.468490

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import clickhouse_sqlalchemy.types
from clickhouse_sqlalchemy.types import *
from clickhouse_sqlalchemy import engines


# revision identifiers, used by Alembic.
revision: str = '87e7fe407b55'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('user__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('company__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_territory__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('geo_point__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('worker_report__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('processed_report__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('processed_report_element__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('service', clickhouse_sqlalchemy.types.common.UInt8(), nullable=True),
    sa.Column('event_type', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('happen_at', clickhouse_sqlalchemy.types.common.UInt64(), nullable=False),
    sa.PrimaryKeyConstraint('happen_at'),
    engines.MergeTree(order_by=('happen_at',)),
    )
    op.create_table('level',
    sa.Column('level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level__nesting_level', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('instance_id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('service', clickhouse_sqlalchemy.types.common.UInt8(), nullable=True),
    sa.Column('event_type', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('happen_at', clickhouse_sqlalchemy.types.common.UInt64(), nullable=False),
    sa.PrimaryKeyConstraint('happen_at'),
    engines.MergeTree(order_by=('happen_at',)),
    )
    op.create_table('level_value',
    sa.Column('level_value__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level_value__path', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('instance_id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('service', clickhouse_sqlalchemy.types.common.UInt8(), nullable=True),
    sa.Column('event_type', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('happen_at', clickhouse_sqlalchemy.types.common.UInt64(), nullable=False),
    sa.PrimaryKeyConstraint('happen_at'),
    engines.MergeTree(order_by=('happen_at',)),
    )
    op.create_table('report',
    sa.Column('schedule_time_slot__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_day', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_worker', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_worker_day', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__active_since_local', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_till_local', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_since', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_till', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('company__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('company__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('territory__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('territory__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project_territory__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_territory__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_territory__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project_scheme__report_creation_radius', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__report_creation_duration', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__lat', clickhouse_sqlalchemy.types.common.Nullable(Float32()), nullable=True),
    sa.Column('geo_point__lon', clickhouse_sqlalchemy.types.common.Nullable(Float32()), nullable=True),
    sa.Column('geo_point__city', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__address', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('level_value__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level_value__path', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level__nesting_level', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('user__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('user__first_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('user__middle_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('user__last_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('user__phone', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__company_user__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('worker_report__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('worker_report__status', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__start_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__loaded_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__finish_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__user__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('worker_report__user__first_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__user__middle_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__user__last_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__user__phone', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('processed_report_element__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('processed_report_element__branch_id', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('processed_report_element__status', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('processed_report__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('processed_report__status', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('processed_report__partner_status', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('service', clickhouse_sqlalchemy.types.common.UInt8(), nullable=True),
    sa.Column('event_type', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('happen_at', clickhouse_sqlalchemy.types.common.UInt64(), nullable=False),
    sa.PrimaryKeyConstraint('happen_at'),
    engines.MergeTree(order_by=('happen_at',)),
    )
    op.create_table('report_answer',
    sa.Column('key', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('values', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('values_qty', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_day', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_worker', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_worker_day', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__active_since_local', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_till_local', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_since', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_till', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('company__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('company__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('territory__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('territory__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project_territory__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_territory__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_territory__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project_scheme__report_creation_radius', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__report_creation_duration', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__lat', clickhouse_sqlalchemy.types.common.Nullable(Float32()), nullable=True),
    sa.Column('geo_point__lon', clickhouse_sqlalchemy.types.common.Nullable(Float32()), nullable=True),
    sa.Column('geo_point__city', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__address', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('level_value__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level_value__path', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level__nesting_level', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('user__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('user__first_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('user__middle_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('user__last_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('user__phone', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__company_user__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('worker_report__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('worker_report__status', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__start_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__loaded_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__finish_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('worker_report__user__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('worker_report__user__first_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__user__middle_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__user__last_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('worker_report__user__phone', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('processed_report_element__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('processed_report_element__branch_id', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('processed_report_element__status', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('processed_report__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('processed_report__status', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('processed_report__partner_status', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('service', clickhouse_sqlalchemy.types.common.UInt8(), nullable=True),
    sa.Column('event_type', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('happen_at', clickhouse_sqlalchemy.types.common.UInt64(), nullable=False),
    sa.PrimaryKeyConstraint('happen_at'),
    engines.MergeTree(order_by=('happen_at',)),
    )
    op.create_table('schedule_time_slot',
    sa.Column('schedule_time_slot__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_day', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_worker', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__max_reports_qty_per_worker_day', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('schedule_time_slot__active_since_local', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_till_local', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_since', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__active_till', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('schedule_time_slot__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('company__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('company__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('territory__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('territory__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project_territory__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_territory__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_territory__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('project_scheme__report_creation_radius', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('project_scheme__report_creation_duration', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__reward', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('geo_point__lat', clickhouse_sqlalchemy.types.common.Nullable(Float32()), nullable=True),
    sa.Column('geo_point__lon', clickhouse_sqlalchemy.types.common.Nullable(Float32()), nullable=True),
    sa.Column('geo_point__city', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__address', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('geo_point__created_at', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('level_value__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level_value__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level_value__path', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level__id', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('level__title', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('level__nesting_level', clickhouse_sqlalchemy.types.common.Nullable(UInt64()), nullable=True),
    sa.Column('instance_id', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('instance_name', clickhouse_sqlalchemy.types.common.Nullable(String()), nullable=True),
    sa.Column('service', clickhouse_sqlalchemy.types.common.UInt8(), nullable=True),
    sa.Column('event_type', clickhouse_sqlalchemy.types.common.Nullable(UInt32()), nullable=True),
    sa.Column('happen_at', clickhouse_sqlalchemy.types.common.UInt64(), nullable=False),
    sa.PrimaryKeyConstraint('happen_at'),
    engines.MergeTree(order_by=('happen_at',)),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule_time_slot')
    op.drop_table('report_answer')
    op.drop_table('report')
    op.drop_table('level_value')
    op.drop_table('level')
    op.drop_table('event')
    # ### end Alembic commands ###
