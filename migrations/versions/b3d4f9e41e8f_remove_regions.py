"""Remove regions

Revision ID: b3d4f9e41e8f
Revises: f5d14797658c
Create Date: 2021-06-17 17:11:17.430060

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b3d4f9e41e8f"
down_revision = "f5d14797658c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("course", sa.Column("country_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "course_country_id_fk", "course", "country", ["country_id"], ["id"]
    )

    op.execute(
        """
        UPDATE course
        SET country_id = r.country_id
        FROM course c
        INNER JOIN region r ON c.region_id = r.id
    """
    )

    op.alter_column("course", "country_id", existing_type=sa.INTEGER(), nullable=False)

    op.drop_constraint("course_region_id_fkey", "course", type_="foreignkey")
    op.drop_column("course", "region_id")
    op.drop_table("region")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "course",
        sa.Column("region_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_constraint("course_country_id_fk", "course", type_="foreignkey")
    op.create_foreign_key(
        "course_region_id_fkey", "course", "region", ["region_id"], ["id"]
    )
    op.drop_column("course", "country_id")
    op.create_table(
        "region",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("country_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("name", sa.VARCHAR(length=100), autoincrement=False, nullable=True),
        sa.Column("latitude", sa.REAL(), autoincrement=False, nullable=False),
        sa.Column("longitude", sa.REAL(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["country_id"], ["country.id"], name="region_country_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="region_pkey"),
    )
    # ### end Alembic commands ###
