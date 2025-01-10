from dateutil.parser import parse
from datetime import date

from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Date, DateTime, Boolean

metadata_obj = MetaData()

atom_site_anisotrop = Table("atom_site_anisotrop",
    metadata_obj,
    Column("B[1][1]", Float),
    Column("B[1][1]_esd", Float),
    Column("B[1][2]", Float),
    Column("B[1][2]_esd", Float),
    Column("B[1][3]", Float),
    Column("B[1][3]_esd", Float),
    Column("B[2][2]", Float),
    Column("B[2][2]_esd", Float),
    Column("B[2][3]", Float),
    Column("B[2][3]_esd", Float),
    Column("B[3][3]", Float),
    Column("B[3][3]_esd", Float),
    Column("ratio", Float),
    Column("id", String(20), primary_key=True),
    Column("type_symbol", String(20), nullable=False),
    Column("U[1][1]", Float),
    Column("U[1][1]_esd", Float),
    Column("U[1][2]", Float),
    Column("U[1][2]_esd", Float),
    Column("U[1][3]", Float),
    Column("U[1][3]_esd", Float),
    Column("U[2][2]", Float),
    Column("U[2][2]_esd", Float),
    Column("U[2][3]", Float),
    Column("U[2][3]_esd", Float),
    Column("U[3][3]", Float),
    Column("U[3][3]_esd", Float),
    Column("pdbx_auth_seq_id", String(20)),
    Column("pdbx_auth_alt_id", String(20)),
    Column("pdbx_auth_asym_id", String(20)),
    Column("pdbx_auth_atom_id", String(6)),
    Column("pdbx_auth_comp_id", String(20)),
    Column("pdbx_label_seq_id", Integer),
    Column("pdbx_label_alt_id", String(20)),
    Column("pdbx_label_asym_id", String(20)),
    Column("pdbx_label_atom_id", String(6)),
    Column("pdbx_label_comp_id", String(10)),
    Column("pdbx_PDB_ins_code", String(20)),
    Column("pdbx_PDB_model_num", Integer),
    Column("pdbx_not_in_asym", String(20)),
    Column("pdbx_PDB_residue_no", String(20)),
    Column("pdbx_PDB_residue_name", String(20)),
    Column("pdbx_PDB_strand_id", String(20)),
    Column("pdbx_PDB_atom_name", String(6)),
    Column("pdbx_auth_atom_name", String(6)),
    Column("pdbx_label_ins_code", String(20))
)


atom_sites = Table("atom_sites",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("Cartn_transf_matrix[1][1]", Float),
    Column("Cartn_transf_matrix[1][2]", Float),
    Column("Cartn_transf_matrix[1][3]", Float),
    Column("Cartn_transf_matrix[2][1]", Float),
    Column("Cartn_transf_matrix[2][2]", Float),
    Column("Cartn_transf_matrix[2][3]", Float),
    Column("Cartn_transf_matrix[3][1]", Float),
    Column("Cartn_transf_matrix[3][2]", Float),
    Column("Cartn_transf_matrix[3][3]", Float),
    Column("Cartn_transf_vector[1]", Float),
    Column("Cartn_transf_vector[2]", Float),
    Column("Cartn_transf_vector[3]", Float),
    Column("Cartn_transform_axes", String(255)),
    Column("fract_transf_matrix[1][1]", Float),
    Column("fract_transf_matrix[1][2]", Float),
    Column("fract_transf_matrix[1][3]", Float),
    Column("fract_transf_matrix[2][1]", Float),
    Column("fract_transf_matrix[2][2]", Float),
    Column("fract_transf_matrix[2][3]", Float),
    Column("fract_transf_matrix[3][1]", Float),
    Column("fract_transf_matrix[3][2]", Float),
    Column("fract_transf_matrix[3][3]", Float),
    Column("fract_transf_vector[1]", Float),
    Column("fract_transf_vector[2]", Float),
    Column("fract_transf_vector[3]", Float),
    Column("solution_primary", String(10)),
    Column("solution_secondary", String(10)),
    Column("solution_hydrogens", String(10)),
    Column("special_details", String(255))
)


atom_sites_alt = Table("atom_sites_alt",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True)
)


atom_sites_alt_ens = Table("atom_sites_alt_ens",
    metadata_obj,
    Column("details", String(255))
)


atom_sites_alt_gen = Table("atom_sites_alt_gen",
    metadata_obj,
    Column("alt_id", String(20), primary_key=True),
    Column("ens_id", String(20), primary_key=True)
)


atom_sites_footnote = Table("atom_sites_footnote",
    metadata_obj,
    Column("text", String(255))
)


audit = Table("audit",
    metadata_obj,
    Column("creation_date", DateTime),
    Column("creation_method", String(255)),
    Column("revision_id", String(20), primary_key=True),
    Column("update_record", String(255))
)


audit_author = Table("audit_author",
    metadata_obj,
    Column("address", String(255)),
    Column("name", String(128), nullable=False),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("identifier_ORCID", String(20))
)


audit_conform = Table("audit_conform",
    metadata_obj,
    Column("dict_location", String(255)),
    Column("dict_name", String(255), primary_key=True),
    Column("dict_version", String(255), primary_key=True)
)


audit_contact_author = Table("audit_contact_author",
    metadata_obj,
    Column("address", String(255)),
    Column("email", String(128)),
    Column("fax", String(128)),
    Column("name", String(128), primary_key=True),
    Column("phone", String(128))
)


cell_measurement = Table("cell_measurement",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("pressure", Float),
    Column("pressure_esd", Float),
    Column("radiation", String(128)),
    Column("reflns_used", Integer),
    Column("temp", Float),
    Column("temp_esd", Float),
    Column("theta_max", Float),
    Column("theta_min", Float),
    Column("wavelength", Float)
)


cell_measurement_refln = Table("cell_measurement_refln",
    metadata_obj,
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("theta", Float)
)


chem_comp = Table("chem_comp",
    metadata_obj,
    Column("formula", String(255)),
    Column("formula_weight", Float),
    Column("model_details", String(255)),
    Column("model_erf", String(128)),
    Column("model_source", String(255)),
    Column("mon_nstd_class", String(255)),
    Column("mon_nstd_details", String(255)),
    Column("mon_nstd_flag", String(10), default="no"),
    Column("mon_nstd_parent", String(20)),
    Column("mon_nstd_parent_comp_id", String(50)),
    Column("name", String(255)),
    Column("number_atoms_all", Integer),
    Column("number_atoms_nh", Integer),
    Column("one_letter_code", String(10)),
    Column("three_letter_code", String(6)),
    Column("pdbx_synonyms", String(255)),
    Column("pdbx_modification_details", String(255)),
    Column("pdbx_component_no", Integer),
    Column("pdbx_type", String(50)),
    Column("pdbx_ambiguous_flag", String(20)),
    Column("pdbx_replaced_by", String(10)),
    Column("pdbx_replaces", String(50)),
    Column("pdbx_formal_charge", Integer, default=0),
    Column("pdbx_subcomponent_list", String(255)),
    Column("pdbx_model_coordinates_details", String(255)),
    Column("pdbx_model_coordinates_db_code", String(128)),
    Column("pdbx_ideal_coordinates_details", String(255)),
    Column("pdbx_ideal_coordinates_missing_flag", String(10), default="N"),
    Column("pdbx_model_coordinates_missing_flag", String(10), default="N"),
    Column("pdbx_initial_date", DateTime),
    Column("pdbx_modified_date", DateTime),
    Column("pdbx_release_status", String(128)),
    Column("pdbx_processing_site", String(20)),
    Column("pdbx_number_subcomponents", Integer),
    Column("pdbx_class_1", String(128)),
    Column("pdbx_class_2", String(128)),
    Column("pdbx_comp_type", String(128)),
    Column("pdbx_reserved_name", String(255)),
    Column("pdbx_status", String(20)),
    Column("pdbx_type_modified", Integer),
    Column("pdbx_casnum", String(128)),
    Column("pdbx_smiles", String(255)),
    Column("pdbx_nscnum", String(20)),
    Column("pdbx_pcm", String(20))
)


chem_comp_angle = Table("chem_comp_angle",
    metadata_obj,
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("atom_id_3", String(6), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("value_angle", Float),
    Column("value_angle_esd", Float),
    Column("value_dist", Float),
    Column("value_dist_esd", Float)
)


chem_comp_atom = Table("chem_comp_atom",
    metadata_obj,
    Column("alt_atom_id", String(128)),
    Column("charge", Integer, default=0),
    Column("model_Cartn_x", Float),
    Column("model_Cartn_x_esd", Float),
    Column("model_Cartn_y", Float),
    Column("model_Cartn_y_esd", Float),
    Column("model_Cartn_z", Float),
    Column("model_Cartn_z_esd", Float),
    Column("comp_id", String(10), primary_key=True),
    Column("partial_charge", Float),
    Column("substruct_code", String(10)),
    Column("type_symbol", String(20), nullable=False),
    Column("pdbx_align", Integer),
    Column("pdbx_ordinal", Integer),
    Column("pdbx_component_atom_id", String(6)),
    Column("pdbx_component_comp_id", String(10)),
    Column("pdbx_alt_atom_id", String(6)),
    Column("pdbx_alt_comp_id", String(10)),
    Column("pdbx_model_Cartn_x_ideal", Float),
    Column("pdbx_model_Cartn_y_ideal", Float),
    Column("pdbx_model_Cartn_z_ideal", Float),
    Column("pdbx_stereo_config", String(10)),
    Column("pdbx_aromatic_flag", String(10)),
    Column("pdbx_leaving_atom_flag", String(10)),
    Column("pdbx_residue_numbering", Integer),
    Column("pdbx_polymer_type", String(128)),
    Column("pdbx_ref_id", String(10)),
    Column("pdbx_component_id", Integer),
    Column("pdbx_component_entity_id", Integer),
    Column("pdbx_stnd_atom_id", String(128)),
    Column("pdbx_backbone_atom_flag", String(10)),
    Column("pdbx_n_terminal_atom_flag", String(10)),
    Column("pdbx_c_terminal_atom_flag", String(10))
)


chem_comp_bond = Table("chem_comp_bond",
    metadata_obj,
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("value_order", String(10), default="sing"),
    Column("value_dist", Float),
    Column("value_dist_esd", Float),
    Column("pdbx_ordinal", Integer),
    Column("pdbx_stereo_config", String(10)),
    Column("pdbx_aromatic_flag", String(10))
)


chem_comp_chir = Table("chem_comp_chir",
    metadata_obj,
    Column("atom_id", String(6), nullable=False),
    Column("atom_config", String(10)),
    Column("comp_id", String(10), primary_key=True),
    Column("number_atoms_all", Integer),
    Column("number_atoms_nh", Integer),
    Column("volume_flag", String(10)),
    Column("volume_three", Float),
    Column("volume_three_esd", Float)
)


chem_comp_chir_atom = Table("chem_comp_chir_atom",
    metadata_obj,
    Column("atom_id", String(6), primary_key=True),
    Column("chir_id", String(20), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("dev", Float)
)


chem_comp_link = Table("chem_comp_link",
    metadata_obj,
    Column("link_id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("type_comp_1", String(50), nullable=False),
    Column("type_comp_2", String(50), nullable=False)
)


chem_comp_plane = Table("chem_comp_plane",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("number_atoms_all", Integer),
    Column("number_atoms_nh", Integer)
)


chem_comp_plane_atom = Table("chem_comp_plane_atom",
    metadata_obj,
    Column("atom_id", String(6), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("plane_id", String(20), primary_key=True),
    Column("dist_esd", Float)
)


chem_comp_tor = Table("chem_comp_tor",
    metadata_obj,
    Column("atom_id_1", String(6), nullable=False),
    Column("atom_id_2", String(6), nullable=False),
    Column("atom_id_3", String(6), nullable=False),
    Column("atom_id_4", String(6), nullable=False),
    Column("comp_id", String(10), primary_key=True)
)


chem_comp_tor_value = Table("chem_comp_tor_value",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("tor_id", String(20), primary_key=True),
    Column("angle", Float, nullable=False),
    Column("angle_esd", Float, nullable=False),
    Column("dist", Float),
    Column("dist_esd", Float)
)


chem_link = Table("chem_link",
    metadata_obj,
    Column("details", String(255))
)


chem_link_angle = Table("chem_link_angle",
    metadata_obj,
    Column("atom_1_comp_id", String(10)),
    Column("atom_2_comp_id", String(10)),
    Column("atom_3_comp_id", String(10)),
    Column("atom_id_1", String(20), primary_key=True),
    Column("atom_id_2", String(20), primary_key=True),
    Column("atom_id_3", String(20), primary_key=True),
    Column("link_id", String(20), primary_key=True),
    Column("value_angle", Float),
    Column("value_angle_esd", Float),
    Column("value_dist", Float),
    Column("value_dist_esd", Float)
)


chem_link_bond = Table("chem_link_bond",
    metadata_obj,
    Column("atom_1_comp_id", String(10)),
    Column("atom_2_comp_id", String(10)),
    Column("atom_id_1", String(20), primary_key=True),
    Column("atom_id_2", String(20), primary_key=True),
    Column("link_id", String(20), primary_key=True),
    Column("value_dist", Float),
    Column("value_dist_esd", Float),
    Column("value_order", String(10), default="sing")
)


chem_link_chir = Table("chem_link_chir",
    metadata_obj,
    Column("atom_comp_id", String(10)),
    Column("atom_id", String(20), nullable=False),
    Column("atom_config", String(10)),
    Column("link_id", String(20), primary_key=True),
    Column("number_atoms_all", Integer),
    Column("number_atoms_nh", Integer),
    Column("volume_flag", String(10)),
    Column("volume_three", Float),
    Column("volume_three_esd", Float)
)


chem_link_chir_atom = Table("chem_link_chir_atom",
    metadata_obj,
    Column("atom_comp_id", String(10)),
    Column("atom_id", String(20), primary_key=True),
    Column("chir_id", String(20), primary_key=True),
    Column("dev", Float)
)


chem_link_plane = Table("chem_link_plane",
    metadata_obj,
    Column("link_id", String(20), primary_key=True),
    Column("number_atoms_all", Integer),
    Column("number_atoms_nh", Integer)
)


chem_link_plane_atom = Table("chem_link_plane_atom",
    metadata_obj,
    Column("atom_comp_id", String(10)),
    Column("atom_id", String(20), primary_key=True),
    Column("plane_id", String(20), primary_key=True)
)


chem_link_tor = Table("chem_link_tor",
    metadata_obj,
    Column("atom_1_comp_id", String(10)),
    Column("atom_2_comp_id", String(10)),
    Column("atom_3_comp_id", String(10)),
    Column("atom_4_comp_id", String(10)),
    Column("atom_id_1", String(20), nullable=False),
    Column("atom_id_2", String(20), nullable=False),
    Column("atom_id_3", String(20), nullable=False),
    Column("atom_id_4", String(20), nullable=False),
    Column("link_id", String(20), primary_key=True)
)


chem_link_tor_value = Table("chem_link_tor_value",
    metadata_obj,
    Column("tor_id", String(20), primary_key=True),
    Column("angle", Float, nullable=False),
    Column("angle_esd", Float, nullable=False),
    Column("dist", Float),
    Column("dist_esd", Float)
)


chemical = Table("chemical",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("compound_source", String(255)),
    Column("melting_point", Float),
    Column("name_common", String(255)),
    Column("name_mineral", String(255)),
    Column("name_structure_type", String(255)),
    Column("name_systematic", String(255)),
    Column("absolute_configuration", String(20)),
    Column("melting_point_gt", Float),
    Column("melting_point_lt", Float),
    Column("optical_rotation", String(128)),
    Column("properties_biological", String(255)),
    Column("properties_physical", String(255)),
    Column("temperature_decomposition", Float),
    Column("temperature_decomposition_esd", Float),
    Column("temperature_decomposition_gt", Float),
    Column("temperature_decomposition_lt", Float),
    Column("temperature_sublimation", Float),
    Column("temperature_sublimation_esd", Float),
    Column("temperature_sublimation_gt", Float),
    Column("temperature_sublimation_lt", Float)
)


chemical_conn_atom = Table("chemical_conn_atom",
    metadata_obj,
    Column("charge", Integer, default=0),
    Column("display_x", Float),
    Column("display_y", Float),
    Column("NCA", Integer),
    Column("NH", Integer),
    Column("type_symbol", String(20), nullable=False)
)


chemical_conn_bond = Table("chemical_conn_bond",
    metadata_obj,
    Column("atom_1", Integer, primary_key=True),
    Column("atom_2", Integer, primary_key=True),
    Column("type", String(10), default="sing")
)


chemical_formula = Table("chemical_formula",
    metadata_obj,
    Column("analytical", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("iupac", String(255)),
    Column("moiety", String(255)),
    Column("structural", String(255)),
    Column("sum", String(255)),
    Column("weight", Float),
    Column("weight_meas", Float)
)


citation = Table("citation",
    metadata_obj,
    Column("abstract", String(255)),
    Column("abstract_id_CAS", String(255)),
    Column("book_id_ISBN", String(128)),
    Column("book_publisher", String(255)),
    Column("book_publisher_city", String(255)),
    Column("book_title", String(255)),
    Column("coordinate_linkage", String(10)),
    Column("country", String(128)),
    Column("database_id_Medline", Integer),
    Column("details", String(255)),
    Column("journal_abbrev", String(128)),
    Column("journal_id_ASTM", String(128)),
    Column("journal_id_CSD", String(128)),
    Column("journal_id_ISSN", String(128)),
    Column("journal_full", String(255)),
    Column("journal_issue", String(128)),
    Column("journal_volume", String(128)),
    Column("language", String(128)),
    Column("page_first", String(128)),
    Column("page_last", String(128)),
    Column("title", String(255)),
    Column("year", Integer),
    Column("database_id_CSD", String(20)),
    Column("pdbx_database_id_DOI", String(20)),
    Column("pdbx_database_id_PubMed", Integer),
    Column("pdbx_database_id_patent", String(128)),
    Column("unpublished_flag", String(20))
)


citation_author = Table("citation_author",
    metadata_obj,
    Column("citation_id", String(20), primary_key=True),
    Column("name", String(128), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("identifier_ORCID", String(20))
)


citation_editor = Table("citation_editor",
    metadata_obj,
    Column("citation_id", String(20), primary_key=True),
    Column("name", String(128), primary_key=True),
    Column("ordinal", Integer)
)


computing = Table("computing",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cell_refinement", String(255)),
    Column("data_collection", String(255)),
    Column("data_reduction", String(255)),
    Column("molecular_graphics", String(255)),
    Column("publication_material", String(255)),
    Column("structure_refinement", String(255)),
    Column("structure_solution", String(255)),
    Column("pdbx_structure_refinement_method", String(255)),
    Column("pdbx_data_reduction_ii", String(255)),
    Column("pdbx_data_reduction_ds", String(255))
)


database_2 = Table("database_2",
    metadata_obj,
    Column("database_id", String(10), primary_key=True),
    Column("database_code", String(128), primary_key=True),
    Column("pdbx_database_accession", String(20)),
    Column("pdbx_DOI", String(128))
)


database_PDB_caveat = Table("database_PDB_caveat",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("text", String(255))
)


database_PDB_matrix = Table("database_PDB_matrix",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("origx[1][1]", Float, default=1.0),
    Column("origx[1][2]", Float, default=0.0),
    Column("origx[1][3]", Float, default=0.0),
    Column("origx[2][1]", Float, default=0.0),
    Column("origx[2][2]", Float, default=1.0),
    Column("origx[2][3]", Float, default=0.0),
    Column("origx[3][1]", Float, default=0.0),
    Column("origx[3][2]", Float, default=0.0),
    Column("origx[3][3]", Float, default=1.0),
    Column("origx_vector[1]", Float, default=0.0),
    Column("origx_vector[2]", Float, default=0.0),
    Column("origx_vector[3]", Float, default=0.0),
    Column("scale[1][1]", Float, default=1.0),
    Column("scale[1][2]", Float, default=0.0),
    Column("scale[1][3]", Float, default=0.0),
    Column("scale[2][1]", Float, default=0.0),
    Column("scale[2][2]", Float, default=1.0),
    Column("scale[2][3]", Float, default=0.0),
    Column("scale[3][1]", Float, default=0.0),
    Column("scale[3][2]", Float, default=0.0),
    Column("scale[3][3]", Float, default=1.0),
    Column("scale_vector[1]", Float, default=0.0),
    Column("scale_vector[2]", Float, default=0.0),
    Column("scale_vector[3]", Float, default=0.0)
)


database_PDB_remark = Table("database_PDB_remark",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("text", String(255))
)


database_PDB_rev = Table("database_PDB_rev",
    metadata_obj,
    Column("author_name", String(128)),
    Column("date", DateTime),
    Column("date_original", DateTime),
    Column("mod_type", Integer),
    Column("replaced_by", String(128)),
    Column("replaces", String(128)),
    Column("status", String(50)),
    Column("pdbx_record_revised_1", String(20)),
    Column("pdbx_record_revised_2", String(20)),
    Column("pdbx_record_revised_3", String(20)),
    Column("pdbx_record_revised_4", String(20))
)


database_PDB_rev_record = Table("database_PDB_rev_record",
    metadata_obj,
    Column("details", String(255)),
    Column("rev_num", Integer, primary_key=True),
    Column("type", String(128), primary_key=True)
)


database_PDB_tvect = Table("database_PDB_tvect",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("vector[1]", Float, default=0.0),
    Column("vector[2]", Float, default=0.0),
    Column("vector[3]", Float, default=0.0)
)


diffrn = Table("diffrn",
    metadata_obj,
    Column("ambient_environment", String(128)),
    Column("ambient_temp", Float),
    Column("ambient_temp_details", String(255)),
    Column("ambient_temp_esd", Float),
    Column("crystal_id", String(20), nullable=False),
    Column("crystal_support", String(255)),
    Column("crystal_treatment", String(255)),
    Column("details", String(255)),
    Column("ambient_pressure", Float),
    Column("ambient_pressure_esd", Float),
    Column("ambient_pressure_gt", Float),
    Column("ambient_pressure_lt", Float),
    Column("ambient_temp_gt", Float),
    Column("ambient_temp_lt", Float),
    Column("pdbx_serial_crystal_experiment", String(255))
)


diffrn_attenuator = Table("diffrn_attenuator",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("scale", Float),
    Column("material", String(255))
)


diffrn_detector = Table("diffrn_detector",
    metadata_obj,
    Column("details", String(255)),
    Column("detector", String(255)),
    Column("diffrn_id", String(20), primary_key=True),
    Column("type", String(255)),
    Column("area_resol_mean", Float),
    Column("dtime", Float),
    Column("pdbx_frames_total", Integer),
    Column("pdbx_collection_time_total", Float),
    Column("pdbx_collection_date", DateTime),
    Column("pdbx_frequency", Float),
    Column("number_of_axes", Integer)
)


diffrn_measurement = Table("diffrn_measurement",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("device", String(255)),
    Column("device_details", String(255)),
    Column("device_type", String(255)),
    Column("method", String(255)),
    Column("specimen_support", String(255)),
    Column("pdbx_date", DateTime)
)


diffrn_orient_matrix = Table("diffrn_orient_matrix",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("type", String(255)),
    Column("UB[1][1]", Float),
    Column("UB[1][2]", Float),
    Column("UB[1][3]", Float),
    Column("UB[2][1]", Float),
    Column("UB[2][2]", Float),
    Column("UB[2][3]", Float),
    Column("UB[3][1]", Float),
    Column("UB[3][2]", Float),
    Column("UB[3][3]", Float)
)


diffrn_orient_refln = Table("diffrn_orient_refln",
    metadata_obj,
    Column("angle_chi", Float),
    Column("angle_kappa", Float),
    Column("angle_omega", Float),
    Column("angle_phi", Float),
    Column("angle_psi", Float),
    Column("angle_theta", Float),
    Column("diffrn_id", String(20), primary_key=True),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True)
)


diffrn_radiation = Table("diffrn_radiation",
    metadata_obj,
    Column("collimation", String(255)),
    Column("diffrn_id", String(20), primary_key=True),
    Column("filter_edge", Float),
    Column("inhomogeneity", Float),
    Column("monochromator", String(255)),
    Column("polarisn_norm", Float),
    Column("polarisn_ratio", Float),
    Column("probe", String(128)),
    Column("type", String(128)),
    Column("xray_symbol", String(128)),
    Column("wavelength_id", String(20)),
    Column("pdbx_monochromatic_or_laue_m_l", String(20), default="M"),
    Column("pdbx_wavelength_list", String(128)),
    Column("pdbx_wavelength", String(128)),
    Column("pdbx_diffrn_protocol", String(128), default="SINGLE WAVELENGTH"),
    Column("pdbx_analyzer", String(255)),
    Column("pdbx_scattering_type", String(128))
)


diffrn_radiation_wavelength = Table("diffrn_radiation_wavelength",
    metadata_obj,
    Column("wavelength", Float, nullable=False),
    Column("wt", Float, default=1.0)
)


diffrn_refln = Table("diffrn_refln",
    metadata_obj,
    Column("angle_chi", Float),
    Column("angle_kappa", Float),
    Column("angle_omega", Float),
    Column("angle_phi", Float),
    Column("angle_psi", Float),
    Column("angle_theta", Float),
    Column("attenuator_code", String(20)),
    Column("counts_bg_1", Integer),
    Column("counts_bg_2", Integer),
    Column("counts_net", Integer),
    Column("counts_peak", Integer),
    Column("counts_total", Integer),
    Column("detect_slit_horiz", Float),
    Column("detect_slit_vert", Float),
    Column("diffrn_id", String(20), primary_key=True),
    Column("elapsed_time", Float),
    Column("id", String(20), primary_key=True),
    Column("index_h", Integer, nullable=False),
    Column("index_k", Integer, nullable=False),
    Column("index_l", Integer, nullable=False),
    Column("intensity_net", Float),
    Column("intensity_sigma", Float),
    Column("scale_group_code", String(20)),
    Column("scan_mode", String(10)),
    Column("scan_mode_backgd", String(10)),
    Column("scan_rate", Float),
    Column("scan_time_backgd", Float),
    Column("scan_width", Float),
    Column("sint_over_lambda", Float),
    Column("standard_code", String(20)),
    Column("wavelength", Float),
    Column("wavelength_id", String(20)),
    Column("pdbx_image_id", Integer),
    Column("pdbx_scan_angle", Float),
    Column("class_code", String(20)),
    Column("intensity_u", Float),
    Column("pdbx_detector_x", Float),
    Column("pdbx_detector_y", Float),
    Column("pdbx_rotation_angle", Float),
    Column("pdbx_scale_value", Float),
    Column("frame_id", String(20)),
    Column("pdbx_batch_id", String(20)),
    Column("pdbx_detector_obs_fast", Float),
    Column("pdbx_detector_obs_slow", Float),
    Column("pdbx_detector_calc_fast", Float),
    Column("pdbx_detector_calc_slow", Float),
    Column("pdbx_panel_mapping_id", String(20))
)


diffrn_reflns = Table("diffrn_reflns",
    metadata_obj,
    Column("av_R_equivalents", Float),
    Column("av_sigmaI_over_netI", Float),
    Column("diffrn_id", String(20), primary_key=True),
    Column("limit_h_max", Integer),
    Column("limit_h_min", Integer),
    Column("limit_k_max", Integer),
    Column("limit_k_min", Integer),
    Column("limit_l_max", Integer),
    Column("limit_l_min", Integer),
    Column("number", Integer),
    Column("reduction_process", String(255)),
    Column("theta_max", Float),
    Column("theta_min", Float),
    Column("transf_matrix[1][1]", Float),
    Column("transf_matrix[1][2]", Float),
    Column("transf_matrix[1][3]", Float),
    Column("transf_matrix[2][1]", Float),
    Column("transf_matrix[2][2]", Float),
    Column("transf_matrix[2][3]", Float),
    Column("transf_matrix[3][1]", Float),
    Column("transf_matrix[3][2]", Float),
    Column("transf_matrix[3][3]", Float),
    Column("av_unetI/netI", Float),
    Column("pdbx_d_res_low", Float),
    Column("pdbx_d_res_high", Float),
    Column("pdbx_percent_possible_obs", Float),
    Column("pdbx_Rmerge_I_obs", Float),
    Column("pdbx_Rsym_value", Float),
    Column("pdbx_chi_squared", Float),
    Column("pdbx_redundancy", Float),
    Column("pdbx_rejects", Integer),
    Column("pdbx_observed_criterion", Float),
    Column("pdbx_number_obs", Integer)
)


diffrn_scale_group = Table("diffrn_scale_group",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("I_net", Float)
)


diffrn_source = Table("diffrn_source",
    metadata_obj,
    Column("current", Float),
    Column("details", String(255)),
    Column("diffrn_id", String(20), primary_key=True),
    Column("power", Float),
    Column("size", String(255)),
    Column("source", String(255)),
    Column("target", String(20)),
    Column("type", String(255)),
    Column("voltage", Float),
    Column("take-off_angle", Float),
    Column("pdbx_wavelength_list", String(128)),
    Column("pdbx_wavelength", String(128)),
    Column("pdbx_synchrotron_beamline", String(128)),
    Column("pdbx_synchrotron_site", String(128)),
    Column("pdbx_synchrotron_y_n", String(255)),
    Column("pdbx_source_specific_beamline", String(255))
)


diffrn_standard_refln = Table("diffrn_standard_refln",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("index_h", Integer, nullable=False),
    Column("index_k", Integer, nullable=False),
    Column("index_l", Integer, nullable=False)
)


diffrn_standards = Table("diffrn_standards",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("decay_%", Float),
    Column("interval_count", Integer),
    Column("interval_time", Float),
    Column("number", Integer),
    Column("scale_sigma", Float),
    Column("scale_u", Float)
)


entity = Table("entity",
    metadata_obj,
    Column("details", String(255)),
    Column("formula_weight", Float),
    Column("src_method", String(10)),
    Column("type", String(10)),
    Column("pdbx_description", String(128)),
    Column("pdbx_number_of_molecules", Integer),
    Column("pdbx_parent_entity_id", String(20)),
    Column("pdbx_mutation", String(128)),
    Column("pdbx_fragment", String(128)),
    Column("pdbx_ec", String(10)),
    Column("pdbx_modification", String(128)),
    Column("pdbx_formula_weight_exptl", Float),
    Column("pdbx_formula_weight_exptl_method", String(128)),
    Column("pdbx_target_id", String(20)),
    Column("pdbx_entities_per_biological_unit", Float)
)


entity_keywords = Table("entity_keywords",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("text", String(255)),
    Column("pdbx_mutation", String(128)),
    Column("pdbx_fragment", String(128)),
    Column("pdbx_ec", String(128)),
    Column("pdbx_antibody_isotype", String(255))
)


entity_link = Table("entity_link",
    metadata_obj,
    Column("link_id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("entity_id_1", String(20), nullable=False),
    Column("entity_id_2", String(20), nullable=False),
    Column("entity_seq_num_1", Integer),
    Column("entity_seq_num_2", Integer)
)


entity_name_com = Table("entity_name_com",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("name", String(255)),
    Column("pdbx_provenance", String(128))
)


entity_name_sys = Table("entity_name_sys",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("name", String(255)),
    Column("system", String(255))
)


entity_poly = Table("entity_poly",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("nstd_chirality", String(10)),
    Column("nstd_linkage", String(10)),
    Column("nstd_monomer", String(10)),
    Column("number_of_monomers", Integer),
    Column("type", String(128)),
    Column("type_details", String(255)),
    Column("pdbx_strand_id", String(128)),
    Column("pdbx_seq_one_letter_code", String(255)),
    Column("pdbx_seq_one_letter_code_can", String(255)),
    Column("pdbx_target_identifier", String(128)),
    Column("pdbx_seq_one_letter_code_sample", String(255)),
    Column("pdbx_explicit_linking_flag", String(10), default="N"),
    Column("pdbx_sequence_evidence_code", String(128)),
    Column("pdbx_build_self_reference", String(2)),
    Column("pdbx_N_terminal_seq_one_letter_code", String(255)),
    Column("pdbx_C_terminal_seq_one_letter_code", String(255)),
    Column("pdbx_seq_three_letter_code", String(255)),
    Column("pdbx_seq_db_name", String(128)),
    Column("pdbx_seq_db_id", String(128)),
    Column("pdbx_seq_align_begin", Integer),
    Column("pdbx_seq_align_end", Integer)
)


entity_poly_seq = Table("entity_poly_seq",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("hetero", String(10), default="no"),
    Column("mon_id", String(10), primary_key=True)
)


entry = Table("entry",
    metadata_obj,
    Column("pdbx_DOI", String(20))
)


entry_link = Table("entry_link",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("details", String(255))
)


exptl = Table("exptl",
    metadata_obj,
    Column("absorpt_coefficient_mu", Float),
    Column("absorpt_correction_T_max", Float),
    Column("absorpt_correction_T_min", Float),
    Column("absorpt_correction_type", String(10)),
    Column("absorpt_process_details", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("crystals_number", Integer),
    Column("details", String(255)),
    Column("method", String(128), primary_key=True),
    Column("method_details", String(255))
)


exptl_crystal = Table("exptl_crystal",
    metadata_obj,
    Column("colour", String(128)),
    Column("density_diffrn", Float),
    Column("density_Matthews", Float),
    Column("density_method", String(255)),
    Column("density_percent_sol", Float),
    Column("description", String(255)),
    Column("F_000", Integer),
    Column("preparation", String(255)),
    Column("size_max", Float),
    Column("size_mid", Float),
    Column("size_min", Float),
    Column("size_rad", Float),
    Column("colour_lustre", String(128)),
    Column("colour_modifier", String(128)),
    Column("colour_primary", String(128)),
    Column("density_meas", Float),
    Column("density_meas_esd", Float),
    Column("density_meas_gt", Float),
    Column("density_meas_lt", Float),
    Column("density_meas_temp", Float),
    Column("density_meas_temp_esd", Float),
    Column("density_meas_temp_gt", Float),
    Column("density_meas_temp_lt", Float),
    Column("pdbx_crystal_image_url", String(128)),
    Column("pdbx_crystal_image_format", String(128)),
    Column("pdbx_mosaicity", Float),
    Column("pdbx_mosaicity_esd", Float),
    Column("pdbx_crystal_image", String(20)),
    Column("pdbx_x-ray_image", String(20)),
    Column("pdbx_x-ray_image_type", String(255)),
    Column("pdbx_crystal_diffrn_limit", Float),
    Column("pdbx_crystal_diffrn_lifetime", Float),
    Column("pdbx_crystal_direction_1", Float),
    Column("pdbx_crystal_direction_2", Float),
    Column("pdbx_crystal_direction_3", Float),
    Column("pdbx_mosaic_method", String(10)),
    Column("pdbx_mosaic_block_size", Float),
    Column("pdbx_mosaic_block_size_esd", Float)
)


exptl_crystal_face = Table("exptl_crystal_face",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("diffr_chi", Float),
    Column("diffr_kappa", Float),
    Column("diffr_phi", Float),
    Column("diffr_psi", Float),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("perp_dist", Float)
)


exptl_crystal_grow = Table("exptl_crystal_grow",
    metadata_obj,
    Column("apparatus", String(255)),
    Column("atmosphere", String(255)),
    Column("crystal_id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("method", String(255)),
    Column("method_ref", String(255)),
    Column("pH", Float),
    Column("pressure", Float),
    Column("pressure_esd", Float),
    Column("seeding", String(255)),
    Column("seeding_ref", String(255)),
    Column("temp_details", String(255)),
    Column("temp_esd", Float),
    Column("time", String(255)),
    Column("pdbx_details", String(255)),
    Column("pdbx_pH_range", String(128)),
    Column("temp", Float)
)


exptl_crystal_grow_comp = Table("exptl_crystal_grow_comp",
    metadata_obj,
    Column("conc", String(128)),
    Column("details", String(255)),
    Column("crystal_id", String(20), primary_key=True),
    Column("id", String(128), primary_key=True),
    Column("name", String(128)),
    Column("sol_id", String(128)),
    Column("volume", String(128)),
    Column("pdbx_conc_final", String(128)),
    Column("pdbx_bath", String(128)),
    Column("pdbx_salt", String(128)),
    Column("pdbx_soak_salt", String(128)),
    Column("pdbx_soak_solv", String(128)),
    Column("pdbx_solv", String(128))
)


geom = Table("geom",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("details", String(255))
)


geom_angle = Table("geom_angle",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20)),
    Column("atom_site_label_atom_id_1", String(6)),
    Column("atom_site_label_comp_id_1", String(10)),
    Column("atom_site_label_seq_id_1", Integer),
    Column("atom_site_label_asym_id_1", String(20)),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20)),
    Column("atom_site_label_atom_id_2", String(6)),
    Column("atom_site_label_comp_id_2", String(10)),
    Column("atom_site_label_seq_id_2", Integer),
    Column("atom_site_label_asym_id_2", String(20)),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20)),
    Column("atom_site_label_atom_id_3", String(6)),
    Column("atom_site_label_comp_id_3", String(10)),
    Column("atom_site_label_seq_id_3", Integer),
    Column("atom_site_label_asym_id_3", String(20)),
    Column("atom_site_auth_asym_id_1", String(20)),
    Column("atom_site_auth_atom_id_1", String(6)),
    Column("atom_site_auth_comp_id_1", String(20)),
    Column("atom_site_auth_seq_id_1", String(20)),
    Column("atom_site_auth_atom_id_2", String(6)),
    Column("atom_site_auth_asym_id_2", String(20)),
    Column("atom_site_auth_comp_id_2", String(20)),
    Column("atom_site_auth_seq_id_2", String(20)),
    Column("atom_site_auth_atom_id_3", String(6)),
    Column("atom_site_auth_asym_id_3", String(20)),
    Column("atom_site_auth_comp_id_3", String(20)),
    Column("atom_site_auth_seq_id_3", String(20)),
    Column("publ_flag", String(10)),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("value", Float),
    Column("value_esd", Float),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20)),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20)),
    Column("pdbx_atom_site_PDB_ins_code_3", String(20)),
    Column("pdbx_PDB_model_num", Integer)
)


geom_bond = Table("geom_bond",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20)),
    Column("atom_site_label_atom_id_1", String(6)),
    Column("atom_site_label_comp_id_1", String(10)),
    Column("atom_site_label_seq_id_1", Integer),
    Column("atom_site_label_asym_id_1", String(20)),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20)),
    Column("atom_site_label_atom_id_2", String(6)),
    Column("atom_site_label_comp_id_2", String(10)),
    Column("atom_site_label_seq_id_2", Integer),
    Column("atom_site_label_asym_id_2", String(20)),
    Column("atom_site_auth_atom_id_1", String(6)),
    Column("atom_site_auth_asym_id_1", String(20)),
    Column("atom_site_auth_comp_id_1", String(20)),
    Column("atom_site_auth_seq_id_1", String(20)),
    Column("atom_site_auth_atom_id_2", String(6)),
    Column("atom_site_auth_asym_id_2", String(20)),
    Column("atom_site_auth_comp_id_2", String(20)),
    Column("atom_site_auth_seq_id_2", String(20)),
    Column("dist", Float),
    Column("dist_esd", Float),
    Column("publ_flag", String(10)),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("valence", Integer),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20)),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20)),
    Column("pdbx_PDB_model_num", Integer)
)


geom_contact = Table("geom_contact",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20)),
    Column("atom_site_label_atom_id_1", String(6)),
    Column("atom_site_label_comp_id_1", String(10)),
    Column("atom_site_label_seq_id_1", Integer),
    Column("atom_site_label_asym_id_1", String(20)),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20)),
    Column("atom_site_label_atom_id_2", String(6)),
    Column("atom_site_label_comp_id_2", String(10)),
    Column("atom_site_label_seq_id_2", Integer),
    Column("atom_site_label_asym_id_2", String(20)),
    Column("atom_site_auth_atom_id_1", String(6)),
    Column("atom_site_auth_asym_id_1", String(20)),
    Column("atom_site_auth_comp_id_1", String(20)),
    Column("atom_site_auth_seq_id_1", String(20)),
    Column("atom_site_auth_atom_id_2", String(6)),
    Column("atom_site_auth_asym_id_2", String(20)),
    Column("atom_site_auth_comp_id_2", String(20)),
    Column("atom_site_auth_seq_id_2", String(20)),
    Column("dist", Float),
    Column("dist_esd", Float),
    Column("publ_flag", String(10)),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20)),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20)),
    Column("pdbx_PDB_model_num", Integer)
)


geom_hbond = Table("geom_hbond",
    metadata_obj,
    Column("angle_DHA", Float),
    Column("angle_DHA_esd", Float),
    Column("atom_site_id_A", String(20), primary_key=True),
    Column("atom_site_label_alt_id_A", String(20)),
    Column("atom_site_label_asym_id_A", String(20)),
    Column("atom_site_label_atom_id_A", String(6)),
    Column("atom_site_label_comp_id_A", String(10)),
    Column("atom_site_label_seq_id_A", Integer),
    Column("atom_site_id_D", String(20), primary_key=True),
    Column("atom_site_label_alt_id_D", String(20)),
    Column("atom_site_label_asym_id_D", String(20)),
    Column("atom_site_label_atom_id_D", String(6)),
    Column("atom_site_label_comp_id_D", String(10)),
    Column("atom_site_label_seq_id_D", Integer),
    Column("atom_site_id_H", String(20), primary_key=True),
    Column("atom_site_label_alt_id_H", String(20)),
    Column("atom_site_label_asym_id_H", String(20)),
    Column("atom_site_label_atom_id_H", String(6)),
    Column("atom_site_label_comp_id_H", String(10)),
    Column("atom_site_label_seq_id_H", Integer),
    Column("atom_site_auth_asym_id_A", String(20)),
    Column("atom_site_auth_atom_id_A", String(6)),
    Column("atom_site_auth_comp_id_A", String(20)),
    Column("atom_site_auth_seq_id_A", String(20)),
    Column("atom_site_auth_asym_id_D", String(20)),
    Column("atom_site_auth_atom_id_D", String(6)),
    Column("atom_site_auth_comp_id_D", String(20)),
    Column("atom_site_auth_seq_id_D", String(20)),
    Column("atom_site_auth_asym_id_H", String(20)),
    Column("atom_site_auth_atom_id_H", String(6)),
    Column("atom_site_auth_comp_id_H", String(20)),
    Column("atom_site_auth_seq_id_H", String(20)),
    Column("dist_DA", Float),
    Column("dist_DA_esd", Float),
    Column("dist_DH", Float),
    Column("dist_DH_esd", Float),
    Column("dist_HA", Float),
    Column("dist_HA_esd", Float),
    Column("publ_flag", String(10)),
    Column("site_symmetry_A", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_D", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_H", String(10), primary_key=True, default="1_555")
)


geom_torsion = Table("geom_torsion",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20)),
    Column("atom_site_label_atom_id_1", String(6)),
    Column("atom_site_label_comp_id_1", String(10)),
    Column("atom_site_label_seq_id_1", Integer),
    Column("atom_site_label_asym_id_1", String(20)),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20)),
    Column("atom_site_label_atom_id_2", String(6)),
    Column("atom_site_label_comp_id_2", String(10)),
    Column("atom_site_label_seq_id_2", Integer),
    Column("atom_site_label_asym_id_2", String(20)),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20)),
    Column("atom_site_label_atom_id_3", String(6)),
    Column("atom_site_label_comp_id_3", String(10)),
    Column("atom_site_label_seq_id_3", Integer),
    Column("atom_site_label_asym_id_3", String(20)),
    Column("atom_site_id_4", String(20), primary_key=True),
    Column("atom_site_label_alt_id_4", String(20)),
    Column("atom_site_label_atom_id_4", String(6)),
    Column("atom_site_label_comp_id_4", String(10)),
    Column("atom_site_label_seq_id_4", Integer),
    Column("atom_site_label_asym_id_4", String(20)),
    Column("atom_site_auth_atom_id_1", String(6)),
    Column("atom_site_auth_asym_id_1", String(20)),
    Column("atom_site_auth_comp_id_1", String(20)),
    Column("atom_site_auth_seq_id_1", String(20)),
    Column("atom_site_auth_atom_id_2", String(6)),
    Column("atom_site_auth_asym_id_2", String(20)),
    Column("atom_site_auth_comp_id_2", String(20)),
    Column("atom_site_auth_seq_id_2", String(20)),
    Column("atom_site_auth_atom_id_3", String(6)),
    Column("atom_site_auth_asym_id_3", String(20)),
    Column("atom_site_auth_comp_id_3", String(20)),
    Column("atom_site_auth_seq_id_3", String(20)),
    Column("atom_site_auth_atom_id_4", String(6)),
    Column("atom_site_auth_asym_id_4", String(20)),
    Column("atom_site_auth_comp_id_4", String(20)),
    Column("atom_site_auth_seq_id_4", String(20)),
    Column("publ_flag", String(10)),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_4", String(10), primary_key=True, default="1_555"),
    Column("value", Float),
    Column("value_esd", Float),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20)),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20)),
    Column("pdbx_atom_site_PDB_ins_code_3", String(20)),
    Column("pdbx_atom_site_PDB_ins_code_4", String(20)),
    Column("pdbx_PDB_model_num", Integer)
)


journal = Table("journal",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("coden_ASTM", String(128)),
    Column("coden_Cambridge", String(128)),
    Column("coeditor_address", String(255)),
    Column("coeditor_code", String(128)),
    Column("coeditor_email", String(128)),
    Column("coeditor_fax", String(128)),
    Column("coeditor_name", String(128)),
    Column("coeditor_notes", String(255)),
    Column("coeditor_phone", String(128)),
    Column("data_validation_number", String(20)),
    Column("date_accepted", DateTime),
    Column("date_from_coeditor", DateTime),
    Column("date_to_coeditor", DateTime),
    Column("date_printers_final", DateTime),
    Column("date_printers_first", DateTime),
    Column("date_proofs_in", DateTime),
    Column("date_proofs_out", DateTime),
    Column("date_recd_copyright", DateTime),
    Column("date_recd_electronic", DateTime),
    Column("date_recd_hard_copy", DateTime),
    Column("issue", String(128)),
    Column("language", String(128)),
    Column("name_full", String(128)),
    Column("page_first", String(128)),
    Column("page_last", String(128)),
    Column("paper_category", String(128)),
    Column("suppl_publ_number", String(128)),
    Column("suppl_publ_pages", String(128)),
    Column("techeditor_address", String(255)),
    Column("techeditor_code", String(128)),
    Column("techeditor_email", String(128)),
    Column("techeditor_fax", String(128)),
    Column("techeditor_name", String(128)),
    Column("techeditor_notes", String(255)),
    Column("techeditor_phone", String(128)),
    Column("volume", String(128)),
    Column("year", String(128))
)


journal_index = Table("journal_index",
    metadata_obj,
    Column("subterm", String(128)),
    Column("term", String(128), primary_key=True),
    Column("type", String(128), primary_key=True)
)


phasing = Table("phasing",
    metadata_obj,
    Column("method", String(10), primary_key=True)
)


phasing_averaging = Table("phasing_averaging",
    metadata_obj,
    Column("details", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255))
)


phasing_isomorphous = Table("phasing_isomorphous",
    metadata_obj,
    Column("details", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255)),
    Column("parent", String(255))
)


phasing_MAD = Table("phasing_MAD",
    metadata_obj,
    Column("details", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255)),
    Column("pdbx_d_res_low", Float),
    Column("pdbx_d_res_high", Float),
    Column("pdbx_reflns_acentric", Integer),
    Column("pdbx_reflns_centric", Integer),
    Column("pdbx_reflns", Integer),
    Column("pdbx_fom_acentric", Float),
    Column("pdbx_fom_centric", Float),
    Column("pdbx_fom", Float),
    Column("pdbx_R_cullis_centric", Float),
    Column("pdbx_R_cullis_acentric", Float),
    Column("pdbx_R_cullis", Float),
    Column("pdbx_R_kraut_centric", Float),
    Column("pdbx_R_kraut_acentric", Float),
    Column("pdbx_R_kraut", Float),
    Column("pdbx_loc_centric", Float),
    Column("pdbx_loc_acentric", Float),
    Column("pdbx_loc", Float),
    Column("pdbx_power_centric", Float),
    Column("pdbx_power_acentric", Float),
    Column("pdbx_power", Float),
    Column("pdbx_number_data_sets", Integer),
    Column("pdbx_anom_scat_method", String(255))
)


phasing_MAD_clust = Table("phasing_MAD_clust",
    metadata_obj,
    Column("expt_id", String(128), primary_key=True),
    Column("number_set", Integer)
)


phasing_MAD_expt = Table("phasing_MAD_expt",
    metadata_obj,
    Column("delta_delta_phi", Float),
    Column("delta_phi", Float),
    Column("delta_phi_sigma", Float),
    Column("mean_fom", Float),
    Column("number_clust", Integer),
    Column("R_normal_all", Float),
    Column("R_normal_anom_scat", Float)
)


phasing_MAD_ratio = Table("phasing_MAD_ratio",
    metadata_obj,
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("expt_id", String(128), primary_key=True),
    Column("clust_id", String(128), primary_key=True),
    Column("ratio_one_wl", Float),
    Column("ratio_one_wl_centric", Float),
    Column("ratio_two_wl", Float),
    Column("wavelength_1", Float, primary_key=True),
    Column("wavelength_2", Float, primary_key=True)
)


phasing_MAD_set = Table("phasing_MAD_set",
    metadata_obj,
    Column("clust_id", String(128), primary_key=True),
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("expt_id", String(128), primary_key=True),
    Column("f_double_prime", Float),
    Column("f_prime", Float),
    Column("set_id", String(128), primary_key=True),
    Column("wavelength_details", String(255)),
    Column("pdbx_atom_type", String(20)),
    Column("pdbx_f_prime_refined", Float),
    Column("pdbx_f_double_prime_refined", Float)
)


phasing_MIR = Table("phasing_MIR",
    metadata_obj,
    Column("details", String(255)),
    Column("d_res_high", Float, nullable=False),
    Column("d_res_low", Float, nullable=False),
    Column("entry_id", String(20), primary_key=True),
    Column("FOM", Float),
    Column("FOM_acentric", Float),
    Column("FOM_centric", Float),
    Column("method", String(255)),
    Column("reflns", Integer),
    Column("reflns_acentric", Integer),
    Column("reflns_centric", Integer),
    Column("reflns_criterion", String(255)),
    Column("pdbx_number_derivatives", Integer)
)


phasing_MIR_der = Table("phasing_MIR_der",
    metadata_obj,
    Column("d_res_high", Float, nullable=False),
    Column("d_res_low", Float, nullable=False),
    Column("der_set_id", String(128), nullable=False),
    Column("details", String(255)),
    Column("native_set_id", String(128), nullable=False),
    Column("number_of_sites", Integer),
    Column("power_acentric", Float),
    Column("power_centric", Float),
    Column("R_cullis_acentric", Float),
    Column("R_cullis_anomalous", Float),
    Column("R_cullis_centric", Float),
    Column("reflns_acentric", Integer),
    Column("reflns_anomalous", Integer),
    Column("reflns_centric", Integer),
    Column("reflns_criteria", String(255)),
    Column("pdbx_R_kraut_centric", Float),
    Column("pdbx_R_kraut_acentric", Float),
    Column("pdbx_R_kraut", Float),
    Column("pdbx_loc_centric", Float),
    Column("pdbx_loc_acentric", Float),
    Column("pdbx_loc", Float),
    Column("pdbx_fom_centric", Float),
    Column("pdbx_fom_acentric", Float),
    Column("pdbx_fom", Float),
    Column("pdbx_power", Float),
    Column("pdbx_R_cullis", Float),
    Column("pdbx_reflns", Integer)
)


phasing_MIR_der_refln = Table("phasing_MIR_der_refln",
    metadata_obj,
    Column("der_id", String(128), primary_key=True),
    Column("F_calc", Float),
    Column("F_calc_au", Float),
    Column("F_meas", Float),
    Column("F_meas_au", Float),
    Column("F_meas_sigma", Float),
    Column("F_meas_sigma_au", Float),
    Column("HL_A_iso", Float),
    Column("HL_B_iso", Float),
    Column("HL_C_iso", Float),
    Column("HL_D_iso", Float),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("phase_calc", Float),
    Column("set_id", String(128), primary_key=True)
)


phasing_MIR_der_shell = Table("phasing_MIR_der_shell",
    metadata_obj,
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("der_id", String(128), primary_key=True),
    Column("fom", Float),
    Column("ha_ampl", Float),
    Column("loc", Float),
    Column("phase", Float),
    Column("power", Float),
    Column("R_cullis", Float),
    Column("R_kraut", Float),
    Column("reflns", Integer),
    Column("pdbx_R_cullis_centric", Float),
    Column("pdbx_R_cullis_acentric", Float),
    Column("pdbx_R_kraut_centric", Float),
    Column("pdbx_R_kraut_acentric", Float),
    Column("pdbx_loc_centric", Float),
    Column("pdbx_loc_acentric", Float),
    Column("pdbx_power_centric", Float),
    Column("pdbx_power_acentric", Float),
    Column("pdbx_fom_centric", Float),
    Column("pdbx_fom_acentric", Float),
    Column("pdbx_reflns_centric", Float),
    Column("pdbx_reflns_acentric", Integer)
)


phasing_MIR_der_site = Table("phasing_MIR_der_site",
    metadata_obj,
    Column("atom_type_symbol", String(20), nullable=False),
    Column("B_iso", Float),
    Column("B_iso_esd", Float),
    Column("Cartn_x", Float),
    Column("Cartn_x_esd", Float),
    Column("Cartn_y", Float),
    Column("Cartn_y_esd", Float),
    Column("Cartn_z", Float),
    Column("Cartn_z_esd", Float),
    Column("der_id", String(128), primary_key=True),
    Column("details", String(255)),
    Column("fract_x", Float),
    Column("fract_x_esd", Float),
    Column("fract_y", Float),
    Column("fract_y_esd", Float),
    Column("fract_z", Float),
    Column("fract_z_esd", Float),
    Column("id", String(20), primary_key=True),
    Column("occupancy", Float, default=1.0),
    Column("occupancy_anom", Float),
    Column("occupancy_anom_su", Float),
    Column("occupancy_iso", Float),
    Column("occupancy_iso_su", Float)
)


phasing_MIR_shell = Table("phasing_MIR_shell",
    metadata_obj,
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("FOM", Float),
    Column("FOM_acentric", Float),
    Column("FOM_centric", Float),
    Column("loc", Float),
    Column("mean_phase", Float),
    Column("power", Float),
    Column("R_cullis", Float),
    Column("R_kraut", Float),
    Column("reflns", Integer),
    Column("reflns_acentric", Integer),
    Column("reflns_anomalous", Integer),
    Column("reflns_centric", Integer),
    Column("pdbx_loc_centric", Float),
    Column("pdbx_loc_acentric", Float),
    Column("pdbx_power_centric", Float),
    Column("pdbx_power_acentric", Float),
    Column("pdbx_R_kraut_centric", Float),
    Column("pdbx_R_kraut_acentric", Float),
    Column("pdbx_R_cullis_centric", Float),
    Column("pdbx_R_cullis_acentric", Float)
)


phasing_set = Table("phasing_set",
    metadata_obj,
    Column("cell_angle_alpha", Float, default=90.0),
    Column("cell_angle_beta", Float, default=90.0),
    Column("cell_angle_gamma", Float, default=90.0),
    Column("cell_length_a", Float),
    Column("cell_length_b", Float),
    Column("cell_length_c", Float),
    Column("detector_specific", String(255)),
    Column("detector_type", String(255)),
    Column("radiation_source_specific", String(255)),
    Column("radiation_wavelength", Float),
    Column("temp", Float),
    Column("pdbx_temp_details", String(255)),
    Column("pdbx_d_res_high", Float, nullable=False),
    Column("pdbx_d_res_low", Float, nullable=False)
)


phasing_set_refln = Table("phasing_set_refln",
    metadata_obj,
    Column("set_id", String(128), primary_key=True),
    Column("F_meas", Float),
    Column("F_meas_au", Float),
    Column("F_meas_sigma", Float),
    Column("F_meas_sigma_au", Float),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True)
)


publ = Table("publ",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("contact_author", String(255)),
    Column("contact_author_address", String(255)),
    Column("contact_author_email", String(128)),
    Column("contact_author_fax", String(128)),
    Column("contact_author_name", String(255)),
    Column("contact_author_phone", String(128)),
    Column("contact_letter", String(255)),
    Column("manuscript_creation", String(255)),
    Column("manuscript_processed", String(255)),
    Column("manuscript_text", String(255)),
    Column("requested_category", String(128), default="FA"),
    Column("requested_coeditor_name", String(128)),
    Column("requested_journal", String(128)),
    Column("section_abstract", String(255)),
    Column("section_acknowledgements", String(255)),
    Column("section_comment", String(255)),
    Column("section_discussion", String(255)),
    Column("section_experimental", String(255)),
    Column("section_exptl_prep", String(255)),
    Column("section_exptl_refinement", String(255)),
    Column("section_exptl_solution", String(255)),
    Column("section_figure_captions", String(255)),
    Column("section_introduction", String(255)),
    Column("section_references", String(255)),
    Column("section_synopsis", String(255)),
    Column("section_table_legends", String(255)),
    Column("section_title", String(255)),
    Column("section_title_footnote", String(255))
)


publ_author = Table("publ_author",
    metadata_obj,
    Column("address", String(255)),
    Column("email", String(255)),
    Column("footnote", String(128)),
    Column("name", String(128), primary_key=True),
    Column("id_iucr", String(20))
)


publ_body = Table("publ_body",
    metadata_obj,
    Column("contents", String(255)),
    Column("element", String(20), primary_key=True),
    Column("format", String(20)),
    Column("label", String(20), primary_key=True),
    Column("title", String(255))
)


publ_manuscript_incl = Table("publ_manuscript_incl",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("extra_defn", String(128)),
    Column("extra_info", String(255)),
    Column("extra_item", String(128))
)


refine = Table("refine",
    metadata_obj,
    Column("aniso_B[1][1]", Float),
    Column("aniso_B[1][2]", Float),
    Column("aniso_B[1][3]", Float),
    Column("aniso_B[2][2]", Float),
    Column("aniso_B[2][3]", Float),
    Column("aniso_B[3][3]", Float),
    Column("B_iso_max", Float),
    Column("B_iso_mean", Float),
    Column("B_iso_min", Float),
    Column("correlation_coeff_Fo_to_Fc", Float),
    Column("correlation_coeff_Fo_to_Fc_free", Float),
    Column("details", String(255)),
    Column("diff_density_max", Float),
    Column("diff_density_max_esd", Float),
    Column("diff_density_min", Float),
    Column("diff_density_min_esd", Float),
    Column("diff_density_rms", Float),
    Column("diff_density_rms_esd", Float),
    Column("entry_id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("ls_abs_structure_details", String(255)),
    Column("ls_abs_structure_Flack", Float),
    Column("ls_abs_structure_Flack_esd", Float),
    Column("ls_abs_structure_Rogers", Float),
    Column("ls_abs_structure_Rogers_esd", Float),
    Column("ls_d_res_high", Float, nullable=False),
    Column("ls_d_res_low", Float),
    Column("ls_extinction_coef", Float),
    Column("ls_extinction_coef_esd", Float),
    Column("ls_extinction_expression", String(255)),
    Column("ls_extinction_method", String(255)),
    Column("ls_goodness_of_fit_all", Float),
    Column("ls_goodness_of_fit_all_esd", Float),
    Column("ls_goodness_of_fit_obs", Float),
    Column("ls_goodness_of_fit_obs_esd", Float),
    Column("ls_hydrogen_treatment", String(10)),
    Column("ls_matrix_type", String(10)),
    Column("ls_number_constraints", Integer),
    Column("ls_number_parameters", Integer),
    Column("ls_number_reflns_all", Integer),
    Column("ls_number_reflns_obs", Integer),
    Column("ls_number_reflns_R_free", Integer),
    Column("ls_number_reflns_R_work", Integer),
    Column("ls_number_restraints", Integer),
    Column("ls_percent_reflns_obs", Float),
    Column("ls_percent_reflns_R_free", Float),
    Column("ls_R_factor_all", Float),
    Column("ls_R_factor_obs", Float),
    Column("ls_R_factor_R_free", Float),
    Column("ls_R_factor_R_free_error", Float),
    Column("ls_R_factor_R_free_error_details", String(255)),
    Column("ls_R_factor_R_work", Float),
    Column("ls_R_Fsqd_factor_obs", Float),
    Column("ls_R_I_factor_obs", Float),
    Column("ls_redundancy_reflns_all", Float),
    Column("ls_redundancy_reflns_obs", Float),
    Column("ls_restrained_S_all", Float),
    Column("ls_restrained_S_obs", Float),
    Column("ls_shift_over_esd_max", Float),
    Column("ls_shift_over_esd_mean", Float),
    Column("ls_structure_factor_coef", String(10)),
    Column("ls_weighting_details", String(255)),
    Column("ls_weighting_scheme", String(10)),
    Column("ls_wR_factor_all", Float),
    Column("ls_wR_factor_obs", Float),
    Column("ls_wR_factor_R_free", Float),
    Column("ls_wR_factor_R_work", Float),
    Column("occupancy_max", Float),
    Column("occupancy_min", Float),
    Column("solvent_model_details", String(255)),
    Column("solvent_model_param_bsol", Float),
    Column("solvent_model_param_ksol", Float),
    Column("pdbx_R_complete", Float),
    Column("ls_R_factor_gt", Float),
    Column("ls_goodness_of_fit_gt", Float),
    Column("ls_goodness_of_fit_ref", Float),
    Column("ls_shift_over_su_max", Float),
    Column("ls_shift_over_su_max_lt", Float),
    Column("ls_shift_over_su_mean", Float),
    Column("ls_shift_over_su_mean_lt", Float),
    Column("pdbx_ls_sigma_I", Float),
    Column("pdbx_ls_sigma_F", Float),
    Column("pdbx_ls_sigma_Fsqd", Float),
    Column("pdbx_data_cutoff_high_absF", Float),
    Column("pdbx_data_cutoff_high_rms_absF", Float),
    Column("pdbx_data_cutoff_low_absF", Float),
    Column("pdbx_isotropic_thermal_model", String(255)),
    Column("pdbx_ls_cross_valid_method", String(255)),
    Column("pdbx_method_to_determine_struct", String(255)),
    Column("pdbx_starting_model", String(255)),
    Column("pdbx_stereochemistry_target_values", String(255)),
    Column("pdbx_R_Free_selection_details", String(255)),
    Column("pdbx_stereochem_target_val_spec_case", String(255)),
    Column("pdbx_overall_ESU_R", Float),
    Column("pdbx_overall_ESU_R_Free", Float),
    Column("pdbx_solvent_vdw_probe_radii", Float),
    Column("pdbx_solvent_ion_probe_radii", Float),
    Column("pdbx_solvent_shrinkage_radii", Float),
    Column("pdbx_real_space_R", Float),
    Column("pdbx_density_correlation", Float),
    Column("pdbx_pd_number_of_powder_patterns", Integer),
    Column("pdbx_pd_number_of_points", Integer),
    Column("pdbx_pd_meas_number_of_points", Integer),
    Column("pdbx_pd_proc_ls_prof_R_factor", Float),
    Column("pdbx_pd_proc_ls_prof_wR_factor", Float),
    Column("pdbx_pd_Marquardt_correlation_coeff", Float),
    Column("pdbx_pd_Fsqrd_R_factor", Float),
    Column("pdbx_pd_ls_matrix_band_width", Integer),
    Column("pdbx_overall_phase_error", Float),
    Column("pdbx_overall_SU_R_free_Cruickshank_DPI", Float),
    Column("pdbx_overall_SU_R_free_Blow_DPI", Float),
    Column("pdbx_overall_SU_R_Blow_DPI", Float),
    Column("pdbx_TLS_residual_ADP_flag", String(128)),
    Column("pdbx_diffrn_id", String(20)),
    Column("overall_SU_B", Float),
    Column("overall_SU_ML", Float),
    Column("overall_SU_R_Cruickshank_DPI", Float),
    Column("overall_SU_R_free", Float),
    Column("overall_FOM_free_R_set", Float),
    Column("overall_FOM_work_R_set", Float),
    Column("pdbx_average_fsc_overall", Float),
    Column("pdbx_average_fsc_work", Float),
    Column("pdbx_average_fsc_free", Float),
    Column("pdbx_overall_ESU_B", Float),
    Column("pdbx_overall_ESU_ML", Float)
)


refine_analyze = Table("refine_analyze",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("Luzzati_coordinate_error_free", Float),
    Column("Luzzati_coordinate_error_obs", Float),
    Column("Luzzati_d_res_low_free", Float),
    Column("Luzzati_d_res_low_obs", Float),
    Column("Luzzati_sigma_a_free", Float),
    Column("Luzzati_sigma_a_free_details", String(255)),
    Column("Luzzati_sigma_a_obs", Float),
    Column("Luzzati_sigma_a_obs_details", String(255)),
    Column("number_disordered_residues", Float),
    Column("occupancy_sum_hydrogen", Float),
    Column("occupancy_sum_non_hydrogen", Float),
    Column("RG_d_res_high", Float),
    Column("RG_d_res_low", Float),
    Column("RG_free", Float),
    Column("RG_work", Float),
    Column("RG_free_work_ratio", Float),
    Column("pdbx_Luzzati_d_res_high_obs", Float)
)


refine_B_iso = Table("refine_B_iso",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("class", String(255), primary_key=True),
    Column("details", String(255)),
    Column("treatment", String(10)),
    Column("value", Float),
    Column("pdbx_residue_name", String(20)),
    Column("pdbx_strand", String(20)),
    Column("pdbx_residue_num", String(20))
)


refine_funct_minimized = Table("refine_funct_minimized",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("number_terms", Integer),
    Column("residual", Float),
    Column("type", String(128), primary_key=True),
    Column("weight", Float)
)


refine_hist = Table("refine_hist",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("cycle_id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("d_res_high", Float, nullable=False),
    Column("d_res_low", Float, nullable=False),
    Column("number_atoms_solvent", Integer),
    Column("number_atoms_total", Integer),
    Column("number_reflns_all", Integer),
    Column("number_reflns_obs", Integer),
    Column("number_reflns_R_free", Integer),
    Column("number_reflns_R_work", Integer),
    Column("R_factor_all", Float),
    Column("R_factor_obs", Float),
    Column("R_factor_R_free", Float),
    Column("R_factor_R_work", Float),
    Column("pdbx_number_residues_total", Integer),
    Column("pdbx_B_iso_mean_ligand", Float),
    Column("pdbx_B_iso_mean_solvent", Float),
    Column("pdbx_number_atoms_protein", Integer),
    Column("pdbx_number_atoms_nucleic_acid", Integer),
    Column("pdbx_number_atoms_ligand", Integer),
    Column("pdbx_number_atoms_lipid", Integer),
    Column("pdbx_number_atoms_carb", Integer),
    Column("pdbx_pseudo_atom_details", String(255)),
    Column("pdbx_number_atoms_solvent", Integer),
    Column("pdbx_number_atoms_total", Integer)
)


refine_ls_restr = Table("refine_ls_restr",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("criterion", String(255)),
    Column("dev_ideal", Float),
    Column("dev_ideal_target", Float),
    Column("number", Integer),
    Column("rejects", Integer),
    Column("weight", Float),
    Column("pdbx_restraint_function", String(255))
)


refine_ls_restr_ncs = Table("refine_ls_restr_ncs",
    metadata_obj,
    Column("pdbx_refine_id", String(128), nullable=False),
    Column("dom_id", String(20), nullable=False),
    Column("ncs_model_details", String(255)),
    Column("rms_dev_B_iso", Float),
    Column("rms_dev_position", Float),
    Column("weight_B_iso", Float),
    Column("weight_position", Float),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("pdbx_type", String(255), nullable=False),
    Column("pdbx_asym_id", String(20)),
    Column("pdbx_auth_asym_id", String(20), nullable=False),
    Column("pdbx_number", Integer),
    Column("pdbx_rms", Float),
    Column("pdbx_weight", Float),
    Column("pdbx_ens_id", String(20), nullable=False)
)


refine_ls_restr_type = Table("refine_ls_restr_type",
    metadata_obj,
    Column("distance_cutoff_high", Float),
    Column("distance_cutoff_low", Float),
    Column("type", String(128), primary_key=True)
)


refine_ls_shell = Table("refine_ls_shell",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float),
    Column("number_reflns_all", Integer),
    Column("number_reflns_obs", Integer),
    Column("number_reflns_R_free", Integer),
    Column("number_reflns_R_work", Integer),
    Column("percent_reflns_obs", Float),
    Column("percent_reflns_R_free", Float),
    Column("R_factor_all", Float),
    Column("R_factor_obs", Float),
    Column("R_factor_R_free_error", Float),
    Column("R_factor_R_work", Float),
    Column("redundancy_reflns_all", Float),
    Column("redundancy_reflns_obs", Float),
    Column("wR_factor_all", Float),
    Column("wR_factor_obs", Float),
    Column("wR_factor_R_free", Float),
    Column("wR_factor_R_work", Float),
    Column("pdbx_R_complete", Float),
    Column("pdbx_total_number_of_bins_used", Integer),
    Column("pdbx_phase_error", Float),
    Column("pdbx_fsc_work", Float),
    Column("pdbx_fsc_free", Float),
    Column("R_factor_R_free", Float)
)


refine_occupancy = Table("refine_occupancy",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("class", String(255), primary_key=True),
    Column("details", String(255)),
    Column("treatment", String(10)),
    Column("value", Float)
)


refln = Table("refln",
    metadata_obj,
    Column("A_calc", Float),
    Column("A_calc_au", Float),
    Column("A_meas", Float),
    Column("A_meas_au", Float),
    Column("B_calc", Float),
    Column("B_calc_au", Float),
    Column("B_meas", Float),
    Column("B_meas_au", Float),
    Column("crystal_id", String(20)),
    Column("F_calc", Float),
    Column("F_calc_au", Float),
    Column("F_meas", Float),
    Column("F_meas_au", Float),
    Column("F_meas_sigma", Float),
    Column("F_meas_sigma_au", Float),
    Column("F_squared_calc", Float),
    Column("F_squared_meas", Float),
    Column("F_squared_sigma", Float),
    Column("fom", Float),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("intensity_calc", Float),
    Column("intensity_meas", Float),
    Column("intensity_sigma", Float),
    Column("status", String(10)),
    Column("phase_calc", Float),
    Column("phase_meas", Float),
    Column("refinement_status", String(10), default="incl"),
    Column("scale_group_code", String(128)),
    Column("sint_over_lambda", Float),
    Column("symmetry_epsilon", Integer),
    Column("symmetry_multiplicity", Integer),
    Column("wavelength", Float),
    Column("wavelength_id", String(20)),
    Column("class_code", String(20)),
    Column("d_spacing", Float),
    Column("include_status", String(20)),
    Column("mean_path_length_tbar", Float),
    Column("pdbx_F_calc_part_solvent", Float),
    Column("pdbx_phase_calc_part_solvent", Float),
    Column("pdbx_F_calc_with_solvent", Float),
    Column("pdbx_phase_calc_with_solvent", Float),
    Column("pdbx_anom_difference", Float),
    Column("pdbx_anom_difference_sigma", Float),
    Column("pdbx_I_plus", Float),
    Column("pdbx_I_minus", Float),
    Column("pdbx_F_plus", Float),
    Column("pdbx_F_minus", Float),
    Column("pdbx_I_plus_sigma", Float),
    Column("pdbx_I_minus_sigma", Float),
    Column("pdbx_F_minus_sigma", Float),
    Column("pdbx_F_plus_sigma", Float),
    Column("pdbx_HL_A_iso", Float),
    Column("pdbx_HL_B_iso", Float),
    Column("pdbx_HL_C_iso", Float),
    Column("pdbx_HL_D_iso", Float),
    Column("pdbx_fiber_layer", Integer),
    Column("pdbx_fiber_coordinate", Float),
    Column("pdbx_fiber_F_meas_au", Float),
    Column("pdbx_FWT", Float),
    Column("pdbx_PHWT", Float),
    Column("pdbx_DELFWT", Float),
    Column("pdbx_DELPHWT", Float),
    Column("pdbx_diffrn_id", String(20)),
    Column("pdbx_r_free_flag", Integer),
    Column("pdbx_anomalous_diff", Float),
    Column("pdbx_anomalous_diff_sigma", Float),
    Column("pdbx_phase_cycle", Float),
    Column("pdbx_cos_phase_calc", Float),
    Column("pdbx_sin_phase_calc", Float),
    Column("pdbx_signal", Float),
    Column("pdbx_signal_status", String(20))
)


refln_sys_abs = Table("refln_sys_abs",
    metadata_obj,
    Column("I", Float),
    Column("I_over_sigmaI", Float),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("sigmaI", Float)
)


reflns = Table("reflns",
    metadata_obj,
    Column("B_iso_Wilson_estimate", Float),
    Column("entry_id", String(20), nullable=False),
    Column("data_reduction_details", String(255)),
    Column("data_reduction_method", String(255)),
    Column("d_resolution_high", Float),
    Column("d_resolution_low", Float),
    Column("details", String(255)),
    Column("limit_h_max", Integer),
    Column("limit_h_min", Integer),
    Column("limit_k_max", Integer),
    Column("limit_k_min", Integer),
    Column("limit_l_max", Integer),
    Column("limit_l_min", Integer),
    Column("number_all", Integer),
    Column("number_obs", Integer),
    Column("observed_criterion", String(255)),
    Column("observed_criterion_F_max", Float),
    Column("observed_criterion_F_min", Float),
    Column("observed_criterion_I_max", Float),
    Column("observed_criterion_I_min", Float),
    Column("observed_criterion_sigma_F", Float),
    Column("observed_criterion_sigma_I", Float),
    Column("percent_possible_obs", Float),
    Column("R_free_details", String(255)),
    Column("Rmerge_F_all", Float),
    Column("Rmerge_F_obs", Float),
    Column("Friedel_coverage", Float),
    Column("number_gt", Integer),
    Column("threshold_expression", String(255)),
    Column("pdbx_redundancy", Float),
    Column("pdbx_netI_over_av_sigmaI", Float),
    Column("pdbx_netI_over_sigmaI", Float),
    Column("pdbx_res_netI_over_av_sigmaI_2", Float),
    Column("pdbx_res_netI_over_sigmaI_2", Float),
    Column("pdbx_chi_squared", Float),
    Column("pdbx_scaling_rejects", Integer),
    Column("pdbx_d_res_high_opt", Float),
    Column("pdbx_d_res_low_opt", Float),
    Column("pdbx_d_res_opt_method", String(255)),
    Column("phase_calculation_details", String(255)),
    Column("pdbx_Rrim_I_all", Float),
    Column("pdbx_Rpim_I_all", Float),
    Column("pdbx_d_opt", Float),
    Column("pdbx_number_measured_all", Integer),
    Column("pdbx_diffrn_id", String(20), nullable=False),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("pdbx_CC_half", Float),
    Column("pdbx_CC_star", Float),
    Column("pdbx_R_split", Float),
    Column("pdbx_redundancy_reflns_obs", Float),
    Column("pdbx_number_anomalous", Integer),
    Column("pdbx_Rrim_I_all_anomalous", Float),
    Column("pdbx_Rpim_I_all_anomalous", Float),
    Column("pdbx_Rmerge_I_anomalous", Float),
    Column("pdbx_Rmerge_I_obs", Float),
    Column("pdbx_Rmerge_I_all", Float),
    Column("pdbx_Rsym_value", Float),
    Column("pdbx_aniso_diffraction_limit_axis_1_ortho[1]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_1_ortho[2]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_1_ortho[3]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_2_ortho[1]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_2_ortho[2]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_2_ortho[3]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_3_ortho[1]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_3_ortho[2]", Float),
    Column("pdbx_aniso_diffraction_limit_axis_3_ortho[3]", Float),
    Column("pdbx_aniso_diffraction_limit_1", Float),
    Column("pdbx_aniso_diffraction_limit_2", Float),
    Column("pdbx_aniso_diffraction_limit_3", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_1_ortho[1]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_1_ortho[2]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_1_ortho[3]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_2_ortho[1]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_2_ortho[2]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_2_ortho[3]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_3_ortho[1]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_3_ortho[2]", Float),
    Column("pdbx_aniso_B_tensor_eigenvector_3_ortho[3]", Float),
    Column("pdbx_aniso_B_tensor_eigenvalue_1", Float),
    Column("pdbx_aniso_B_tensor_eigenvalue_2", Float),
    Column("pdbx_aniso_B_tensor_eigenvalue_3", Float),
    Column("pdbx_orthogonalization_convention", String(20)),
    Column("pdbx_percent_possible_ellipsoidal", Float),
    Column("pdbx_percent_possible_spherical", Float),
    Column("pdbx_percent_possible_ellipsoidal_anomalous", Float),
    Column("pdbx_percent_possible_spherical_anomalous", Float),
    Column("pdbx_redundancy_anomalous", Float),
    Column("pdbx_CC_half_anomalous", Float),
    Column("pdbx_absDiff_over_sigma_anomalous", Float),
    Column("pdbx_percent_possible_anomalous", Float),
    Column("pdbx_observed_signal_threshold", Float),
    Column("pdbx_signal_type", String(128)),
    Column("pdbx_signal_details", String(255)),
    Column("pdbx_signal_software_id", String(255)),
    Column("pdbx_CC_split_method", String(10))
)


reflns_scale = Table("reflns_scale",
    metadata_obj,
    Column("meas_F", Float),
    Column("meas_F_squared", Float),
    Column("meas_intensity", Float)
)


reflns_shell = Table("reflns_shell",
    metadata_obj,
    Column("d_res_high", Float, nullable=False),
    Column("d_res_low", Float),
    Column("meanI_over_sigI_all", Float),
    Column("meanI_over_sigI_obs", Float),
    Column("number_measured_all", Integer),
    Column("number_measured_obs", Integer),
    Column("number_possible", Integer),
    Column("number_unique_all", Integer),
    Column("number_unique_obs", Integer),
    Column("percent_possible_obs", Float),
    Column("Rmerge_F_all", Float),
    Column("Rmerge_F_obs", Float),
    Column("meanI_over_sigI_gt", Float),
    Column("meanI_over_uI_all", Float),
    Column("meanI_over_uI_gt", Float),
    Column("number_measured_gt", Integer),
    Column("number_unique_gt", Integer),
    Column("percent_possible_gt", Float),
    Column("Rmerge_F_gt", Float),
    Column("Rmerge_I_gt", Float),
    Column("pdbx_redundancy", Float),
    Column("pdbx_chi_squared", Float),
    Column("pdbx_netI_over_sigmaI_all", Float),
    Column("pdbx_netI_over_sigmaI_obs", Float),
    Column("pdbx_Rrim_I_all", Float),
    Column("pdbx_Rpim_I_all", Float),
    Column("pdbx_rejects", Integer),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("pdbx_diffrn_id", String(20)),
    Column("pdbx_CC_half", Float),
    Column("pdbx_CC_star", Float),
    Column("pdbx_R_split", Float),
    Column("pdbx_redundancy_reflns_obs", Float),
    Column("pdbx_number_anomalous", Integer),
    Column("pdbx_Rrim_I_all_anomalous", Float),
    Column("pdbx_Rpim_I_all_anomalous", Float),
    Column("pdbx_Rmerge_I_all_anomalous", Float),
    Column("percent_possible_all", Float),
    Column("Rmerge_I_all", Float),
    Column("Rmerge_I_obs", Float),
    Column("pdbx_Rsym_value", Float),
    Column("pdbx_percent_possible_ellipsoidal", Float),
    Column("pdbx_percent_possible_spherical", Float),
    Column("pdbx_percent_possible_ellipsoidal_anomalous", Float),
    Column("pdbx_percent_possible_spherical_anomalous", Float),
    Column("pdbx_redundancy_anomalous", Float),
    Column("pdbx_CC_half_anomalous", Float),
    Column("pdbx_absDiff_over_sigma_anomalous", Float),
    Column("pdbx_percent_possible_anomalous", Float)
)


software = Table("software",
    metadata_obj,
    Column("citation_id", String(20)),
    Column("classification", String(50), nullable=False),
    Column("compiler_name", String(128)),
    Column("compiler_version", String(128)),
    Column("contact_author", String(128)),
    Column("contact_author_email", String(128)),
    Column("date", String(128)),
    Column("description", String(128)),
    Column("dependencies", String(128)),
    Column("hardware", String(128)),
    Column("language", String(50)),
    Column("location", String(128)),
    Column("mods", String(128)),
    Column("name", String(255), nullable=False),
    Column("os", String(255)),
    Column("os_version", String(255)),
    Column("type", String(50)),
    Column("version", String(128)),
    Column("pdbx_ordinal", Integer, primary_key=True)
)


struct = Table("struct",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("title", String(255)),
    Column("pdbx_center_of_mass_x", Float),
    Column("pdbx_center_of_mass_y", Float),
    Column("pdbx_center_of_mass_z", Float),
    Column("pdbx_structure_determination_methodology", String(128)),
    Column("pdbx_descriptor", String(255)),
    Column("pdbx_model_details", String(255)),
    Column("pdbx_formula_weight", Float),
    Column("pdbx_formula_weight_method", String(128)),
    Column("pdbx_model_type_details", String(128)),
    Column("pdbx_CASP_flag", String(2)),
    Column("pdbx_details", String(255)),
    Column("pdbx_title_text", String(255))
)


struct_asym = Table("struct_asym",
    metadata_obj,
    Column("details", String(255)),
    Column("entity_id", String(20), nullable=False),
    Column("pdbx_modified", String(255)),
    Column("pdbx_blank_PDB_chainid_flag", String(20)),
    Column("pdbx_PDB_id", String(20)),
    Column("pdbx_alt_id", String(20)),
    Column("pdbx_type", String(10)),
    Column("pdbx_order", Integer),
    Column("pdbx_fraction_per_asym_unit", String(255)),
    Column("pdbx_missing_num_begin_of_chain_not_in_seqres", Integer),
    Column("pdbx_missing_num_end_of_chain_not_in_seqres", Integer),
    Column("pdbx_missing_num_begin_of_chain_in_seqres", Integer)
)


struct_biol = Table("struct_biol",
    metadata_obj,
    Column("details", String(255)),
    Column("pdbx_parent_biol_id", String(128)),
    Column("pdbx_formula_weight", Float),
    Column("pdbx_formula_weight_method", String(128)),
    Column("pdbx_aggregation_state", String(128)),
    Column("pdbx_assembly_method", String(255))
)


struct_biol_gen = Table("struct_biol_gen",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("biol_id", String(128), primary_key=True),
    Column("details", String(255)),
    Column("symmetry", String(10), primary_key=True),
    Column("pdbx_full_symmetry_operation", String(20)),
    Column("pdbx_PDB_order", Integer),
    Column("pdbx_new_asym_id", String(20), nullable=False),
    Column("pdbx_new_pdb_asym_id", String(20), nullable=False),
    Column("pdbx_color_red", Float, default="?"),
    Column("pdbx_color_green", Float, default="?"),
    Column("pdbx_color_blue", Float, default="?"),
    Column("pdbx_after_begin_residue_no", String(20)),
    Column("pdbx_after_end_residue_no", String(20)),
    Column("pdbx_before_begin_residue_no", String(20)),
    Column("pdbx_before_end_residue_no", String(20))
)


struct_biol_keywords = Table("struct_biol_keywords",
    metadata_obj,
    Column("biol_id", String(128), primary_key=True),
    Column("text", String(255), primary_key=True)
)


struct_biol_view = Table("struct_biol_view",
    metadata_obj,
    Column("biol_id", String(128), primary_key=True),
    Column("details", String(255)),
    Column("id", String(128), primary_key=True),
    Column("rot_matrix[1][1]", Float),
    Column("rot_matrix[1][2]", Float),
    Column("rot_matrix[1][3]", Float),
    Column("rot_matrix[2][1]", Float),
    Column("rot_matrix[2][2]", Float),
    Column("rot_matrix[2][3]", Float),
    Column("rot_matrix[3][1]", Float),
    Column("rot_matrix[3][2]", Float),
    Column("rot_matrix[3][3]", Float),
    Column("pdbx_vector[1]", Float, default=0.0),
    Column("pdbx_vector[2]", Float, default=0.0),
    Column("pdbx_vector[3]", Float, default=0.0)
)


struct_conf = Table("struct_conf",
    metadata_obj,
    Column("beg_label_asym_id", String(20), nullable=False),
    Column("beg_label_comp_id", String(10), nullable=False),
    Column("beg_label_seq_id", Integer, nullable=False),
    Column("beg_auth_asym_id", String(20)),
    Column("beg_auth_comp_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("conf_type_id", String(10), nullable=False),
    Column("details", String(255)),
    Column("end_label_asym_id", String(20), nullable=False),
    Column("end_label_comp_id", String(10), nullable=False),
    Column("end_label_seq_id", Integer, nullable=False),
    Column("end_auth_asym_id", String(20)),
    Column("end_auth_comp_id", String(20)),
    Column("end_auth_seq_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("pdbx_beg_PDB_ins_code", String(20)),
    Column("pdbx_end_PDB_ins_code", String(20)),
    Column("pdbx_PDB_helix_class", String(128)),
    Column("pdbx_PDB_helix_length", Integer),
    Column("pdbx_PDB_helix_id", String(20))
)


struct_conf_type = Table("struct_conf_type",
    metadata_obj,
    Column("criteria", String(255)),
    Column("reference", String(255))
)


struct_conn = Table("struct_conn",
    metadata_obj,
    Column("conn_type_id", String(10), nullable=False),
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("ptnr1_label_alt_id", String(20)),
    Column("ptnr1_label_asym_id", String(20), nullable=False),
    Column("ptnr1_label_atom_id", String(6)),
    Column("ptnr1_label_comp_id", String(10), nullable=False),
    Column("ptnr1_label_seq_id", Integer, nullable=False),
    Column("ptnr1_auth_asym_id", String(20)),
    Column("ptnr1_auth_atom_id", String(6)),
    Column("ptnr1_auth_comp_id", String(20)),
    Column("ptnr1_auth_seq_id", String(20)),
    Column("ptnr1_role", String(50)),
    Column("ptnr1_symmetry", String(10)),
    Column("ptnr2_label_alt_id", String(20)),
    Column("ptnr2_label_asym_id", String(20), nullable=False),
    Column("ptnr2_label_atom_id", String(6)),
    Column("ptnr2_label_comp_id", String(10), nullable=False),
    Column("ptnr2_label_seq_id", Integer, nullable=False),
    Column("ptnr2_auth_asym_id", String(20)),
    Column("ptnr2_auth_atom_id", String(6)),
    Column("ptnr2_auth_comp_id", String(20)),
    Column("ptnr2_auth_seq_id", String(20)),
    Column("ptnr2_role", String(50)),
    Column("ptnr2_symmetry", String(10)),
    Column("pdbx_ptnr1_PDB_ins_code", String(20)),
    Column("pdbx_ptnr1_auth_alt_id", String(20)),
    Column("pdbx_ptnr1_label_alt_id", String(20)),
    Column("pdbx_ptnr1_standard_comp_id", String(20)),
    Column("pdbx_ptnr2_PDB_ins_code", String(20)),
    Column("pdbx_ptnr2_auth_alt_id", String(20)),
    Column("pdbx_ptnr2_label_alt_id", String(20)),
    Column("pdbx_ptnr3_auth_alt_id", String(20)),
    Column("pdbx_ptnr3_auth_asym_id", String(20)),
    Column("pdbx_ptnr3_auth_atom_id", String(6)),
    Column("pdbx_ptnr3_auth_comp_id", String(20)),
    Column("pdbx_ptnr3_PDB_ins_code", String(20)),
    Column("pdbx_ptnr3_auth_seq_id", String(20)),
    Column("pdbx_ptnr3_label_alt_id", String(20)),
    Column("pdbx_ptnr3_label_asym_id", String(20)),
    Column("pdbx_ptnr3_label_atom_id", String(6)),
    Column("pdbx_ptnr3_label_comp_id", String(10)),
    Column("pdbx_ptnr3_label_seq_id", Integer),
    Column("pdbx_PDB_id", String(20)),
    Column("pdbx_dist_value", Float),
    Column("pdbx_value_order", String(10), default="sing"),
    Column("pdbx_leaving_atom_flag", String(20)),
    Column("pdbx_ptnr1_mod_name", String(128)),
    Column("pdbx_ptnr1_sugar_name", String(128)),
    Column("pdbx_ptnr1_replaced_atom", String(20)),
    Column("pdbx_ptnr3_auth_ins_code", String(20)),
    Column("pdbx_ptnr1_atom_stereo_config", String(10), default="N"),
    Column("pdbx_ptnr1_leaving_atom_id", String(6)),
    Column("pdbx_ptnr2_atom_stereo_config", String(10), default="N"),
    Column("pdbx_ptnr2_leaving_atom_id", String(6)),
    Column("pdbx_role", String(50))
)


struct_conn_type = Table("struct_conn_type",
    metadata_obj,
    Column("criteria", String(255)),
    Column("reference", String(255))
)


struct_keywords = Table("struct_keywords",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("text", String(255)),
    Column("pdbx_keywords", String(128)),
    Column("pdbx_details", String(255))
)


struct_mon_details = Table("struct_mon_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("prot_cis", Float),
    Column("RSCC", String(255)),
    Column("RSR", String(255))
)


struct_mon_nucl = Table("struct_mon_nucl",
    metadata_obj,
    Column("alpha", Float),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("beta", Float),
    Column("chi1", Float),
    Column("chi2", Float),
    Column("delta", Float),
    Column("details", Float),
    Column("epsilon", Float),
    Column("gamma", Float),
    Column("label_alt_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_comp_id", String(10), primary_key=True),
    Column("label_seq_id", Integer, primary_key=True),
    Column("mean_B_all", Float),
    Column("mean_B_base", Float),
    Column("mean_B_phos", Float),
    Column("mean_B_sugar", Float),
    Column("nu0", Float),
    Column("nu1", Float),
    Column("nu2", Float),
    Column("nu3", Float),
    Column("nu4", Float),
    Column("P", Float),
    Column("RSCC_all", Float),
    Column("RSCC_base", Float),
    Column("RSCC_phos", Float),
    Column("RSCC_sugar", Float),
    Column("RSR_all", Float),
    Column("RSR_base", Float),
    Column("RSR_phos", Float),
    Column("RSR_sugar", Float),
    Column("tau0", Float),
    Column("tau1", Float),
    Column("tau2", Float),
    Column("tau3", Float),
    Column("tau4", Float),
    Column("taum", Float),
    Column("zeta", Float)
)


struct_mon_prot = Table("struct_mon_prot",
    metadata_obj,
    Column("chi1", Float),
    Column("chi2", Float),
    Column("chi3", Float),
    Column("chi4", Float),
    Column("chi5", Float),
    Column("details", Float),
    Column("label_alt_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_comp_id", String(10), primary_key=True),
    Column("label_seq_id", Integer, primary_key=True),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("RSCC_all", Float),
    Column("RSCC_main", Float),
    Column("RSCC_side", Float),
    Column("RSR_all", Float),
    Column("RSR_main", Float),
    Column("RSR_side", Float),
    Column("mean_B_all", Float),
    Column("mean_B_main", Float),
    Column("mean_B_side", Float),
    Column("omega", Float),
    Column("phi", Float),
    Column("psi", Float)
)


struct_mon_prot_cis = Table("struct_mon_prot_cis",
    metadata_obj,
    Column("label_alt_id", String(20), nullable=False),
    Column("label_asym_id", String(20), nullable=False),
    Column("label_comp_id", String(10), nullable=False),
    Column("label_seq_id", Integer, nullable=False),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("pdbx_auth_asym_id_2", String(20)),
    Column("pdbx_auth_comp_id_2", String(20)),
    Column("pdbx_auth_seq_id_2", String(20)),
    Column("pdbx_label_asym_id_2", String(20)),
    Column("pdbx_label_comp_id_2", String(10)),
    Column("pdbx_label_seq_id_2", Integer),
    Column("pdbx_PDB_ins_code", String(20)),
    Column("pdbx_PDB_ins_code_2", String(20)),
    Column("pdbx_PDB_model_num", Integer, nullable=False),
    Column("pdbx_omega_angle", String(20)),
    Column("pdbx_id", String(20), primary_key=True),
    Column("pdbx_auth_ins_code", String(20)),
    Column("pdbx_auth_ins_code_2", String(20))
)


struct_ncs_dom = Table("struct_ncs_dom",
    metadata_obj,
    Column("details", String(255)),
    Column("pdbx_ens_id", String(20), primary_key=True)
)


struct_ncs_dom_lim = Table("struct_ncs_dom_lim",
    metadata_obj,
    Column("beg_label_alt_id", String(20)),
    Column("beg_label_asym_id", String(20)),
    Column("beg_label_comp_id", String(20)),
    Column("beg_label_seq_id", Integer),
    Column("beg_auth_asym_id", String(20)),
    Column("beg_auth_comp_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("dom_id", String(20), primary_key=True),
    Column("end_label_alt_id", String(20)),
    Column("end_label_asym_id", String(20)),
    Column("end_label_comp_id", String(20)),
    Column("end_label_seq_id", Integer),
    Column("end_auth_asym_id", String(20)),
    Column("end_auth_comp_id", String(20)),
    Column("end_auth_seq_id", String(20)),
    Column("selection_details", String(255)),
    Column("pdbx_component_id", Integer, primary_key=True),
    Column("pdbx_refine_code", Float),
    Column("pdbx_ens_id", String(20), primary_key=True)
)


struct_ncs_ens = Table("struct_ncs_ens",
    metadata_obj,
    Column("details", String(255)),
    Column("point_group", String(128))
)


struct_ncs_ens_gen = Table("struct_ncs_ens_gen",
    metadata_obj,
    Column("dom_id_1", String(20), primary_key=True),
    Column("dom_id_2", String(20), primary_key=True),
    Column("ens_id", String(20), primary_key=True),
    Column("oper_id", Integer, primary_key=True)
)


struct_ncs_oper = Table("struct_ncs_oper",
    metadata_obj,
    Column("code", String(20), nullable=False),
    Column("details", String(255)),
    Column("matrix[1][1]", Float, nullable=False),
    Column("matrix[1][2]", Float, nullable=False),
    Column("matrix[1][3]", Float, nullable=False),
    Column("matrix[2][1]", Float, nullable=False),
    Column("matrix[2][2]", Float, nullable=False),
    Column("matrix[2][3]", Float, nullable=False),
    Column("matrix[3][1]", Float, nullable=False),
    Column("matrix[3][2]", Float, nullable=False),
    Column("matrix[3][3]", Float, nullable=False),
    Column("vector[1]", Float, nullable=False),
    Column("vector[2]", Float, nullable=False),
    Column("vector[3]", Float, nullable=False)
)


struct_ref = Table("struct_ref",
    metadata_obj,
    Column("biol_id", String(128)),
    Column("db_code", String(128), nullable=False),
    Column("db_name", String(128), nullable=False),
    Column("details", String(255)),
    Column("entity_id", String(20), nullable=False),
    Column("seq_align", String(10)),
    Column("seq_dif", String(10)),
    Column("pdbx_db_accession", String(20)),
    Column("pdbx_db_isoform", String(20)),
    Column("pdbx_seq_one_letter_code", String(255)),
    Column("pdbx_align_begin", String(20)),
    Column("pdbx_align_end", String(20))
)


struct_ref_seq = Table("struct_ref_seq",
    metadata_obj,
    Column("db_align_beg", Integer, nullable=False),
    Column("db_align_end", Integer, nullable=False),
    Column("details", String(255)),
    Column("ref_id", String(20), nullable=False),
    Column("seq_align_beg", Integer, nullable=False),
    Column("seq_align_end", Integer, nullable=False),
    Column("pdbx_strand_id", String(20)),
    Column("pdbx_db_accession", String(20)),
    Column("pdbx_db_align_beg_ins_code", String(20)),
    Column("pdbx_db_align_end_ins_code", String(20)),
    Column("pdbx_PDB_id_code", String(20)),
    Column("pdbx_auth_seq_align_beg", String(20)),
    Column("pdbx_auth_seq_align_end", String(20)),
    Column("pdbx_seq_align_beg_ins_code", String(20)),
    Column("pdbx_seq_align_end_ins_code", String(20))
)


struct_ref_seq_dif = Table("struct_ref_seq_dif",
    metadata_obj,
    Column("align_id", String(20), nullable=False),
    Column("db_mon_id", String(10)),
    Column("details", String(255)),
    Column("mon_id", String(10)),
    Column("seq_num", Integer),
    Column("pdbx_pdb_id_code", String(20)),
    Column("pdbx_pdb_strand_id", String(20)),
    Column("pdbx_pdb_ins_code", String(20)),
    Column("pdbx_auth_seq_num", String(20)),
    Column("pdbx_seq_db_name", String(20)),
    Column("pdbx_seq_db_accession_code", String(20)),
    Column("pdbx_seq_db_seq_num", String(20)),
    Column("pdbx_ordinal", Integer, primary_key=True)
)


struct_sheet = Table("struct_sheet",
    metadata_obj,
    Column("details", String(255)),
    Column("number_strands", Integer),
    Column("type", String(255))
)


struct_sheet_hbond = Table("struct_sheet_hbond",
    metadata_obj,
    Column("range_1_beg_label_atom_id", String(6), nullable=False),
    Column("range_1_beg_label_seq_id", Integer, nullable=False),
    Column("range_1_end_label_atom_id", String(6), nullable=False),
    Column("range_1_end_label_seq_id", Integer, nullable=False),
    Column("range_2_beg_label_atom_id", String(6), nullable=False),
    Column("range_2_beg_label_seq_id", Integer, nullable=False),
    Column("range_2_end_label_atom_id", String(6), nullable=False),
    Column("range_2_end_label_seq_id", Integer, nullable=False),
    Column("range_1_beg_auth_atom_id", String(6)),
    Column("range_1_beg_auth_seq_id", String(20)),
    Column("range_1_end_auth_atom_id", String(6)),
    Column("range_1_end_auth_seq_id", String(20)),
    Column("range_2_beg_auth_atom_id", String(6)),
    Column("range_2_beg_auth_seq_id", String(20)),
    Column("range_2_end_auth_atom_id", String(6)),
    Column("range_2_end_auth_seq_id", String(20)),
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sheet_id", String(20), primary_key=True),
    Column("pdbx_range_1_beg_auth_comp_id", String(20)),
    Column("pdbx_range_1_beg_auth_asym_id", String(20)),
    Column("pdbx_range_1_end_auth_comp_id", String(20)),
    Column("pdbx_range_1_end_auth_asym_id", String(20)),
    Column("pdbx_range_1_beg_label_comp_id", String(10)),
    Column("pdbx_range_1_beg_label_asym_id", String(20)),
    Column("pdbx_range_1_beg_PDB_ins_code", String(20)),
    Column("pdbx_range_1_end_label_comp_id", String(10)),
    Column("pdbx_range_1_end_label_asym_id", String(20)),
    Column("pdbx_range_1_end_PDB_ins_code", String(20)),
    Column("pdbx_range_2_beg_label_comp_id", String(10)),
    Column("pdbx_range_2_beg_label_asym_id", String(20)),
    Column("pdbx_range_2_beg_PDB_ins_code", String(20)),
    Column("pdbx_range_2_end_label_comp_id", String(10)),
    Column("pdbx_range_2_end_label_asym_id", String(20)),
    Column("pdbx_range_2_end_label_ins_code", String(20))
)


struct_sheet_order = Table("struct_sheet_order",
    metadata_obj,
    Column("offset", Integer),
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sense", String(10)),
    Column("sheet_id", String(20), primary_key=True)
)


struct_sheet_range = Table("struct_sheet_range",
    metadata_obj,
    Column("beg_label_asym_id", String(20), nullable=False),
    Column("beg_label_comp_id", String(10), nullable=False),
    Column("beg_label_seq_id", Integer, nullable=False),
    Column("end_label_asym_id", String(20), nullable=False),
    Column("end_label_comp_id", String(10), nullable=False),
    Column("end_label_seq_id", Integer, nullable=False),
    Column("beg_auth_asym_id", String(20)),
    Column("beg_auth_comp_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("end_auth_asym_id", String(20)),
    Column("end_auth_comp_id", String(20)),
    Column("end_auth_seq_id", String(20)),
    Column("sheet_id", String(20), primary_key=True),
    Column("symmetry", String(10)),
    Column("pdbx_beg_PDB_ins_code", String(20)),
    Column("pdbx_end_PDB_ins_code", String(20))
)


struct_sheet_topology = Table("struct_sheet_topology",
    metadata_obj,
    Column("offset", Integer),
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sense", String(10)),
    Column("sheet_id", String(20), primary_key=True)
)


struct_site = Table("struct_site",
    metadata_obj,
    Column("details", String(255)),
    Column("pdbx_num_residues", Integer),
    Column("pdbx_evidence_code", String(255)),
    Column("pdbx_auth_asym_id", String(20)),
    Column("pdbx_auth_comp_id", String(20)),
    Column("pdbx_auth_seq_id", String(20)),
    Column("pdbx_auth_ins_code", String(20))
)


struct_site_gen = Table("struct_site_gen",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(128), primary_key=True),
    Column("label_alt_id", String(20)),
    Column("label_asym_id", String(20), nullable=False),
    Column("label_atom_id", String(6), nullable=False),
    Column("label_comp_id", String(10), nullable=False),
    Column("label_seq_id", Integer, nullable=False),
    Column("auth_asym_id", String(20)),
    Column("auth_atom_id", String(6)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("site_id", String(128), primary_key=True),
    Column("symmetry", String(10)),
    Column("pdbx_auth_ins_code", String(20)),
    Column("pdbx_num_res", Integer)
)


struct_site_keywords = Table("struct_site_keywords",
    metadata_obj,
    Column("site_id", String(128), primary_key=True),
    Column("text", String(255), primary_key=True)
)


struct_site_view = Table("struct_site_view",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(128), primary_key=True),
    Column("rot_matrix[1][1]", Float),
    Column("rot_matrix[1][2]", Float),
    Column("rot_matrix[1][3]", Float),
    Column("rot_matrix[2][1]", Float),
    Column("rot_matrix[2][2]", Float),
    Column("rot_matrix[2][3]", Float),
    Column("rot_matrix[3][1]", Float),
    Column("rot_matrix[3][2]", Float),
    Column("rot_matrix[3][3]", Float),
    Column("site_id", String(128), nullable=False)
)


symmetry = Table("symmetry",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cell_setting", String(10)),
    Column("Int_Tables_number", Integer),
    Column("space_group_name_Hall", String(128)),
    Column("space_group_name_H-M", String(128)),
    Column("pdbx_full_space_group_name_H-M", String(128))
)


symmetry_equiv = Table("symmetry_equiv",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("pos_as_xyz", String(128))
)


audit_link = Table("audit_link",
    metadata_obj,
    Column("block_code", String(20), primary_key=True),
    Column("block_description", String(255), primary_key=True)
)


diffrn_reflns_class = Table("diffrn_reflns_class",
    metadata_obj,
    Column("av_R_eq", Float),
    Column("av_sgI/I", Float),
    Column("av_uI/I", Float),
    Column("code", String(20), primary_key=True),
    Column("description", String(255)),
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("number", Integer)
)


refine_ls_class = Table("refine_ls_class",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("R_factor_gt", Float),
    Column("R_factor_all", Float),
    Column("R_Fsqd_factor", Float),
    Column("R_I_factor", Float),
    Column("wR_factor_all", Float)
)


reflns_class = Table("reflns_class",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("description", String(255)),
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("number_gt", Integer),
    Column("number_total", Integer),
    Column("R_factor_all", Float),
    Column("R_factor_gt", Float),
    Column("R_Fsqd_factor", Float),
    Column("R_I_factor", Float),
    Column("wR_factor_all", Float)
)


space_group = Table("space_group",
    metadata_obj,
    Column("crystal_system", String(20)),
    Column("id", String(20), primary_key=True),
    Column("IT_number", Integer),
    Column("name_Hall", String(128)),
    Column("name_H-M_alt", String(128))
)


space_group_symop = Table("space_group_symop",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("operation_xyz", String(128)),
    Column("sg_id", String(20))
)


valence_param = Table("valence_param",
    metadata_obj,
    Column("atom_1", String(20), primary_key=True),
    Column("atom_1_valence", Integer, primary_key=True),
    Column("atom_2", String(20), primary_key=True),
    Column("atom_2_valence", Integer, primary_key=True),
    Column("B", Float),
    Column("details", String(255)),
    Column("id", String(20)),
    Column("ref_id", String(20)),
    Column("Ro", Float)
)


valence_ref = Table("valence_ref",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("reference", String(255))
)


pdbx_audit = Table("pdbx_audit",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("current_version", String(20), nullable=False)
)


pdbx_version = Table("pdbx_version",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("revision_date", DateTime, nullable=False),
    Column("major_version", Integer, primary_key=True),
    Column("minor_version", String(20), primary_key=True),
    Column("details", String(255)),
    Column("revision_type", String(128), primary_key=True)
)


pdbx_audit_author = Table("pdbx_audit_author",
    metadata_obj,
    Column("address", String(255)),
    Column("name", String(128), nullable=False),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_database_message = Table("pdbx_database_message",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("message_id", String(255), primary_key=True),
    Column("date", Date, nullable=False),
    Column("content_type", String(20), nullable=False),
    Column("message_type", String(20), nullable=False),
    Column("sender", String(255)),
    Column("sender_address_fax", String(25)),
    Column("sender_address_phone", String(25)),
    Column("sender_address_email", String(80)),
    Column("sender_address_mail", String(255)),
    Column("receiver", String(255)),
    Column("receiver_address_fax", String(25)),
    Column("receiver_address_phone", String(25)),
    Column("receiver_address_email", String(80)),
    Column("receiver_address_mail", String(255)),
    Column("message", String(255))
)


pdbx_database_PDB_obs_spr = Table("pdbx_database_PDB_obs_spr",
    metadata_obj,
    Column("id", String(20), nullable=False),
    Column("date", Date, nullable=False),
    Column("pdb_id", String(20), primary_key=True),
    Column("replace_pdb_id", String(255), primary_key=True),
    Column("details", String(255))
)


pdbx_database_proc = Table("pdbx_database_proc",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cycle_id", String(20), primary_key=True),
    Column("date_begin_cycle", Date, nullable=False),
    Column("date_end_cycle", Date, nullable=False),
    Column("details", String(255))
)


pdbx_database_remark = Table("pdbx_database_remark",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("text", String(255))
)


pdbx_database_status = Table("pdbx_database_status",
    metadata_obj,
    Column("status_code", String(20), nullable=False),
    Column("author_release_status_code", String(20)),
    Column("status_code_sf", String(20)),
    Column("status_code_mr", String(20)),
    Column("dep_release_code_coordinates", String(128), default="RELEASE NOW"),
    Column("dep_release_code_sequence", String(128), default="RELEASE NOW"),
    Column("dep_release_code_struct_fact", String(128), default="RELEASE NOW"),
    Column("dep_release_code_nmr_constraints", String(128), default="RELEASE NOW"),
    Column("entry_id", String(20), primary_key=True),
    Column("recvd_deposit_form", String(2)),
    Column("date_deposition_form", Date),
    Column("date_begin_deposition", Date),
    Column("date_begin_processing", Date),
    Column("date_end_processing", Date),
    Column("date_begin_release_preparation", Date),
    Column("date_author_release_request", Date),
    Column("recvd_coordinates", String(2)),
    Column("date_coordinates", Date),
    Column("recvd_struct_fact", String(2)),
    Column("date_struct_fact", Date),
    Column("recvd_nmr_constraints", String(2)),
    Column("date_nmr_constraints", Date),
    Column("recvd_internal_approval", String(2)),
    Column("recvd_manuscript", String(2)),
    Column("date_manuscript", Date),
    Column("name_depositor", String(255)),
    Column("recvd_author_approval", String(2)),
    Column("author_approval_type", String(20)),
    Column("date_author_approval", Date),
    Column("recvd_initial_deposition_date", DateTime),
    Column("date_submitted", Date),
    Column("rcsb_annotator", String(20)),
    Column("date_of_sf_release", DateTime),
    Column("date_of_mr_release", DateTime),
    Column("date_of_PDB_release", Date),
    Column("date_hold_coordinates", Date),
    Column("date_hold_struct_fact", Date),
    Column("date_hold_nmr_constraints", Date),
    Column("hold_for_publication", String(2)),
    Column("SG_entry", String(2)),
    Column("pdb_date_of_author_approval", Date),
    Column("deposit_site", String(20)),
    Column("process_site", String(20)),
    Column("dep_release_code_chemical_shifts", String(128), default="RELEASE NOW"),
    Column("recvd_chemical_shifts", String(2)),
    Column("date_chemical_shifts", Date),
    Column("date_hold_chemical_shifts", Date),
    Column("status_code_cs", String(20)),
    Column("date_of_cs_release", DateTime),
    Column("date_nmr_data", Date),
    Column("date_hold_nmr_data", Date),
    Column("date_of_nmr_data_release", DateTime),
    Column("dep_release_code_nmr_data", String(128), default="RELEASE NOW"),
    Column("recvd_nmr_data", String(2)),
    Column("status_code_nmr_data", String(20)),
    Column("methods_development_category", String(128)),
    Column("pdb_format_compatible", String(2), default="Y"),
    Column("post_rel_status", String(20)),
    Column("post_rel_recvd_coord", String(20)),
    Column("post_rel_recvd_coord_date", DateTime),
    Column("auth_req_rel_date", DateTime),
    Column("ndb_tid", String(20)),
    Column("status_coordinates_in_NDB", String(2)),
    Column("date_revised", DateTime),
    Column("replaced_entry_id", String(20)),
    Column("revision_id", String(20)),
    Column("revision_description", String(255)),
    Column("pdbx_annotator", String(20)),
    Column("date_of_NDB_release", DateTime),
    Column("date_released_to_PDB", DateTime),
    Column("skip_PDB_REMARK_500", String(2), default="N"),
    Column("skip_PDB_REMARK", String(128)),
    Column("title_suppression", String(2), default="N"),
    Column("date_accepted_terms_and_conditions", DateTime)
)


pdbx_entity_name = Table("pdbx_entity_name",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("name", String(128), primary_key=True),
    Column("name_type", String(128), primary_key=True)
)


pdbx_prerelease_seq = Table("pdbx_prerelease_seq",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("seq_one_letter_code", String(255))
)


pdbx_poly_seq_scheme = Table("pdbx_poly_seq_scheme",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("seq_id", Integer, primary_key=True),
    Column("hetero", String(10), default="no"),
    Column("mon_id", String(10), primary_key=True),
    Column("pdb_strand_id", String(20)),
    Column("ndb_seq_num", Integer),
    Column("pdb_seq_num", String(20)),
    Column("auth_seq_num", String(20)),
    Column("pdb_mon_id", String(20)),
    Column("auth_mon_id", String(20)),
    Column("pdb_ins_code", String(20))
)


pdbx_nonpoly_scheme = Table("pdbx_nonpoly_scheme",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("entity_id", String(20)),
    Column("mon_id", String(10)),
    Column("pdb_strand_id", String(20)),
    Column("ndb_seq_num", String(20), primary_key=True),
    Column("pdb_seq_num", String(20)),
    Column("auth_seq_num", String(20)),
    Column("pdb_mon_id", String(20)),
    Column("auth_mon_id", String(20)),
    Column("pdb_ins_code", String(20))
)


pdbx_refine = Table("pdbx_refine",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("R_factor_all_no_cutoff", Float),
    Column("R_factor_obs_no_cutoff", Float),
    Column("free_R_factor_4sig_cutoff", Float),
    Column("free_R_factor_no_cutoff", Float),
    Column("free_R_error_no_cutoff", Float),
    Column("free_R_val_test_set_size_perc_no_cutoff", Float),
    Column("free_R_val_test_set_ct_no_cutoff", Float),
    Column("number_reflns_obs_no_cutoff", Float),
    Column("R_factor_all_4sig_cutoff", Float),
    Column("R_factor_obs_4sig_cutoff", Float),
    Column("free_R_val_4sig_cutoff", Float),
    Column("free_R_val_test_set_size_perc_4sig_cutoff", Float),
    Column("free_R_val_test_set_ct_4sig_cutoff", Float),
    Column("number_reflns_obs_4sig_cutoff", Float),
    Column("free_R_val_no_cutoff", Float)
)


pdbx_struct_sheet_hbond = Table("pdbx_struct_sheet_hbond",
    metadata_obj,
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sheet_id", String(20), primary_key=True),
    Column("range_1_label_atom_id", String(6), nullable=False),
    Column("range_1_label_seq_id", Integer, nullable=False),
    Column("range_1_label_comp_id", String(10)),
    Column("range_1_label_asym_id", String(20)),
    Column("range_1_auth_atom_id", String(6)),
    Column("range_1_auth_seq_id", String(20)),
    Column("range_1_auth_comp_id", String(20)),
    Column("range_1_auth_asym_id", String(20)),
    Column("range_1_PDB_ins_code", String(20)),
    Column("range_2_label_atom_id", String(6), nullable=False),
    Column("range_2_label_seq_id", Integer, nullable=False),
    Column("range_2_label_comp_id", String(10)),
    Column("range_2_label_asym_id", String(20)),
    Column("range_2_auth_atom_id", String(6)),
    Column("range_2_auth_seq_id", String(20)),
    Column("range_2_auth_comp_id", String(20)),
    Column("range_2_auth_asym_id", String(20)),
    Column("range_2_PDB_ins_code", String(20))
)


pdbx_xplor_file = Table("pdbx_xplor_file",
    metadata_obj,
    Column("serial_no", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("param_file", String(128)),
    Column("topol_file", String(128))
)


pdbx_refine_aux_file = Table("pdbx_refine_aux_file",
    metadata_obj,
    Column("serial_no", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("file_name", String(128)),
    Column("file_type", String(128))
)


pdbx_database_related = Table("pdbx_database_related",
    metadata_obj,
    Column("db_name", String(20), primary_key=True),
    Column("details", String(255)),
    Column("db_id", String(80), primary_key=True),
    Column("content_type", String(128), primary_key=True)
)


pdbx_entity_assembly = Table("pdbx_entity_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("biol_id", String(128), nullable=False),
    Column("num_copies", Integer, nullable=False)
)


pdbx_exptl_crystal_grow_comp = Table("pdbx_exptl_crystal_grow_comp",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("comp_id", String(20), primary_key=True),
    Column("comp_name", String(128)),
    Column("sol_id", String(128)),
    Column("conc", Float),
    Column("conc_range", String(128)),
    Column("conc_units", String(128))
)


pdbx_exptl_crystal_grow_sol = Table("pdbx_exptl_crystal_grow_sol",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("sol_id", String(128), primary_key=True),
    Column("volume", Float),
    Column("volume_units", String(128)),
    Column("pH", Float)
)


pdbx_exptl_crystal_cryo_treatment = Table("pdbx_exptl_crystal_cryo_treatment",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("final_solution_details", String(255)),
    Column("soaking_details", String(255)),
    Column("cooling_details", String(255)),
    Column("annealing_details", String(255))
)


pdbx_refine_tls = Table("pdbx_refine_tls",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), nullable=False),
    Column("details", String(255)),
    Column("method", String(10)),
    Column("origin_x", Float),
    Column("origin_y", Float),
    Column("origin_z", Float),
    Column("T[1][1]", Float),
    Column("T[1][1]_esd", Float, default=0.0),
    Column("T[1][2]", Float),
    Column("T[1][2]_esd", Float, default=0.0),
    Column("T[1][3]", Float),
    Column("T[1][3]_esd", Float, default=0.0),
    Column("T[2][2]", Float),
    Column("T[2][2]_esd", Float, default=0.0),
    Column("T[2][3]", Float),
    Column("T[2][3]_esd", Float, default=0.0),
    Column("T[3][3]", Float),
    Column("T[3][3]_esd", Float, default=0.0),
    Column("L[1][1]", Float),
    Column("L[1][1]_esd", Float, default=0.0),
    Column("L[1][2]", Float),
    Column("L[1][2]_esd", Float, default=0.0),
    Column("L[1][3]", Float),
    Column("L[1][3]_esd", Float, default=0.0),
    Column("L[2][2]", Float),
    Column("L[2][2]_esd", Float, default=0.0),
    Column("L[2][3]", Float),
    Column("L[2][3]_esd", Float, default=0.0),
    Column("L[3][3]", Float),
    Column("L[3][3]_esd", Float, default=0.0),
    Column("S[1][1]", Float),
    Column("S[1][1]_esd", Float, default=0.0),
    Column("S[1][2]", Float),
    Column("S[1][2]_esd", Float, default=0.0),
    Column("S[1][3]", Float),
    Column("S[1][3]_esd", Float, default=0.0),
    Column("S[2][1]", Float),
    Column("S[2][1]_esd", Float, default=0.0),
    Column("S[2][2]", Float),
    Column("S[2][2]_esd", Float, default=0.0),
    Column("S[2][3]", Float),
    Column("S[2][3]_esd", Float, default=0.0),
    Column("S[3][1]", Float),
    Column("S[3][1]_esd", Float, default=0.0),
    Column("S[3][2]", Float),
    Column("S[3][2]_esd", Float, default=0.0),
    Column("S[3][3]", Float),
    Column("S[3][3]_esd", Float, default=0.0)
)


pdbx_refine_tls_group = Table("pdbx_refine_tls_group",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), nullable=False),
    Column("refine_tls_id", String(20), nullable=False),
    Column("beg_label_asym_id", String(20)),
    Column("beg_label_seq_id", Integer),
    Column("beg_auth_asym_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("beg_PDB_ins_code", String(20)),
    Column("end_label_asym_id", String(20)),
    Column("end_label_seq_id", Integer),
    Column("end_auth_asym_id", String(20)),
    Column("end_auth_seq_id", String(20)),
    Column("end_PDB_ins_code", String(20)),
    Column("selection", String(128)),
    Column("selection_details", String(255))
)


pdbx_contact_author = Table("pdbx_contact_author",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("address_1", String(255)),
    Column("address_2", String(255)),
    Column("address_3", String(255)),
    Column("legacy_address", String(255)),
    Column("city", String(128)),
    Column("state_province", String(128)),
    Column("postal_code", String(128)),
    Column("email", String(128), nullable=False),
    Column("fax", String(128)),
    Column("name_first", String(128), nullable=False),
    Column("name_last", String(128), nullable=False),
    Column("name_mi", String(128)),
    Column("name_salutation", String(128)),
    Column("country", String(128)),
    Column("continent", String(128)),
    Column("phone", String(128)),
    Column("role", String(128)),
    Column("organization_type", String(128)),
    Column("identifier_ORCID", String(20))
)


pdbx_SG_project = Table("pdbx_SG_project",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("project_name", String(255)),
    Column("full_name_of_center", String(255)),
    Column("initial_of_center", String(255))
)


pdbx_atom_site_aniso_tls = Table("pdbx_atom_site_aniso_tls",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type_symbol", String(20), nullable=False),
    Column("tls_group_id", String(20), primary_key=True),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("auth_atom_id", String(6), nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_alt_id", String(20), nullable=False),
    Column("label_asym_id", String(20)),
    Column("label_atom_id", String(6)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("U_tls[1][1]", Float, nullable=False),
    Column("U_tls[2][2]", Float, nullable=False),
    Column("U_tls[3][3]", Float, nullable=False),
    Column("U_tls[1][2]", Float, nullable=False),
    Column("U_tls[1][3]", Float, nullable=False),
    Column("U_tls[2][3]", Float, nullable=False)
)


pdbx_nmr_details = Table("pdbx_nmr_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("text", String(255))
)


pdbx_nmr_sample_details = Table("pdbx_nmr_sample_details",
    metadata_obj,
    Column("solution_id", String(20), primary_key=True),
    Column("contents", String(255)),
    Column("solvent_system", String(255)),
    Column("label", String(128), default="sample_1"),
    Column("type", String(128), default="solution"),
    Column("details", String(255))
)


pdbx_nmr_exptl_sample = Table("pdbx_nmr_exptl_sample",
    metadata_obj,
    Column("solution_id", String(20), primary_key=True),
    Column("component", String(128), primary_key=True),
    Column("concentration", Float),
    Column("concentration_range", String(30)),
    Column("concentration_units", String(128)),
    Column("isotopic_labeling", String(128)),
    Column("concentration_err", Float)
)


pdbx_nmr_exptl_sample_conditions = Table("pdbx_nmr_exptl_sample_conditions",
    metadata_obj,
    Column("conditions_id", String(20), primary_key=True),
    Column("temperature", String(30)),
    Column("pressure_units", String(20)),
    Column("pressure", String(128)),
    Column("pH", String(30)),
    Column("ionic_strength", String(128)),
    Column("details", String(255)),
    Column("ionic_strength_err", Float),
    Column("ionic_strength_units", String(128)),
    Column("label", String(128), default="sample_conditions_1"),
    Column("pH_err", Float),
    Column("pH_units", String(128)),
    Column("pressure_err", Float),
    Column("temperature_err", Float),
    Column("temperature_units", String(128))
)


pdbx_nmr_spectrometer = Table("pdbx_nmr_spectrometer",
    metadata_obj,
    Column("spectrometer_id", String(20), primary_key=True),
    Column("model", String(128)),
    Column("type", String(128)),
    Column("manufacturer", String(128)),
    Column("field_strength", Float),
    Column("details", String(255)),
    Column("name", String(128))
)


pdbx_nmr_exptl = Table("pdbx_nmr_exptl",
    metadata_obj,
    Column("experiment_id", String(20), primary_key=True),
    Column("conditions_id", String(20), primary_key=True),
    Column("solution_id", String(20), primary_key=True),
    Column("type", String(128)),
    Column("spectrometer_id", Integer),
    Column("sample_state", String(128), default="isotropic")
)


pdbx_nmr_software = Table("pdbx_nmr_software",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("classification", String(128), nullable=False),
    Column("name", String(128), nullable=False),
    Column("version", String(128)),
    Column("authors", String(255)),
    Column("details", String(255))
)


pdbx_nmr_constraints = Table("pdbx_nmr_constraints",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("NOE_constraints_total", Integer),
    Column("NOE_intraresidue_total_count", Integer),
    Column("NOE_interentity_total_count", Integer),
    Column("NOE_sequential_total_count", Integer),
    Column("NOE_medium_range_total_count", Integer),
    Column("NOE_long_range_total_count", Integer),
    Column("protein_phi_angle_constraints_total_count", Integer),
    Column("protein_psi_angle_constraints_total_count", Integer),
    Column("protein_chi_angle_constraints_total_count", Integer),
    Column("protein_other_angle_constraints_total_count", Integer),
    Column("NOE_interproton_distance_evaluation", String(255)),
    Column("NOE_pseudoatom_corrections", String(255)),
    Column("NOE_motional_averaging_correction", String(255)),
    Column("hydrogen_bond_constraints_total_count", Integer),
    Column("disulfide_bond_constraints_total_count", Integer),
    Column("NA_alpha-angle_constraints_total_count", Integer),
    Column("NA_beta-angle_constraints_total_count", Integer),
    Column("NA_gamma-angle_constraints_total_count", Integer),
    Column("NA_delta-angle_constraints_total_count", Integer),
    Column("NA_epsilon-angle_constraints_total_count", Integer),
    Column("NA_chi-angle_constraints_total_count", Integer),
    Column("NA_other-angle_constraints_total_count", Integer),
    Column("NA_sugar_pucker_constraints_total_count", Integer)
)


pdbx_nmr_ensemble = Table("pdbx_nmr_ensemble",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("conformers_calculated_total_number", Integer),
    Column("conformers_submitted_total_number", Integer),
    Column("conformer_selection_criteria", String(255)),
    Column("representative_conformer", Integer),
    Column("average_constraints_per_residue", Integer),
    Column("average_constraint_violations_per_residue", Integer),
    Column("maximum_distance_constraint_violation", Float),
    Column("average_distance_constraint_violation", Float),
    Column("maximum_upper_distance_constraint_violation", Float),
    Column("maximum_lower_distance_constraint_violation", Float),
    Column("distance_constraint_violation_method", String(255)),
    Column("maximum_torsion_angle_constraint_violation", Float),
    Column("average_torsion_angle_constraint_violation", Float),
    Column("torsion_angle_constraint_violation_method", String(255))
)


pdbx_nmr_ensemble_rms = Table("pdbx_nmr_ensemble_rms",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("residue_range_begin", Integer),
    Column("chain_range_begin", String(20)),
    Column("residue_range_end", Integer),
    Column("chain_range_end", String(20)),
    Column("atom_type", String(128)),
    Column("distance_rms_dev", Float),
    Column("distance_rms_dev_error", Float),
    Column("covalent_bond_rms_dev", Float),
    Column("covalent_bond_rms_dev_error", Float),
    Column("bond_angle_rms_dev", Float),
    Column("bond_angle_rms_dev_error", Float),
    Column("improper_torsion_angle_rms_dev", Float),
    Column("improper_torsion_angle_rms_dev_error", Float),
    Column("peptide_planarity_rms_dev", Float),
    Column("peptide_planarity_rms_dev_error", Float),
    Column("dihedral_angles_rms_dev", Float),
    Column("dihedral_angles_rms_dev_error", Float),
    Column("coord_average_rmsd_method", String(255))
)


pdbx_nmr_representative = Table("pdbx_nmr_representative",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("conformer_id", String(128)),
    Column("selection_criteria", String(128))
)


pdbx_nmr_refine = Table("pdbx_nmr_refine",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255)),
    Column("details", String(255)),
    Column("software_ordinal", Integer, primary_key=True)
)


pdbx_nmr_force_constants = Table("pdbx_nmr_force_constants",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("exptl_distance_term", Float),
    Column("exptl_distance_term_units", String(20)),
    Column("exptl_torsion_angles_term", Float),
    Column("exptl_torsion_angles_term_units", String(20)),
    Column("exptl_J_coupling_term", Float),
    Column("exptl_J_coupling_term_units", String(20)),
    Column("exptl_13C_shift_term", Float),
    Column("exptl_13C_shift_term_units", String(20)),
    Column("exptl_1H_shift_term", Float),
    Column("exptl_1H_shift_term_units", String(20)),
    Column("exptl_dipolar_coupling_term", Float),
    Column("exptl_dipolar_coupling_term_units", String(20)),
    Column("exptl_D_isotope_shift_term", Float),
    Column("exptl_D_isotope_shift_term_units", String(20)),
    Column("covalent_geom_bond_term", Float),
    Column("covalent_geom_bond_term_units", String(20)),
    Column("covalent_geom_angles_term", Float),
    Column("covalent_geom_angles_term_units", String(20)),
    Column("covalent_geom_impropers_term", Float),
    Column("covalent_geom_impropers_term_units", String(20)),
    Column("non-bonded_inter_van_der_Waals_term_type", String(255)),
    Column("non-bonded_inter_van_der_Waals_term", Float),
    Column("non-bonded_inter_van_der_Waals_term_units", String(20)),
    Column("non-bonded_inter_conf_db_potential_term", Float),
    Column("non-bonded_inter_radius_of_gyration_term", Float),
    Column("non-bonded_inter_radius_of_gyration_term_units", String(20))
)


ndb_struct_conf_na = Table("ndb_struct_conf_na",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("feature", String(128), primary_key=True),
    Column("feature_count", Integer)
)


ndb_struct_feature_na = Table("ndb_struct_feature_na",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("feature", String(128), primary_key=True),
    Column("feature_count", Integer)
)


ndb_struct_na_base_pair = Table("ndb_struct_na_base_pair",
    metadata_obj,
    Column("model_number", Integer, primary_key=True),
    Column("pair_number", Integer, nullable=False),
    Column("pair_name", String(128), nullable=False),
    Column("i_label_asym_id", String(20), primary_key=True),
    Column("i_label_comp_id", String(10), primary_key=True),
    Column("i_label_seq_id", Integer, primary_key=True),
    Column("i_symmetry", String(10), primary_key=True, default="1_555"),
    Column("j_label_asym_id", String(20), primary_key=True),
    Column("j_label_comp_id", String(10), primary_key=True),
    Column("j_label_seq_id", Integer, primary_key=True),
    Column("j_symmetry", String(10), primary_key=True, default="1_555"),
    Column("i_auth_asym_id", String(20), nullable=False),
    Column("i_auth_seq_id", String(20), nullable=False),
    Column("i_PDB_ins_code", String(20)),
    Column("j_auth_asym_id", String(20), nullable=False),
    Column("j_auth_seq_id", String(20), nullable=False),
    Column("j_PDB_ins_code", String(20)),
    Column("shear", Float),
    Column("stretch", Float),
    Column("stagger", Float),
    Column("buckle", Float),
    Column("propeller", Float),
    Column("opening", Float),
    Column("hbond_type_12", Integer),
    Column("hbond_type_28", Integer),
    Column("hbond_type_leontis_westhof", String(128))
)


ndb_struct_na_base_pair_step = Table("ndb_struct_na_base_pair_step",
    metadata_obj,
    Column("model_number", Integer, primary_key=True),
    Column("step_number", Integer, nullable=False),
    Column("step_name", String(128), nullable=False),
    Column("i_label_asym_id_1", String(20), primary_key=True),
    Column("i_label_comp_id_1", String(10), primary_key=True),
    Column("i_label_seq_id_1", Integer, primary_key=True),
    Column("i_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("j_label_asym_id_1", String(20)),
    Column("j_label_comp_id_1", String(10)),
    Column("j_label_seq_id_1", Integer),
    Column("j_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("i_label_asym_id_2", String(20), primary_key=True),
    Column("i_label_comp_id_2", String(10), primary_key=True),
    Column("i_label_seq_id_2", Integer, primary_key=True),
    Column("i_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("j_label_asym_id_2", String(20)),
    Column("j_label_comp_id_2", String(10)),
    Column("j_label_seq_id_2", Integer),
    Column("j_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("i_auth_asym_id_1", String(20), nullable=False),
    Column("i_auth_seq_id_1", String(20), nullable=False),
    Column("i_PDB_ins_code_1", String(20)),
    Column("j_auth_asym_id_1", String(20), nullable=False),
    Column("j_auth_seq_id_1", String(20), nullable=False),
    Column("j_PDB_ins_code_1", String(20)),
    Column("i_auth_asym_id_2", String(20), nullable=False),
    Column("i_auth_seq_id_2", String(20), nullable=False),
    Column("i_PDB_ins_code_2", String(20)),
    Column("j_auth_asym_id_2", String(20), nullable=False),
    Column("j_auth_seq_id_2", String(20), nullable=False),
    Column("j_PDB_ins_code_2", String(20)),
    Column("shift", Float),
    Column("slide", Float),
    Column("rise", Float),
    Column("tilt", Float),
    Column("roll", Float),
    Column("twist", Float),
    Column("x_displacement", Float),
    Column("y_displacement", Float),
    Column("helical_rise", Float),
    Column("inclination", Float),
    Column("tip", Float),
    Column("helical_twist", Float)
)


ndb_original_ndb_coordinates = Table("ndb_original_ndb_coordinates",
    metadata_obj,
    Column("coord_section", String(255), primary_key=True)
)


pdbx_entity_nonpoly = Table("pdbx_entity_nonpoly",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("comp_id", String(10)),
    Column("name", String(255))
)


pdbx_phasing_dm = Table("pdbx_phasing_dm",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(128)),
    Column("mask_type", String(128)),
    Column("fom_acentric", Float),
    Column("fom_centric", Float),
    Column("fom", Float),
    Column("reflns_acentric", Integer),
    Column("reflns_centric", Integer),
    Column("reflns", Integer),
    Column("delta_phi_initial", Float),
    Column("delta_phi_final", Float)
)


pdbx_phasing_dm_shell = Table("pdbx_phasing_dm_shell",
    metadata_obj,
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("fom_acentric", Float),
    Column("fom_centric", Float),
    Column("fom", Float),
    Column("reflns_acentric", Integer),
    Column("reflns_centric", Integer),
    Column("reflns", Integer),
    Column("delta_phi_initial", Float),
    Column("delta_phi_final", Float)
)


pdbx_phasing_MAD_shell = Table("pdbx_phasing_MAD_shell",
    metadata_obj,
    Column("d_res_low", Float, primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("reflns_acentric", Float),
    Column("reflns_centric", Integer),
    Column("reflns", Integer),
    Column("fom_acentric", Float),
    Column("fom_centric", Float),
    Column("fom", Float),
    Column("R_cullis_centric", Float),
    Column("R_cullis_acentric", Float),
    Column("R_cullis", Float),
    Column("R_kraut_centric", Float),
    Column("R_kraut_acentric", Float),
    Column("R_kraut", Float),
    Column("loc_centric", Float),
    Column("loc_acentric", Float),
    Column("loc", Float),
    Column("power_centric", Float),
    Column("power_acentric", Float),
    Column("power", Float)
)


pdbx_phasing_MAD_set = Table("pdbx_phasing_MAD_set",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("d_res_low", Float),
    Column("d_res_high", Float),
    Column("number_of_sites", Integer),
    Column("reflns_acentric", Integer),
    Column("reflns_centric", Integer),
    Column("reflns", Integer),
    Column("fom_acentric", Float),
    Column("fom_centric", Float),
    Column("fom", Float),
    Column("R_cullis_centric", Float),
    Column("R_cullis_acentric", Float),
    Column("R_cullis", Float),
    Column("R_kraut_centric", Float),
    Column("R_kraut_acentric", Float),
    Column("R_kraut", Float),
    Column("loc_centric", Float),
    Column("loc_acentric", Float),
    Column("loc", Float),
    Column("power_centric", Float),
    Column("power_acentric", Float),
    Column("power", Float)
)


pdbx_phasing_MAD_set_shell = Table("pdbx_phasing_MAD_set_shell",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("reflns_acentric", Integer),
    Column("reflns_centric", Integer),
    Column("reflns", Integer),
    Column("fom_acentric", Float),
    Column("fom_centric", Float),
    Column("fom", Float),
    Column("R_cullis_centric", Float),
    Column("R_cullis_acentric", Float),
    Column("R_cullis", Float),
    Column("R_kraut_centric", Float),
    Column("R_kraut_acentric", Float),
    Column("R_kraut", Float),
    Column("loc_centric", Float),
    Column("loc_acentric", Float),
    Column("loc", Float),
    Column("power_centric", Float),
    Column("power_acentric", Float),
    Column("power", Float)
)


pdbx_phasing_MAD_set_site = Table("pdbx_phasing_MAD_set_site",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("atom_type_symbol", String(20)),
    Column("Cartn_x", Float),
    Column("Cartn_y", Float),
    Column("Cartn_z", Float),
    Column("Cartn_x_esd", Float),
    Column("Cartn_y_esd", Float),
    Column("Cartn_z_esd", Float),
    Column("fract_x", Float),
    Column("fract_y", Float),
    Column("fract_z", Float),
    Column("fract_x_esd", Float),
    Column("fract_y_esd", Float),
    Column("fract_z_esd", Float),
    Column("b_iso", Float),
    Column("b_iso_esd", Float),
    Column("occupancy", Float),
    Column("occupancy_esd", Float),
    Column("set_id", String(20)),
    Column("occupancy_iso", Float)
)


pdbx_phasing_MR = Table("pdbx_phasing_MR",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("method_rotation", String(128)),
    Column("d_res_high_rotation", Float),
    Column("d_res_low_rotation", Float),
    Column("sigma_F_rotation", Float),
    Column("sigma_I_rotation", Float),
    Column("reflns_percent_rotation", Float),
    Column("method_translation", String(128)),
    Column("d_res_high_translation", Float),
    Column("d_res_low_translation", Float),
    Column("sigma_F_translation", Float),
    Column("sigma_I_translation", Float),
    Column("reflns_percent_translation", Float),
    Column("correlation_coeff_Io_to_Ic", Float),
    Column("correlation_coeff_Fo_to_Fc", Float),
    Column("R_factor", Float),
    Column("R_rigid_body", Float),
    Column("packing", Float),
    Column("model_details", String(255)),
    Column("native_set_id", String(128)),
    Column("d_res_high_fit", Float),
    Column("d_res_low_fit", Float),
    Column("zscore_rotation", Float),
    Column("LL_gain_rotation", Float),
    Column("zscore_translation", Float),
    Column("LL_gain_translation", Float)
)


pdbx_refine_component = Table("pdbx_refine_component",
    metadata_obj,
    Column("label_alt_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_comp_id", String(10), primary_key=True),
    Column("label_seq_id", Integer, primary_key=True),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20)),
    Column("B_iso", Float),
    Column("B_iso_main_chain", Float),
    Column("B_iso_side_chain", Float),
    Column("shift", Float),
    Column("shift_side_chain", Float),
    Column("shift_main_chain", Float),
    Column("correlation", Float),
    Column("correlation_side_chain", Float),
    Column("correlation_main_chain", Float),
    Column("real_space_R", Float),
    Column("real_space_R_side_chain", Float),
    Column("real_space_R_main_chain", Float),
    Column("connect", Float),
    Column("density_index", Float),
    Column("density_index_main_chain", Float),
    Column("density_index_side_chain", Float),
    Column("density_ratio", Float),
    Column("density_ratio_main_chain", Float),
    Column("density_ratio_side_chain", Float)
)


pdbx_entity_prod_protocol = Table("pdbx_entity_prod_protocol",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("protocol", String(255), nullable=False),
    Column("protocol_type", String(20), primary_key=True)
)


pdbx_entity_src_gen_prod_other = Table("pdbx_entity_src_gen_prod_other",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("process_name", String(255)),
    Column("details", String(255))
)


pdbx_entity_src_gen_prod_other_parameter = Table("pdbx_entity_src_gen_prod_other_parameter",
    metadata_obj,
    Column("step_id", Integer, primary_key=True),
    Column("parameter", String(128), primary_key=True),
    Column("value", String(255), nullable=False),
    Column("details", String(255), nullable=False)
)


pdbx_entity_src_gen_prod_pcr = Table("pdbx_entity_src_gen_prod_pcr",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("forward_primer_id", String(20), nullable=False),
    Column("reverse_primer_id", String(20), nullable=False),
    Column("reaction_details", String(255)),
    Column("purification_details", String(255)),
    Column("summary", String(255))
)


pdbx_entity_src_gen_prod_digest = Table("pdbx_entity_src_gen_prod_digest",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("restriction_enzyme_1", String(255), nullable=False),
    Column("restriction_enzyme_2", String(255)),
    Column("purification_details", String(255)),
    Column("summary", String(255))
)


pdbx_entity_src_gen_clone = Table("pdbx_entity_src_gen_clone",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("gene_insert_method", String(20), nullable=False),
    Column("vector_name", String(255)),
    Column("vector_details", String(255)),
    Column("transformation_method", String(20)),
    Column("marker", String(20)),
    Column("verification_method", String(20)),
    Column("purification_details", String(255)),
    Column("summary", String(255))
)


pdbx_entity_src_gen_clone_ligation = Table("pdbx_entity_src_gen_clone_ligation",
    metadata_obj,
    Column("step_id", Integer, primary_key=True),
    Column("cleavage_enzymes", String(255), nullable=False),
    Column("ligation_enzymes", String(255), nullable=False),
    Column("temperature", Float, nullable=False),
    Column("time", Integer, nullable=False),
    Column("details", String(255))
)


pdbx_entity_src_gen_clone_recombination = Table("pdbx_entity_src_gen_clone_recombination",
    metadata_obj,
    Column("step_id", Integer, primary_key=True),
    Column("system", String(20), nullable=False),
    Column("recombination_enzymes", String(20), nullable=False),
    Column("details", String(255))
)


pdbx_entity_src_gen_express = Table("pdbx_entity_src_gen_express",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("promoter_type", String(255), nullable=False),
    Column("plasmid_id", String(20), nullable=False),
    Column("vector_type", String(20), nullable=False),
    Column("N_terminal_seq_tag", String(255), nullable=False),
    Column("C_terminal_seq_tag", String(255), nullable=False),
    Column("host_org_scientific_name", String(128)),
    Column("host_org_common_name", String(128)),
    Column("host_org_variant", String(128)),
    Column("host_org_strain", String(128)),
    Column("host_org_tissue", String(128)),
    Column("host_org_culture_collection", String(128)),
    Column("host_org_cell_line", String(128)),
    Column("host_org_tax_id", String(128)),
    Column("host_org_details", String(255)),
    Column("culture_base_media", String(255)),
    Column("culture_additives", String(255)),
    Column("culture_volume", Float, nullable=False),
    Column("culture_time", Float, nullable=False),
    Column("culture_temperature", Float, nullable=False),
    Column("inducer", String(128)),
    Column("inducer_concentration", Float),
    Column("induction_details", String(255)),
    Column("multiplicity_of_infection", Float),
    Column("induction_timepoint", Float),
    Column("induction_temperature", Float, nullable=False),
    Column("harvesting_details", String(255)),
    Column("storage_details", String(255)),
    Column("summary", String(255))
)


pdbx_entity_src_gen_express_timepoint = Table("pdbx_entity_src_gen_express_timepoint",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("serial", Integer, primary_key=True),
    Column("OD", Integer, nullable=False),
    Column("time", Integer, nullable=False)
)


pdbx_entity_src_gen_lysis = Table("pdbx_entity_src_gen_lysis",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("method", String(20), nullable=False),
    Column("buffer_id", String(20), nullable=False),
    Column("buffer_volume", Float, nullable=False),
    Column("temperature", Float, nullable=False),
    Column("time", Float, nullable=False),
    Column("details", String(255))
)


pdbx_entity_src_gen_refold = Table("pdbx_entity_src_gen_refold",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("denature_buffer_id", String(20), nullable=False),
    Column("refold_buffer_id", String(20), nullable=False),
    Column("temperature", Float, nullable=False),
    Column("time", Float, nullable=False),
    Column("storage_buffer_id", String(20), nullable=False),
    Column("details", String(255))
)


pdbx_entity_src_gen_proteolysis = Table("pdbx_entity_src_gen_proteolysis",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("details", String(255)),
    Column("protease", String(255), nullable=False),
    Column("protein_protease_ratio", Float),
    Column("cleavage_buffer_id", String(20)),
    Column("cleavage_temperature", Float),
    Column("cleavage_time", Float)
)


pdbx_entity_src_gen_chrom = Table("pdbx_entity_src_gen_chrom",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("column_type", String(255), nullable=False),
    Column("column_volume", Float, nullable=False),
    Column("column_temperature", Float, nullable=False),
    Column("equilibration_buffer_id", String(20), nullable=False),
    Column("flow_rate", Float),
    Column("elution_buffer_id", String(20), nullable=False),
    Column("elution_protocol", String(255)),
    Column("sample_prep_details", String(255)),
    Column("sample_volume", Float, nullable=False),
    Column("sample_concentration", Float),
    Column("sample_conc_method", String(255)),
    Column("volume_pooled_fractions", Float, nullable=False),
    Column("yield_pooled_fractions", Float, nullable=False),
    Column("yield_method", String(255), nullable=False),
    Column("post_treatment", String(255))
)


pdbx_entity_src_gen_fract = Table("pdbx_entity_src_gen_fract",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer, nullable=False),
    Column("end_construct_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("method", String(20), nullable=False),
    Column("temperature", Float, nullable=False),
    Column("details", String(255)),
    Column("protein_location", String(20), nullable=False),
    Column("protein_volume", Float),
    Column("protein_yield", Float, nullable=False),
    Column("protein_yield_method", String(255), nullable=False)
)


pdbx_entity_src_gen_pure = Table("pdbx_entity_src_gen_pure",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("product_id", String(20)),
    Column("date", Date),
    Column("conc_device_id", String(20)),
    Column("conc_details", String(255)),
    Column("conc_assay_method", String(255), nullable=False),
    Column("protein_concentration", Float, nullable=False),
    Column("protein_yield", Float),
    Column("protein_purity", Float),
    Column("protein_oligomeric_state", Integer),
    Column("storage_buffer_id", String(20), nullable=False),
    Column("storage_temperature", Float),
    Column("summary", String(255))
)


pdbx_entity_src_gen_character = Table("pdbx_entity_src_gen_character",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("method", String(255), nullable=False),
    Column("result", String(255), nullable=False),
    Column("details", String(255))
)


pdbx_construct = Table("pdbx_construct",
    metadata_obj,
    Column("entry_id", String(20), nullable=False),
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=False),
    Column("organisation", String(128), nullable=False),
    Column("entity_id", String(20)),
    Column("robot_id", String(20)),
    Column("date", Date),
    Column("details", String(255)),
    Column("class", String(20)),
    Column("type", String(20), nullable=False),
    Column("seq", String(255), nullable=False)
)


pdbx_construct_feature = Table("pdbx_construct_feature",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("construct_id", String(20), primary_key=True),
    Column("entry_id", String(20), nullable=False),
    Column("start_seq", Integer),
    Column("end_seq", Integer),
    Column("type", String(128)),
    Column("details", String(255))
)


pdbx_robot_system = Table("pdbx_robot_system",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("model", String(128)),
    Column("type", String(128)),
    Column("manufacturer", String(128))
)


pdbx_buffer = Table("pdbx_buffer",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("details", String(255))
)


pdbx_buffer_components = Table("pdbx_buffer_components",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("buffer_id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("volume", String(20)),
    Column("conc", String(20)),
    Column("details", String(255)),
    Column("conc_units", String(20)),
    Column("isotopic_labeling", String(128))
)


pdbx_domain = Table("pdbx_domain",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True)
)


pdbx_domain_range = Table("pdbx_domain_range",
    metadata_obj,
    Column("beg_label_alt_id", String(20), primary_key=True),
    Column("beg_label_asym_id", String(20), primary_key=True),
    Column("beg_label_comp_id", String(10), primary_key=True),
    Column("beg_label_seq_id", Integer, primary_key=True),
    Column("beg_auth_asym_id", String(20)),
    Column("beg_auth_comp_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("domain_id", String(20), primary_key=True),
    Column("end_label_alt_id", String(20), primary_key=True),
    Column("end_label_asym_id", String(20), primary_key=True),
    Column("end_label_comp_id", String(10), primary_key=True),
    Column("end_label_seq_id", Integer, primary_key=True),
    Column("end_auth_asym_id", String(20)),
    Column("end_auth_comp_id", String(20)),
    Column("end_auth_seq_id", String(20))
)


pdbx_sequence_range = Table("pdbx_sequence_range",
    metadata_obj,
    Column("beg_label_alt_id", String(20), primary_key=True),
    Column("beg_label_asym_id", String(20), primary_key=True),
    Column("beg_label_comp_id", String(10), primary_key=True),
    Column("beg_label_seq_id", Integer, primary_key=True),
    Column("beg_auth_asym_id", String(20)),
    Column("beg_auth_comp_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("seq_range_id", String(20), primary_key=True),
    Column("end_label_alt_id", String(20), primary_key=True),
    Column("end_label_asym_id", String(20), primary_key=True),
    Column("end_label_comp_id", String(10), primary_key=True),
    Column("end_label_seq_id", Integer, primary_key=True),
    Column("end_auth_asym_id", String(20)),
    Column("end_auth_comp_id", String(20)),
    Column("end_auth_seq_id", String(20))
)


pdbx_feature_entry = Table("pdbx_feature_entry",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("feature_name", String(255), nullable=False),
    Column("feature_type", String(255), nullable=False),
    Column("feature", String(255), nullable=False),
    Column("feature_identifier", String(255)),
    Column("feature_assigned_by", String(255), nullable=False),
    Column("feature_citation_id", String(20)),
    Column("feature_software_id", String(255))
)


pdbx_feature_domain = Table("pdbx_feature_domain",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("domain_id", String(20), nullable=False),
    Column("feature_name", String(255), nullable=False),
    Column("feature_type", String(255), nullable=False),
    Column("feature", String(255), nullable=False),
    Column("feature_identifier", String(255)),
    Column("feature_assigned_by", String(255), nullable=False),
    Column("feature_citation_id", String(20)),
    Column("feature_software_id", String(255))
)


pdbx_feature_sequence_range = Table("pdbx_feature_sequence_range",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("seq_range_id", String(20), nullable=False),
    Column("feature_name", String(255), nullable=False),
    Column("feature_type", String(255), nullable=False),
    Column("feature", String(255), nullable=False),
    Column("feature_identifier", String(255)),
    Column("feature_assigned_by", String(255), nullable=False),
    Column("feature_citation_id", String(20)),
    Column("feature_software_id", String(255))
)


pdbx_feature_assembly = Table("pdbx_feature_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(128), nullable=False),
    Column("feature_name", String(255), nullable=False),
    Column("feature_type", String(255), nullable=False),
    Column("feature", String(255), nullable=False),
    Column("feature_identifier", String(255)),
    Column("feature_assigned_by", String(255), nullable=False),
    Column("feature_citation_id", String(20)),
    Column("feature_software_id", String(255))
)


pdbx_feature_monomer = Table("pdbx_feature_monomer",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("feature_name", String(255), nullable=False),
    Column("feature_type", String(255), nullable=False),
    Column("feature", String(255), nullable=False),
    Column("feature_identifier", String(255)),
    Column("feature_assigned_by", String(255), nullable=False),
    Column("feature_citation_id", String(20)),
    Column("feature_software_id", String(255)),
    Column("label_alt_id", String(20), nullable=False),
    Column("label_asym_id", String(20), nullable=False),
    Column("label_comp_id", String(10), nullable=False),
    Column("label_seq_id", Integer, nullable=False),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20))
)


pdbx_exptl_pd = Table("pdbx_exptl_pd",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("spec_preparation_pH", Float),
    Column("spec_preparation_pH_range", String(128)),
    Column("spec_preparation", String(255))
)


pdbx_reflns_twin = Table("pdbx_reflns_twin",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("crystal_id", String(20), primary_key=True),
    Column("domain_id", String(20)),
    Column("type", String(128)),
    Column("operator", String(128), primary_key=True),
    Column("fraction", Float, nullable=False),
    Column("mean_I2_over_mean_I_square", Float),
    Column("mean_F_square_over_mean_F2", Float)
)


pdbx_struct_info = Table("pdbx_struct_info",
    metadata_obj,
    Column("type", String(128), primary_key=True),
    Column("value", String(255), primary_key=True),
    Column("details", String(255))
)


pdbx_re_refinement = Table("pdbx_re_refinement",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("citation_id", String(20), nullable=False),
    Column("details", String(20), nullable=False)
)


pdbx_struct_assembly_prop = Table("pdbx_struct_assembly_prop",
    metadata_obj,
    Column("biol_id", String(20), primary_key=True),
    Column("type", String(128), primary_key=True),
    Column("value", String(255), nullable=False),
    Column("details", String(255))
)


pdbx_struct_ref_seq_feature = Table("pdbx_struct_ref_seq_feature",
    metadata_obj,
    Column("feature_id", Integer, primary_key=True),
    Column("align_id", String(20), nullable=False),
    Column("type", String(255)),
    Column("details", String(255)),
    Column("pdb_strand_id", String(20)),
    Column("asym_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("end_auth_seq_id", String(20)),
    Column("beg_seq_num", String(20)),
    Column("end_seq_num", String(20)),
    Column("beg_auth_mon_id", String(20)),
    Column("end_auth_mon_id", String(20)),
    Column("beg_pdb_ins_code", String(20)),
    Column("end_pdb_ins_code", String(20))
)


pdbx_struct_ref_seq_feature_prop = Table("pdbx_struct_ref_seq_feature_prop",
    metadata_obj,
    Column("feature_id", Integer, primary_key=True),
    Column("property_id", Integer, primary_key=True),
    Column("type", String(255), nullable=False),
    Column("value", String(255), nullable=False),
    Column("details", String(255)),
    Column("beg_db_mon_id", String(20)),
    Column("end_db_mon_id", String(20)),
    Column("beg_db_seq_id", Integer),
    Column("end_db_seq_id", Integer)
)


pdbx_struct_chem_comp_diagnostics = Table("pdbx_struct_chem_comp_diagnostics",
    metadata_obj,
    Column("details", String(255)),
    Column("type", String(128)),
    Column("pdb_strand_id", String(20)),
    Column("asym_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("seq_num", Integer),
    Column("auth_comp_id", String(20)),
    Column("pdb_ins_code", String(20)),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_chem_comp_synonyms = Table("pdbx_chem_comp_synonyms",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("comp_id", String(10), primary_key=True),
    Column("provenance", String(128)),
    Column("type", String(128))
)


pdbx_chem_comp_feature = Table("pdbx_chem_comp_feature",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("type", String(128), primary_key=True),
    Column("support", String(255)),
    Column("value", String(255), primary_key=True),
    Column("source", String(128), primary_key=True)
)


pdbx_coordinate_model = Table("pdbx_coordinate_model",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("type", String(128), nullable=False)
)


pdbx_struct_chem_comp_feature = Table("pdbx_struct_chem_comp_feature",
    metadata_obj,
    Column("details", String(255)),
    Column("type", String(128)),
    Column("pdb_strand_id", String(20)),
    Column("asym_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("seq_num", Integer),
    Column("auth_comp_id", String(20)),
    Column("pdb_ins_code", String(20)),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_diffrn_reflns_shell = Table("pdbx_diffrn_reflns_shell",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("percent_possible_obs", Float),
    Column("Rmerge_I_obs", Float),
    Column("Rsym_value", Float),
    Column("chi_squared", Float),
    Column("redundancy", Float),
    Column("rejects", Integer),
    Column("number_obs", Integer)
)


pdbx_bond_distance_limits = Table("pdbx_bond_distance_limits",
    metadata_obj,
    Column("atom_type_1", String(20), primary_key=True),
    Column("atom_type_2", String(20), primary_key=True),
    Column("lower_limit", Float, nullable=False),
    Column("upper_limit", Float, nullable=False)
)


pdbx_soln_scatter = Table("pdbx_soln_scatter",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("type", String(20), nullable=False),
    Column("source_beamline", String(255)),
    Column("source_beamline_instrument", String(255)),
    Column("detector_type", String(255)),
    Column("detector_specific", String(255)),
    Column("source_type", String(255)),
    Column("source_class", String(255)),
    Column("num_time_frames", Integer),
    Column("sample_pH", Float),
    Column("temperature", Float),
    Column("concentration_range", String(128)),
    Column("buffer_name", String(128)),
    Column("mean_guiner_radius", Float),
    Column("mean_guiner_radius_esd", Float),
    Column("min_mean_cross_sectional_radii_gyration", Float),
    Column("min_mean_cross_sectional_radii_gyration_esd", Float),
    Column("max_mean_cross_sectional_radii_gyration", Float),
    Column("max_mean_cross_sectional_radii_gyration_esd", Float),
    Column("protein_length", String(128)),
    Column("data_reduction_software_list", String(255)),
    Column("data_analysis_software_list", String(255))
)


pdbx_soln_scatter_model = Table("pdbx_soln_scatter_model",
    metadata_obj,
    Column("scatter_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("method", String(255)),
    Column("software_list", String(255)),
    Column("software_author_list", String(255)),
    Column("entry_fitting_list", String(255)),
    Column("num_conformers_calculated", Integer),
    Column("num_conformers_submitted", Integer),
    Column("representative_conformer", Integer),
    Column("conformer_selection_criteria", String(255))
)


pdbx_chem_comp_descriptor = Table("pdbx_chem_comp_descriptor",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("descriptor", String(255), nullable=False),
    Column("type", String(50), primary_key=True),
    Column("program", String(128), primary_key=True),
    Column("program_version", String(128), primary_key=True),
    Column("ordinal", Integer)
)


pdbx_chem_comp_identifier = Table("pdbx_chem_comp_identifier",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("identifier", String(255), nullable=False),
    Column("type", String(128), primary_key=True),
    Column("program", String(128), primary_key=True),
    Column("program_version", String(128), primary_key=True),
    Column("ordinal", Integer)
)


pdbx_chem_comp_import = Table("pdbx_chem_comp_import",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True)
)


pdbx_chem_comp_atom_edit = Table("pdbx_chem_comp_atom_edit",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("comp_id", String(10), nullable=False),
    Column("edit_op", String(10), nullable=False),
    Column("atom_id", String(6), nullable=False),
    Column("edit_atom_id", String(6), nullable=False),
    Column("edit_atom_value", String(128))
)


pdbx_chem_comp_bond_edit = Table("pdbx_chem_comp_bond_edit",
    metadata_obj,
    Column("ordinal", Integer, nullable=False),
    Column("comp_id", String(10), primary_key=True),
    Column("edit_op", String(10), primary_key=True),
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("edit_bond_value", String(128))
)


pdbx_chem_comp_audit = Table("pdbx_chem_comp_audit",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20)),
    Column("processing_site", String(20)),
    Column("details", String(255)),
    Column("action_type", String(128), primary_key=True)
)


pdbx_validate_close_contact = Table("pdbx_validate_close_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("PDB_ins_code_1", String(20)),
    Column("PDB_ins_code_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_alt_id_2", String(20)),
    Column("symm_as_xyz_1", String(128), default="x,y,z"),
    Column("symm_as_xyz_2", String(128), default="x,y,z"),
    Column("dist", Float, nullable=False)
)


pdbx_validate_symm_contact = Table("pdbx_validate_symm_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("PDB_ins_code_1", String(20)),
    Column("PDB_ins_code_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_alt_id_2", String(20)),
    Column("site_symmetry_1", String(128), nullable=False, default="1555"),
    Column("site_symmetry_2", String(128), nullable=False, default="1555"),
    Column("dist", Float, nullable=False)
)


pdbx_validate_rmsd_bond = Table("pdbx_validate_rmsd_bond",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("PDB_ins_code_1", String(20)),
    Column("PDB_ins_code_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_alt_id_2", String(20)),
    Column("bond_deviation", Float, nullable=False),
    Column("bond_value", Float),
    Column("bond_target_value", Float),
    Column("bond_standard_deviation", Float),
    Column("linker_flag", String(50), default="N")
)


pdbx_validate_rmsd_angle = Table("pdbx_validate_rmsd_angle",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("auth_atom_id_3", String(6), nullable=False),
    Column("auth_asym_id_3", String(20), nullable=False),
    Column("auth_comp_id_3", String(20), nullable=False),
    Column("auth_seq_id_3", String(20), nullable=False),
    Column("PDB_ins_code_1", String(20)),
    Column("PDB_ins_code_2", String(20)),
    Column("PDB_ins_code_3", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_alt_id_2", String(20)),
    Column("label_alt_id_3", String(20)),
    Column("angle_deviation", Float, nullable=False),
    Column("angle_value", Float),
    Column("angle_target_value", Float),
    Column("angle_standard_deviation", Float),
    Column("linker_flag", String(50), default="N")
)


pdbx_validate_torsion = Table("pdbx_validate_torsion",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_alt_id", String(20)),
    Column("phi", Float, nullable=False),
    Column("psi", Float, nullable=False)
)


pdbx_validate_peptide_omega = Table("pdbx_validate_peptide_omega",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("PDB_ins_code_1", String(20)),
    Column("PDB_ins_code_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_alt_id_2", String(20)),
    Column("omega", Float, nullable=False)
)


pdbx_validate_chiral = Table("pdbx_validate_chiral",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_atom_id", String(6)),
    Column("label_alt_id", String(20)),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("omega", Float, nullable=False),
    Column("details", String(128))
)


pdbx_validate_planes = Table("pdbx_validate_planes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_alt_id", String(20)),
    Column("rmsd", Float, nullable=False),
    Column("type", String(50), nullable=False)
)


pdbx_validate_planes_atom = Table("pdbx_validate_planes_atom",
    metadata_obj,
    Column("plane_id", Integer, nullable=False),
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("auth_atom_id", String(6), nullable=False),
    Column("atom_deviation", Float, nullable=False)
)


pdbx_validate_main_chain_plane = Table("pdbx_validate_main_chain_plane",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_alt_id", String(20)),
    Column("improper_torsion_angle", Float, nullable=False)
)


pdbx_struct_conn_angle = Table("pdbx_struct_conn_angle",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("ptnr1_label_alt_id", String(20)),
    Column("ptnr1_label_asym_id", String(20), nullable=False),
    Column("ptnr1_label_atom_id", String(6), nullable=False),
    Column("ptnr1_label_comp_id", String(10), nullable=False),
    Column("ptnr1_label_seq_id", Integer),
    Column("ptnr1_auth_asym_id", String(20)),
    Column("ptnr1_auth_atom_id", String(6)),
    Column("ptnr1_auth_comp_id", String(20)),
    Column("ptnr1_auth_seq_id", String(20)),
    Column("ptnr1_symmetry", String(10)),
    Column("ptnr2_label_alt_id", String(20)),
    Column("ptnr2_label_asym_id", String(20), nullable=False),
    Column("ptnr2_label_atom_id", String(6), nullable=False),
    Column("ptnr2_label_comp_id", String(10), nullable=False),
    Column("ptnr2_label_seq_id", Integer),
    Column("ptnr2_auth_asym_id", String(20)),
    Column("ptnr2_auth_atom_id", String(6)),
    Column("ptnr2_auth_comp_id", String(20)),
    Column("ptnr2_auth_seq_id", String(20)),
    Column("ptnr2_symmetry", String(10)),
    Column("ptnr1_PDB_ins_code", String(20)),
    Column("ptnr1_auth_alt_id", String(20)),
    Column("ptnr2_PDB_ins_code", String(20)),
    Column("ptnr2_auth_alt_id", String(20)),
    Column("ptnr3_auth_alt_id", String(20)),
    Column("ptnr3_auth_asym_id", String(20)),
    Column("ptnr3_auth_atom_id", String(6)),
    Column("ptnr3_auth_comp_id", String(20)),
    Column("ptnr3_PDB_ins_code", String(20)),
    Column("ptnr3_auth_seq_id", String(20)),
    Column("ptnr3_label_alt_id", String(20)),
    Column("ptnr3_label_asym_id", String(20)),
    Column("ptnr3_label_atom_id", String(6)),
    Column("ptnr3_label_comp_id", String(10)),
    Column("ptnr3_label_seq_id", Integer),
    Column("ptnr3_symmetry", String(10)),
    Column("value", Float),
    Column("value_esd", Float)
)


pdbx_unobs_or_zero_occ_residues = Table("pdbx_unobs_or_zero_occ_residues",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("polymer_flag", String(10), nullable=False),
    Column("occupancy_flag", Integer, nullable=False),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(10), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer)
)


pdbx_unobs_or_zero_occ_atoms = Table("pdbx_unobs_or_zero_occ_atoms",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("polymer_flag", String(10), nullable=False),
    Column("occupancy_flag", Integer, nullable=False),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_atom_id", String(6), nullable=False),
    Column("auth_comp_id", String(10), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_alt_id", String(20)),
    Column("label_atom_id", String(6)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer)
)


pdbx_entry_details = Table("pdbx_entry_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("nonpolymer_details", String(255)),
    Column("sequence_details", String(255)),
    Column("compound_details", String(255)),
    Column("source_details", String(255)),
    Column("has_ligand_of_interest", String(10)),
    Column("has_protein_modification", String(20))
)


pdbx_struct_mod_residue = Table("pdbx_struct_mod_residue",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("parent_comp_id", String(20)),
    Column("details", String(255))
)


pdbx_struct_ref_seq_insertion = Table("pdbx_struct_ref_seq_insertion",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("comp_id", String(10), nullable=False),
    Column("asym_id", String(20), nullable=False),
    Column("auth_asym_id", String(20)),
    Column("auth_seq_id", String(20), nullable=False),
    Column("seq_id", Integer, nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("details", String(255)),
    Column("db_code", String(128), nullable=False),
    Column("db_name", String(128), nullable=False)
)


pdbx_struct_ref_seq_deletion = Table("pdbx_struct_ref_seq_deletion",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("asym_id", String(20), nullable=False),
    Column("comp_id", String(10), nullable=False),
    Column("db_seq_id", Integer, nullable=False),
    Column("db_code", String(128), nullable=False),
    Column("db_name", String(128), nullable=False)
)


pdbx_remediation_atom_site_mapping = Table("pdbx_remediation_atom_site_mapping",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("group_PDB", String(20)),
    Column("label_alt_id", String(20)),
    Column("label_asym_id", String(20), nullable=False),
    Column("label_atom_id", String(6), nullable=False),
    Column("label_comp_id", String(10), nullable=False),
    Column("label_seq_id", Integer, nullable=False),
    Column("pdbx_align", Integer),
    Column("PDB_ins_code", String(20)),
    Column("pre_auth_asym_id", String(20)),
    Column("pre_auth_atom_id", String(6)),
    Column("pre_auth_comp_id", String(20)),
    Column("pre_auth_seq_id", String(20)),
    Column("pre_PDB_ins_code", String(20)),
    Column("pre_group_PDB", String(20)),
    Column("pre_auth_alt_id", String(20)),
    Column("pre_pdbx_align", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_atom_id", String(6)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("auth_alt_id", String(20)),
    Column("occupancy", Float),
    Column("pre_occupancy", Float)
)


pdbx_validate_polymer_linkage = Table("pdbx_validate_polymer_linkage",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("PDB_ins_code_1", String(20)),
    Column("PDB_ins_code_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_alt_id_2", String(20)),
    Column("dist", Float, nullable=False)
)


pdbx_helical_symmetry = Table("pdbx_helical_symmetry",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("number_of_operations", Integer, nullable=False),
    Column("rotation_per_n_subunits", Float, nullable=False),
    Column("rise_per_n_subunits", Float, nullable=False),
    Column("n_subunits_divisor", Integer, nullable=False),
    Column("dyad_axis", String(20), nullable=False),
    Column("circular_symmetry", Integer, nullable=False)
)


pdbx_point_symmetry = Table("pdbx_point_symmetry",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("Schoenflies_symbol", String(20), nullable=False),
    Column("circular_symmetry", Integer),
    Column("H-M_notation", String(20))
)


pdbx_struct_entity_inst = Table("pdbx_struct_entity_inst",
    metadata_obj,
    Column("details", String(255)),
    Column("entity_id", String(20)),
    Column("id", String(20), primary_key=True)
)


pdbx_struct_oper_list = Table("pdbx_struct_oper_list",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(128), nullable=False),
    Column("name", String(128)),
    Column("symmetry_operation", String(128)),
    Column("matrix[1][1]", Float),
    Column("matrix[1][2]", Float),
    Column("matrix[1][3]", Float),
    Column("matrix[2][1]", Float),
    Column("matrix[2][2]", Float),
    Column("matrix[2][3]", Float),
    Column("matrix[3][1]", Float),
    Column("matrix[3][2]", Float),
    Column("matrix[3][3]", Float),
    Column("vector[1]", Float),
    Column("vector[2]", Float),
    Column("vector[3]", Float),
    Column("full_matrix", String(255))
)


pdbx_struct_assembly = Table("pdbx_struct_assembly",
    metadata_obj,
    Column("method_details", String(255)),
    Column("oligomeric_details", String(128)),
    Column("oligomeric_count", Integer),
    Column("details", String(255), nullable=False)
)


pdbx_struct_assembly_gen = Table("pdbx_struct_assembly_gen",
    metadata_obj,
    Column("entity_inst_id", String(20)),
    Column("asym_id_list", String(255)),
    Column("auth_asym_id_list", String(128)),
    Column("assembly_id", String(128)),
    Column("oper_expression", String(511))
)


pdbx_struct_asym_gen = Table("pdbx_struct_asym_gen",
    metadata_obj,
    Column("entity_inst_id", String(20), primary_key=True),
    Column("asym_id", String(20)),
    Column("oper_expression", String(511), primary_key=True)
)


pdbx_struct_msym_gen = Table("pdbx_struct_msym_gen",
    metadata_obj,
    Column("entity_inst_id", String(20), primary_key=True),
    Column("msym_id", String(20), primary_key=True),
    Column("oper_expression", String(511), primary_key=True)
)


pdbx_struct_legacy_oper_list = Table("pdbx_struct_legacy_oper_list",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(128)),
    Column("matrix[1][1]", Float),
    Column("matrix[1][2]", Float),
    Column("matrix[1][3]", Float),
    Column("matrix[2][1]", Float),
    Column("matrix[2][2]", Float),
    Column("matrix[2][3]", Float),
    Column("matrix[3][1]", Float),
    Column("matrix[3][2]", Float),
    Column("matrix[3][3]", Float),
    Column("vector[1]", Float),
    Column("vector[2]", Float),
    Column("vector[3]", Float)
)


pdbx_chem_comp_atom_feature = Table("pdbx_chem_comp_atom_feature",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("atom_id", String(6), primary_key=True),
    Column("feature_type", String(10), primary_key=True)
)


pdbx_reference_molecule_family = Table("pdbx_reference_molecule_family",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("name", String(255)),
    Column("release_status", String(50)),
    Column("replaces", String(50)),
    Column("replaced_by", String(50))
)


pdbx_reference_molecule_list = Table("pdbx_reference_molecule_list",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("family_prd_id", String(10), primary_key=True)
)


pdbx_reference_molecule = Table("pdbx_reference_molecule",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("formula_weight", Float),
    Column("formula", String(255)),
    Column("type", String(50)),
    Column("type_evidence_code", String(255)),
    Column("class", String(50)),
    Column("class_evidence_code", String(255)),
    Column("name", String(255)),
    Column("represent_as", String(50)),
    Column("chem_comp_id", String(10)),
    Column("compound_details", String(255)),
    Column("description", String(255)),
    Column("representative_PDB_id_code", String(10)),
    Column("release_status", String(50)),
    Column("replaces", String(50)),
    Column("replaced_by", String(50))
)


pdbx_reference_entity_list = Table("pdbx_reference_entity_list",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("type", String(50)),
    Column("details", String(255)),
    Column("component_id", Integer, primary_key=True)
)


pdbx_reference_entity_nonpoly = Table("pdbx_reference_entity_nonpoly",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("details", String(255)),
    Column("name", String(255)),
    Column("chem_comp_id", String(10))
)


pdbx_reference_entity_link = Table("pdbx_reference_entity_link",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("details", String(255)),
    Column("ref_entity_id_1", String(10), nullable=False),
    Column("ref_entity_id_2", String(10), nullable=False),
    Column("entity_seq_num_1", Integer),
    Column("entity_seq_num_2", Integer),
    Column("comp_id_1", String(20), nullable=False),
    Column("comp_id_2", String(20), nullable=False),
    Column("atom_id_1", String(6), nullable=False),
    Column("atom_id_2", String(20), nullable=False),
    Column("value_order", String(10), default="sing"),
    Column("component_1", Integer, nullable=False),
    Column("component_2", Integer, nullable=False),
    Column("nonpoly_res_num_1", String(20)),
    Column("nonpoly_res_num_2", String(20)),
    Column("link_class", String(20))
)


pdbx_reference_entity_poly_link = Table("pdbx_reference_entity_poly_link",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("details", String(255)),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("component_id", Integer, primary_key=True),
    Column("entity_seq_num_1", Integer),
    Column("entity_seq_num_2", Integer),
    Column("comp_id_1", String(20), nullable=False),
    Column("comp_id_2", String(20), nullable=False),
    Column("atom_id_1", String(6), nullable=False),
    Column("atom_id_2", String(20), nullable=False),
    Column("insert_code_1", String(20)),
    Column("insert_code_2", String(20)),
    Column("value_order", String(10), default="sing")
)


pdbx_reference_entity_poly = Table("pdbx_reference_entity_poly",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("type", String(128)),
    Column("db_code", String(255)),
    Column("db_name", String(255))
)


pdbx_reference_entity_poly_seq = Table("pdbx_reference_entity_poly_seq",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("mon_id", String(20), primary_key=True),
    Column("parent_mon_id", String(20)),
    Column("num", Integer, primary_key=True),
    Column("observed", String(10), default="Y"),
    Column("hetero", String(10), primary_key=True, default="N")
)


pdbx_reference_entity_sequence = Table("pdbx_reference_entity_sequence",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("type", String(128), nullable=False),
    Column("NRP_flag", String(20), nullable=False),
    Column("one_letter_codes", String(128))
)


pdbx_reference_entity_src_nat = Table("pdbx_reference_entity_src_nat",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("organism_scientific", String(255)),
    Column("strain", String(255)),
    Column("taxid", String(255)),
    Column("atcc", String(255)),
    Column("db_code", String(255)),
    Column("db_name", String(255)),
    Column("source", String(255)),
    Column("source_id", String(255))
)


pdbx_reference_molecule_details = Table("pdbx_reference_molecule_details",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10)),
    Column("ordinal", Integer, primary_key=True),
    Column("source", String(255)),
    Column("source_id", String(255)),
    Column("text", String(255), nullable=False)
)


pdbx_reference_molecule_synonyms = Table("pdbx_reference_molecule_synonyms",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("source", String(255), nullable=False),
    Column("chem_comp_id", String(10))
)


pdbx_reference_entity_subcomponents = Table("pdbx_reference_entity_subcomponents",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("seq", String(255), primary_key=True),
    Column("chem_comp_id", String(10))
)


pdbx_reference_molecule_annotation = Table("pdbx_reference_molecule_annotation",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10)),
    Column("ordinal", Integer, primary_key=True),
    Column("text", String(255), nullable=False),
    Column("type", String(128), nullable=False),
    Column("support", String(255)),
    Column("source", String(255), nullable=False),
    Column("chem_comp_id", String(10))
)


pdbx_reference_molecule_features = Table("pdbx_reference_molecule_features",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("source_ordinal", Integer),
    Column("type", String(128), nullable=False),
    Column("value", String(255), nullable=False),
    Column("source", String(128), nullable=False),
    Column("chem_comp_id", String(10))
)


pdbx_reference_molecule_related_structures = Table("pdbx_reference_molecule_related_structures",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("db_name", String(255)),
    Column("db_code", String(255)),
    Column("db_accession", String(255)),
    Column("name", String(255)),
    Column("formula", String(255)),
    Column("citation_id", String(20))
)


pdbx_struct_group_list = Table("pdbx_struct_group_list",
    metadata_obj,
    Column("struct_group_id", String(10), primary_key=True),
    Column("name", String(128), nullable=False),
    Column("type", String(128), nullable=False),
    Column("group_enumeration_type", String(25), nullable=False),
    Column("description", String(255), nullable=False),
    Column("selection", String(128)),
    Column("selection_details", String(255))
)


pdbx_struct_group_components = Table("pdbx_struct_group_components",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("struct_group_id", String(10), nullable=False),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("label_alt_id", String(20))
)


pdbx_struct_group_component_range = Table("pdbx_struct_group_component_range",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("struct_group_id", String(10), nullable=False),
    Column("PDB_model_num", Integer),
    Column("beg_auth_asym_id", String(20), nullable=False),
    Column("beg_auth_comp_id", String(20), nullable=False),
    Column("beg_auth_seq_id", String(20), nullable=False),
    Column("beg_PDB_ins_code", String(20)),
    Column("beg_label_asym_id", String(20)),
    Column("beg_label_comp_id", String(10)),
    Column("beg_label_seq_id", Integer),
    Column("beg_label_alt_id", String(20)),
    Column("end_auth_asym_id", String(20), nullable=False),
    Column("end_auth_comp_id", String(20), nullable=False),
    Column("end_auth_seq_id", String(20), nullable=False),
    Column("end_PDB_ins_code", String(20)),
    Column("end_label_asym_id", String(20)),
    Column("end_label_comp_id", String(10)),
    Column("end_label_seq_id", Integer),
    Column("end_label_alt_id", String(20))
)


pdbx_prd_audit = Table("pdbx_prd_audit",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20)),
    Column("processing_site", String(20)),
    Column("details", String(255)),
    Column("action_type", String(128), primary_key=True)
)


pdbx_family_prd_audit = Table("pdbx_family_prd_audit",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20)),
    Column("processing_site", String(20)),
    Column("details", String(255)),
    Column("action_type", String(128), primary_key=True)
)


pdbx_molecule = Table("pdbx_molecule",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("instance_id", Integer, primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("linked_entity_id", String(20))
)


pdbx_molecule_features = Table("pdbx_molecule_features",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("class", String(50)),
    Column("type", String(50)),
    Column("name", String(255)),
    Column("details", String(255))
)


pdbx_family_group_index = Table("pdbx_family_group_index",
    metadata_obj,
    Column("id", String(10), primary_key=True),
    Column("family_prd_id", String(10), primary_key=True)
)


pdbx_distant_solvent_atoms = Table("pdbx_distant_solvent_atoms",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_atom_id", String(6), nullable=False),
    Column("auth_comp_id", String(10), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_alt_id", String(20)),
    Column("label_atom_id", String(6)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("neighbor_macromolecule_distance", Float),
    Column("neighbor_ligand_distance", Float)
)


pdbx_struct_special_symmetry = Table("pdbx_struct_special_symmetry",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(10), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("label_alt_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer)
)


pdbx_reference_publication_list = Table("pdbx_reference_publication_list",
    metadata_obj,
    Column("publication_abbrev", String(128), primary_key=True),
    Column("ASTM_code_type", String(128)),
    Column("ASTM_code_value", String(128)),
    Column("ISSN_code_type", String(128)),
    Column("ISSN_code_value", String(128)),
    Column("country", String(128)),
    Column("start_year", String(128)),
    Column("end_year", String(128))
)


pdbx_nmr_assigned_chem_shift_list = Table("pdbx_nmr_assigned_chem_shift_list",
    metadata_obj,
    Column("chem_shift_13C_err", Float),
    Column("chem_shift_15N_err", Float),
    Column("chem_shift_19F_err", Float),
    Column("chem_shift_1H_err", Float),
    Column("chem_shift_2H_err", Float),
    Column("chem_shift_31P_err", Float),
    Column("chem_shift_reference_id", Integer, nullable=False),
    Column("conditions_id", Integer, nullable=False),
    Column("data_file_name", String(128), nullable=False),
    Column("details", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("error_derivation_method", String(255)),
    Column("label", String(128)),
    Column("conditions_label", String(128))
)


pdbx_nmr_chem_shift_experiment = Table("pdbx_nmr_chem_shift_experiment",
    metadata_obj,
    Column("assigned_chem_shift_list_id", Integer, primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("experiment_id", Integer, primary_key=True),
    Column("experiment_name", String(128)),
    Column("sample_state", String(128)),
    Column("solution_id", Integer)
)


pdbx_nmr_chem_shift_ref = Table("pdbx_nmr_chem_shift_ref",
    metadata_obj,
    Column("atom_group", String(128), nullable=False),
    Column("atom_isotope_number", Integer, primary_key=True),
    Column("atom_type", String(20), primary_key=True),
    Column("chem_shift_reference_id", Integer, primary_key=True),
    Column("chem_shift_units", String(128), nullable=False),
    Column("chem_shift_val", Float, nullable=False),
    Column("correction_val", Float),
    Column("entry_id", String(20), primary_key=True),
    Column("external_ref_axis", String(128)),
    Column("external_ref_loc", String(128)),
    Column("external_ref_sample_geometry", String(128)),
    Column("indirect_shift_ratio", Float, default=1.0),
    Column("mol_common_name", String(128), primary_key=True),
    Column("rank", String(20)),
    Column("ref_correction_type", String(128)),
    Column("ref_method", String(128)),
    Column("ref_type", String(128)),
    Column("solvent", String(128))
)


pdbx_nmr_chem_shift_reference = Table("pdbx_nmr_chem_shift_reference",
    metadata_obj,
    Column("carbon_shifts_flag", String(128)),
    Column("details", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("id", Integer, primary_key=True),
    Column("label", String(128), nullable=False, default="chemical_shift_reference_1"),
    Column("nitrogen_shifts_flag", String(128)),
    Column("other_shifts_flag", String(128), default="no"),
    Column("phosphorus_shifts_flag", String(128), default="no"),
    Column("proton_shifts_flag", String(128))
)


pdbx_nmr_chem_shift_software = Table("pdbx_nmr_chem_shift_software",
    metadata_obj,
    Column("assigned_chem_shift_list_id", Integer, primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("software_id", Integer, primary_key=True),
    Column("software_label", String(20))
)


pdbx_nmr_constraint_file = Table("pdbx_nmr_constraint_file",
    metadata_obj,
    Column("constraint_filename", String(128), primary_key=True),
    Column("constraint_number", Integer),
    Column("constraint_subtype", String(128), primary_key=True),
    Column("constraint_type", String(128), primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("id", Integer),
    Column("software_name", String(128)),
    Column("software_ordinal", Integer)
)


pdbx_nmr_software_task = Table("pdbx_nmr_software_task",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("software_ordinal", Integer, primary_key=True),
    Column("task", String(128), primary_key=True)
)


pdbx_nmr_spectral_dim = Table("pdbx_nmr_spectral_dim",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("atom_type", String(20), primary_key=True),
    Column("atom_isotope_number", Integer, nullable=False),
    Column("spectral_region", String(20), primary_key=True),
    Column("magnetization_linkage_id", Integer),
    Column("sweep_width", Float),
    Column("encoding_code", String(128)),
    Column("encoded_source_dimension_id", Integer),
    Column("entry_id", String(20), primary_key=True),
    Column("spectral_peak_list_id", Integer, primary_key=True),
    Column("sweep_width_units", String(20), nullable=False),
    Column("center_frequency_offset", Float, nullable=False),
    Column("under_sampling_type", String(128), nullable=False)
)


pdbx_nmr_spectral_peak_list = Table("pdbx_nmr_spectral_peak_list",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("data_file_name", String(128)),
    Column("solution_id", Integer, nullable=False),
    Column("conditions_id", Integer, nullable=False),
    Column("experiment_id", Integer, nullable=False),
    Column("number_of_spectral_dimensions", Integer, nullable=False),
    Column("details", String(255)),
    Column("text_data_format", String(128)),
    Column("label", String(128)),
    Column("conditions_label", String(128))
)


pdbx_nmr_spectral_peak_software = Table("pdbx_nmr_spectral_peak_software",
    metadata_obj,
    Column("software_id", Integer, primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("spectral_peak_list_id", Integer, primary_key=True)
)


pdbx_nmr_systematic_chem_shift_offset = Table("pdbx_nmr_systematic_chem_shift_offset",
    metadata_obj,
    Column("type", String(128)),
    Column("atom_type", String(128)),
    Column("atom_isotope_number", Integer),
    Column("val", Float),
    Column("val_err", Float),
    Column("entry_id", String(20), nullable=False),
    Column("assigned_chem_shift_list_id", Integer, nullable=False),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_nmr_upload = Table("pdbx_nmr_upload",
    metadata_obj,
    Column("data_file_id", Integer, primary_key=True),
    Column("data_file_name", String(128), nullable=False),
    Column("data_file_category", String(128), nullable=False),
    Column("data_file_syntax", String(128)),
    Column("entry_id", String(20), primary_key=True)
)


pdbx_chem_comp_subcomponent_struct_conn = Table("pdbx_chem_comp_subcomponent_struct_conn",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("type", String(10), nullable=False),
    Column("entity_id_1", Integer, nullable=False),
    Column("entity_id_2", Integer, nullable=False),
    Column("atom_id_1", String(6), nullable=False),
    Column("atom_id_2", String(6), nullable=False),
    Column("comp_id_1", String(10), nullable=False),
    Column("comp_id_2", String(10), nullable=False),
    Column("seq_id_1", Integer, nullable=False),
    Column("seq_id_2", Integer, nullable=False)
)


pdbx_chem_comp_subcomponent_entity_list = Table("pdbx_chem_comp_subcomponent_entity_list",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("parent_comp_id", String(10), nullable=False),
    Column("type", String(50), nullable=False),
    Column("class", String(10), nullable=False)
)


entity_src_nat = Table("entity_src_nat",
    metadata_obj,
    Column("common_name", String(255)),
    Column("details", String(255)),
    Column("entity_id", String(20), primary_key=True),
    Column("genus", String(255)),
    Column("species", String(255)),
    Column("strain", String(255)),
    Column("tissue", String(255)),
    Column("tissue_fraction", String(255)),
    Column("pdbx_organism_scientific", String(255)),
    Column("pdbx_secretion", String(255)),
    Column("pdbx_fragment", String(255)),
    Column("pdbx_variant", String(255)),
    Column("pdbx_cell_line", String(255)),
    Column("pdbx_atcc", String(255)),
    Column("pdbx_cellular_location", String(255)),
    Column("pdbx_organ", String(255)),
    Column("pdbx_organelle", String(255)),
    Column("pdbx_cell", String(255)),
    Column("pdbx_plasmid_name", String(255)),
    Column("pdbx_plasmid_details", String(255)),
    Column("pdbx_ncbi_taxonomy_id", String(128)),
    Column("pdbx_src_id", Integer, primary_key=True, default=1),
    Column("pdbx_alt_source_flag", String(20), default="sample"),
    Column("pdbx_beg_seq_num", Integer),
    Column("pdbx_end_seq_num", Integer),
    Column("pdbx_culture_collection", String(255))
)


entity_src_gen = Table("entity_src_gen",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("gene_src_common_name", String(255)),
    Column("gene_src_details", String(255)),
    Column("gene_src_genus", String(255)),
    Column("gene_src_species", String(255)),
    Column("gene_src_strain", String(255)),
    Column("gene_src_tissue", String(255)),
    Column("gene_src_tissue_fraction", String(255)),
    Column("host_org_genus", String(255)),
    Column("host_org_species", String(255)),
    Column("pdbx_gene_src_fragment", String(255)),
    Column("pdbx_gene_src_gene", String(255)),
    Column("pdbx_gene_src_scientific_name", String(255)),
    Column("pdbx_gene_src_variant", String(255)),
    Column("pdbx_gene_src_cell_line", String(255)),
    Column("pdbx_gene_src_atcc", String(255)),
    Column("pdbx_gene_src_organ", String(255)),
    Column("pdbx_gene_src_organelle", String(255)),
    Column("pdbx_gene_src_plasmid", String(255)),
    Column("pdbx_gene_src_plasmid_name", String(255)),
    Column("pdbx_gene_src_cell", String(255)),
    Column("pdbx_gene_src_cellular_location", String(255)),
    Column("pdbx_host_org_gene", String(255)),
    Column("pdbx_host_org_organ", String(255)),
    Column("pdbx_host_org_organelle", String(255)),
    Column("pdbx_host_org_cellular_location", String(255)),
    Column("pdbx_host_org_strain", String(255)),
    Column("pdbx_host_org_tissue_fraction", String(255)),
    Column("pdbx_description", String(255)),
    Column("host_org_common_name", String(255)),
    Column("host_org_details", String(255)),
    Column("host_org_strain", String(255)),
    Column("plasmid_details", String(255)),
    Column("plasmid_name", String(255)),
    Column("pdbx_host_org_variant", String(255)),
    Column("pdbx_host_org_cell_line", String(255)),
    Column("pdbx_host_org_atcc", String(255)),
    Column("pdbx_host_org_culture_collection", String(255)),
    Column("pdbx_host_org_cell", String(255)),
    Column("pdbx_host_org_scientific_name", String(255)),
    Column("pdbx_host_org_tissue", String(255)),
    Column("pdbx_host_org_vector", String(255)),
    Column("pdbx_host_org_vector_type", String(255)),
    Column("expression_system_id", String(50)),
    Column("gene_src_dev_stage", String(255)),
    Column("start_construct_id", String(20)),
    Column("pdbx_gene_src_ncbi_taxonomy_id", String(128)),
    Column("pdbx_host_org_ncbi_taxonomy_id", String(128)),
    Column("pdbx_src_id", Integer, primary_key=True, default=1),
    Column("pdbx_alt_source_flag", String(20), default="sample"),
    Column("pdbx_seq_type", String(128)),
    Column("pdbx_beg_seq_num", Integer),
    Column("pdbx_end_seq_num", Integer),
    Column("pdbx_gene_src_culture_collection", String(255))
)


pdbx_entity_src_syn = Table("pdbx_entity_src_syn",
    metadata_obj,
    Column("details", String(255)),
    Column("organism_scientific", String(255)),
    Column("organism_common_name", String(255)),
    Column("strain", String(255)),
    Column("ncbi_taxonomy_id", String(128)),
    Column("entity_id", String(20), primary_key=True),
    Column("pdbx_src_id", Integer, primary_key=True, default=1),
    Column("pdbx_alt_source_flag", String(20), default="sample"),
    Column("pdbx_beg_seq_num", Integer),
    Column("pdbx_end_seq_num", Integer)
)


pdbx_entity_poly_comp_link_list = Table("pdbx_entity_poly_comp_link_list",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("details", String(255)),
    Column("entity_id", String(20), nullable=False),
    Column("entity_comp_num_1", Integer, nullable=False),
    Column("entity_comp_num_2", Integer, nullable=False),
    Column("comp_id_1", String(10), nullable=False),
    Column("comp_id_2", String(10), nullable=False),
    Column("atom_id_1", String(6), nullable=False),
    Column("leaving_atom_id_1", String(6), nullable=False),
    Column("atom_stereo_config_1", String(10), default="N"),
    Column("atom_id_2", String(6), nullable=False),
    Column("leaving_atom_id_2", String(6), nullable=False),
    Column("atom_stereo_config_2", String(10), default="N"),
    Column("value_order", String(10), default="sing")
)


pdbx_linked_entity = Table("pdbx_linked_entity",
    metadata_obj,
    Column("linked_entity_id", String(10), primary_key=True),
    Column("type", String(50)),
    Column("class", String(255)),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("prd_id", String(10))
)


pdbx_linked_entity_instance_list = Table("pdbx_linked_entity_instance_list",
    metadata_obj,
    Column("linked_entity_id", String(10), primary_key=True),
    Column("instance_id", Integer, primary_key=True),
    Column("asym_id", String(20), primary_key=True)
)


pdbx_linked_entity_list = Table("pdbx_linked_entity_list",
    metadata_obj,
    Column("linked_entity_id", String(10), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("component_id", Integer, primary_key=True),
    Column("details", String(255))
)


pdbx_linked_entity_link_list = Table("pdbx_linked_entity_link_list",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("linked_entity_id", String(10), primary_key=True),
    Column("details", String(255)),
    Column("entity_id_1", String(20), nullable=False),
    Column("entity_id_2", String(20), nullable=False),
    Column("entity_seq_num_1", Integer),
    Column("entity_seq_num_2", Integer),
    Column("comp_id_1", String(20), nullable=False),
    Column("comp_id_2", String(20), nullable=False),
    Column("atom_id_1", String(6), nullable=False),
    Column("atom_id_2", String(6), nullable=False),
    Column("value_order", String(10), default="sing"),
    Column("component_1", Integer, nullable=False),
    Column("component_2", Integer, nullable=False),
    Column("link_class", String(20))
)


pdbx_entity_branch_descriptor = Table("pdbx_entity_branch_descriptor",
    metadata_obj,
    Column("entity_id", String(20), nullable=False),
    Column("descriptor", String(255), nullable=False),
    Column("type", String(50), nullable=False),
    Column("program", String(128)),
    Column("program_version", String(128)),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_reference_linked_entity = Table("pdbx_reference_linked_entity",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("class", String(255)),
    Column("name", String(255)),
    Column("taxonomy_id", String(255)),
    Column("taxonomy_class", String(255)),
    Column("link_to_entity_type", String(128)),
    Column("link_to_comp_id", String(10)),
    Column("link_from_entity_type", String(128))
)


pdbx_reference_linked_entity_comp_list = Table("pdbx_reference_linked_entity_comp_list",
    metadata_obj,
    Column("linked_entity_id", Integer, primary_key=True),
    Column("list_id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("comp_id", String(10))
)


pdbx_reference_linked_entity_comp_link = Table("pdbx_reference_linked_entity_comp_link",
    metadata_obj,
    Column("linked_entity_id", Integer, primary_key=True),
    Column("link_id", Integer, primary_key=True),
    Column("list_id_1", Integer, nullable=False),
    Column("list_id_2", Integer, nullable=False),
    Column("details", String(255)),
    Column("comp_id_1", String(20), nullable=False),
    Column("comp_id_2", String(20), nullable=False),
    Column("atom_id_1", String(6), nullable=False),
    Column("atom_id_2", String(6), nullable=False),
    Column("leaving_atom_id_1", String(6), nullable=False),
    Column("atom_stereo_config_1", String(10), default="N"),
    Column("leaving_atom_id_2", String(6), nullable=False),
    Column("atom_stereo_config_2", String(10), default="N"),
    Column("value_order", String(10), default="sing")
)


pdbx_reference_linked_entity_link = Table("pdbx_reference_linked_entity_link",
    metadata_obj,
    Column("linked_entity_id", Integer, primary_key=True),
    Column("link_id", Integer, primary_key=True),
    Column("from_list_id", Integer, nullable=False),
    Column("details", String(255)),
    Column("to_comp_id", String(20), nullable=False),
    Column("from_comp_id", String(20), nullable=False),
    Column("to_atom_id", String(6), nullable=False),
    Column("from_atom_id", String(6), nullable=False),
    Column("from_leaving_atom_id", String(6), nullable=False),
    Column("from_atom_stereo_config", String(10), default="N"),
    Column("value_order", String(10), default="sing")
)


pdbx_related_exp_data_set = Table("pdbx_related_exp_data_set",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("data_reference", String(80), nullable=False),
    Column("metadata_reference", String(80)),
    Column("data_set_type", String(128), nullable=False),
    Column("details", String(255))
)


pdbx_database_status_history = Table("pdbx_database_status_history",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("ordinal", String(20), primary_key=True),
    Column("date_begin", Date, nullable=False),
    Column("date_end", Date),
    Column("status_code", String(20), nullable=False),
    Column("details", String(255))
)


em_assembly = Table("em_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("name", String(255)),
    Column("aggregation_state", String(128)),
    Column("composition", String(255)),
    Column("num_components", Integer),
    Column("mol_wt_exp", Float),
    Column("mol_wt_theo", Float),
    Column("mol_wt_method", String(255)),
    Column("details", String(255))
)


em_entity_assembly = Table("em_entity_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(20)),
    Column("parent_id", Integer, nullable=False),
    Column("source", String(128)),
    Column("type", String(128)),
    Column("name", String(255), nullable=False),
    Column("details", String(255)),
    Column("go_id", String(128)),
    Column("ipr_id", String(128)),
    Column("synonym", String(128)),
    Column("number_of_copies", Integer),
    Column("oligomeric_details", String(255)),
    Column("entity_id_list", String(128)),
    Column("ebi_organism_scientific", String(128)),
    Column("ebi_organism_common", String(255)),
    Column("ebi_strain", String(255)),
    Column("ebi_tissue", String(255)),
    Column("ebi_cell", String(255)),
    Column("ebi_organelle", String(255)),
    Column("ebi_cellular_location", String(255)),
    Column("ebi_engineered", String(128)),
    Column("ebi_expression_system", String(128)),
    Column("ebi_expression_system_plasmid", String(128)),
    Column("mutant_flag", String(128)),
    Column("chimera", String(128))
)


em_virus_entity = Table("em_virus_entity",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("virus_host_category", String(128)),
    Column("virus_host_species", String(128)),
    Column("virus_host_growth_cell", String(128)),
    Column("virus_type", String(128)),
    Column("virus_isolate", String(128)),
    Column("ictvdb_id", String(128)),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("enveloped", String(20)),
    Column("empty", String(20)),
    Column("details", String(255))
)


em_sample_preparation = Table("em_sample_preparation",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ph", Float),
    Column("buffer_id", String(20)),
    Column("sample_concentration", Float),
    Column("2d_crystal_grow_id", String(20)),
    Column("support_id", String(20)),
    Column("entity_assembly_id", String(20)),
    Column("details", String(255))
)


em_sample_support = Table("em_sample_support",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("film_material", String(128)),
    Column("method", String(255)),
    Column("grid_material", String(128)),
    Column("grid_mesh_size", Integer),
    Column("grid_type", String(128)),
    Column("pretreatment", String(255)),
    Column("details", String(255)),
    Column("specimen_id", String(20), primary_key=True),
    Column("citation_id", String(20))
)


em_buffer = Table("em_buffer",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("specimen_id", String(20), primary_key=True),
    Column("name", String(255)),
    Column("details", String(255)),
    Column("pH", Float)
)


em_vitrification = Table("em_vitrification",
    metadata_obj,
    Column("entry_id", String(20), nullable=False),
    Column("id", String(20), primary_key=True),
    Column("sample_preparation_id", String(20)),
    Column("specimen_id", String(20), primary_key=True),
    Column("cryogen_name", String(128)),
    Column("humidity", Float),
    Column("temp", Float),
    Column("chamber_temperature", Float),
    Column("instrument", String(128)),
    Column("method", String(255)),
    Column("time_resolved_state", String(255)),
    Column("citation_id", String(20)),
    Column("details", String(255))
)


em_imaging = Table("em_imaging",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("astigmatism", String(255)),
    Column("electron_beam_tilt_params", String(255)),
    Column("residual_tilt", Float),
    Column("sample_support_id", String(20)),
    Column("detector_id", String(20)),
    Column("scans_id", String(20)),
    Column("microscope_id", String(20)),
    Column("microscope_model", String(128), nullable=False),
    Column("specimen_holder_type", String(255)),
    Column("specimen_holder_model", String(128)),
    Column("details", String(255)),
    Column("date", DateTime),
    Column("accelerating_voltage", Integer),
    Column("illumination_mode", String(128), nullable=False),
    Column("mode", String(128), nullable=False),
    Column("nominal_cs", Float),
    Column("nominal_defocus_min", Float),
    Column("nominal_defocus_max", Float),
    Column("calibrated_defocus_min", Float),
    Column("calibrated_defocus_max", Float),
    Column("tilt_angle_min", Float),
    Column("tilt_angle_max", Float),
    Column("nominal_magnification", Integer),
    Column("calibrated_magnification", Integer),
    Column("electron_source", String(128)),
    Column("electron_dose", Float),
    Column("energy_filter", String(128)),
    Column("energy_window", String(128)),
    Column("citation_id", String(20)),
    Column("temperature", Float),
    Column("detector_distance", Float),
    Column("recording_temperature_minimum", Float),
    Column("recording_temperature_maximum", Float),
    Column("alignment_procedure", String(128)),
    Column("c2_aperture_diameter", Float),
    Column("specimen_id", String(20), nullable=False),
    Column("cryogen", String(255))
)


em_detector = Table("em_detector",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("type", String(128)),
    Column("detective_quantum_efficiency", Float),
    Column("mode", String(128))
)


em_image_scans = Table("em_image_scans",
    metadata_obj,
    Column("entry_id", String(20), nullable=False),
    Column("id", String(20), primary_key=True),
    Column("number_digital_images", Integer),
    Column("details", String(255)),
    Column("scanner_model", String(128)),
    Column("sampling_size", Float),
    Column("od_range", Float),
    Column("quant_bit_size", Integer),
    Column("citation_id", String(20)),
    Column("dimension_height", Integer),
    Column("dimension_width", Integer),
    Column("frames_per_image", Integer),
    Column("image_recording_id", String(20), primary_key=True),
    Column("used_frames_per_image", String(20))
)


em_2d_projection_selection = Table("em_2d_projection_selection",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), nullable=False),
    Column("num_particles", Integer),
    Column("software_name", String(128)),
    Column("method", String(255)),
    Column("details", String(255)),
    Column("citation_id", String(20))
)


em_3d_reconstruction = Table("em_3d_reconstruction",
    metadata_obj,
    Column("entry_id", String(20), nullable=False),
    Column("id", String(20), primary_key=True),
    Column("method", String(255)),
    Column("algorithm", String(255)),
    Column("citation_id", String(20)),
    Column("details", String(255)),
    Column("resolution", Float),
    Column("resolution_method", String(255)),
    Column("magnification_calibration", String(255)),
    Column("ctf_correction_method", String(255)),
    Column("nominal_pixel_size", Float),
    Column("actual_pixel_size", Float),
    Column("num_particles", Integer),
    Column("euler_angles_details", String(255)),
    Column("num_class_averages", Integer),
    Column("software", String(255)),
    Column("fsc_type", String(255)),
    Column("refinement_type", String(255)),
    Column("image_processing_id", String(20), primary_key=True),
    Column("symmetry_type", String(128))
)


em_3d_fitting = Table("em_3d_fitting",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(128)),
    Column("target_criteria", String(255)),
    Column("software_name", String(255)),
    Column("details", String(255)),
    Column("overall_b_value", Float),
    Column("ref_space", String(128)),
    Column("ref_protocol", String(128)),
    Column("initial_refinement_model_id", Integer)
)


em_3d_fitting_list = Table("em_3d_fitting_list",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("3d_fitting_id", String(20), primary_key=True),
    Column("pdb_entry_id", String(20)),
    Column("pdb_chain_id", String(80)),
    Column("pdb_chain_residue_range", String(20)),
    Column("details", String(255)),
    Column("chain_id", String(80)),
    Column("chain_residue_range", String(20)),
    Column("source_name", String(20)),
    Column("type", String(128)),
    Column("accession_code", String(128)),
    Column("initial_refinement_model_id", Integer)
)


em_helical_entity = Table("em_helical_entity",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entity_assembly_id", String(20)),
    Column("image_processing_id", String(20), primary_key=True),
    Column("details", String(255)),
    Column("dyad", String(128)),
    Column("axial_symmetry", String(5), nullable=False),
    Column("angular_rotation_per_subunit", Float),
    Column("axial_rise_per_subunit", Float),
    Column("hand", String(255))
)


em_experiment = Table("em_experiment",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), nullable=False),
    Column("reconstruction_method", String(128), nullable=False),
    Column("aggregation_state", String(128), nullable=False),
    Column("specimen_type", String(255)),
    Column("entity_assembly_id", String(20), nullable=False)
)


em_single_particle_entity = Table("em_single_particle_entity",
    metadata_obj,
    Column("entry_id", String(20), nullable=False),
    Column("id", Integer, primary_key=True),
    Column("symmetry_type", String(128)),
    Column("image_processing_id", String(20), primary_key=True),
    Column("point_symmetry", String(20))
)


em_admin = Table("em_admin",
    metadata_obj,
    Column("current_status", String(20), nullable=False),
    Column("deposition_date", DateTime, nullable=False),
    Column("deposition_site", String(20), nullable=False),
    Column("details", String(255)),
    Column("entry_id", String(20), primary_key=True),
    Column("last_update", DateTime, nullable=False),
    Column("map_release_date", DateTime),
    Column("map_hold_date", DateTime),
    Column("header_release_date", DateTime),
    Column("obsoleted_date", DateTime),
    Column("replace_existing_entry_flag", String(20)),
    Column("title", String(128), nullable=False),
    Column("process_site", String(20)),
    Column("composite_map", String(128))
)


em_author_list = Table("em_author_list",
    metadata_obj,
    Column("author", String(150), nullable=False),
    Column("identifier_ORCID", String(20)),
    Column("ordinal", Integer, primary_key=True)
)


em_db_reference = Table("em_db_reference",
    metadata_obj,
    Column("access_code", String(20), nullable=False),
    Column("db_name", String(20), nullable=False),
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("relationship", String(128))
)


em_db_reference_auxiliary = Table("em_db_reference_auxiliary",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("link", String(20), nullable=False),
    Column("link_type", String(255), nullable=False)
)


em_depui = Table("em_depui",
    metadata_obj,
    Column("composite_map_deposition", String(128)),
    Column("depositor_hold_instructions", String(128), nullable=False),
    Column("entry_id", String(20), primary_key=True),
    Column("macromolecule_description", String(10), nullable=False),
    Column("obsolete_instructions", String(255)),
    Column("same_authors_as_pdb", String(10), nullable=False),
    Column("same_title_as_pdb", String(10), nullable=False)
)


em_obsolete = Table("em_obsolete",
    metadata_obj,
    Column("date", DateTime, nullable=False),
    Column("details", String(255)),
    Column("entry", String(15), nullable=False),
    Column("id", String(20), primary_key=True)
)


em_supersede = Table("em_supersede",
    metadata_obj,
    Column("date", DateTime, nullable=False),
    Column("details", String(255)),
    Column("entry", String(15), nullable=False),
    Column("id", String(20), primary_key=True)
)


em_entity_assembly_molwt = Table("em_entity_assembly_molwt",
    metadata_obj,
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("experimental_flag", String(20)),
    Column("id", String(20), primary_key=True),
    Column("units", String(20)),
    Column("value", Float),
    Column("method", String(255))
)


em_entity_assembly_naturalsource = Table("em_entity_assembly_naturalsource",
    metadata_obj,
    Column("cell", String(255)),
    Column("cellular_location", String(255)),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer, nullable=False),
    Column("organism", String(128), nullable=False),
    Column("organelle", String(255)),
    Column("organ", String(128)),
    Column("strain", String(255)),
    Column("tissue", String(255)),
    Column("details", String(255))
)


em_entity_assembly_synthetic = Table("em_entity_assembly_synthetic",
    metadata_obj,
    Column("cell", String(255)),
    Column("cellular_location", String(255)),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer, nullable=False),
    Column("organism", String(128), nullable=False),
    Column("organelle", String(255)),
    Column("organ", String(128)),
    Column("strain", String(255)),
    Column("tissue", String(255))
)


em_entity_assembly_recombinant = Table("em_entity_assembly_recombinant",
    metadata_obj,
    Column("cell", String(128)),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer, nullable=False),
    Column("organism", String(128), nullable=False),
    Column("plasmid", String(128)),
    Column("strain", String(128))
)


em_virus_natural_host = Table("em_virus_natural_host",
    metadata_obj,
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer),
    Column("organism", String(128)),
    Column("strain", String(255))
)


em_virus_synthetic = Table("em_virus_synthetic",
    metadata_obj,
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("organism", String(128)),
    Column("ncbi_tax_id", Integer),
    Column("strain", String(255))
)


em_virus_shell = Table("em_virus_shell",
    metadata_obj,
    Column("diameter", Float),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("triangulation", Integer)
)


em_specimen = Table("em_specimen",
    metadata_obj,
    Column("concentration", Float),
    Column("details", String(255)),
    Column("embedding_applied", String(80), nullable=False),
    Column("experiment_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("shadowing_applied", String(80), nullable=False),
    Column("staining_applied", String(80), nullable=False),
    Column("vitrification_applied", String(80), nullable=False)
)


em_embedding = Table("em_embedding",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("material", String(128), nullable=False),
    Column("specimen_id", String(20), nullable=False)
)


em_fiducial_markers = Table("em_fiducial_markers",
    metadata_obj,
    Column("diameter", Float, nullable=False),
    Column("em_tomography_specimen_id", String(20), nullable=False),
    Column("id", String(20), primary_key=True),
    Column("manufacturer", String(128), nullable=False)
)


em_focused_ion_beam = Table("em_focused_ion_beam",
    metadata_obj,
    Column("current", Float, nullable=False),
    Column("details", String(255)),
    Column("dose_rate", Integer),
    Column("duration", Float, nullable=False),
    Column("em_tomography_specimen_id", String(20), nullable=False),
    Column("final_thickness", Integer, nullable=False),
    Column("id", String(20), primary_key=True),
    Column("initial_thickness", Integer, nullable=False),
    Column("instrument", String(128), nullable=False),
    Column("ion", String(128), nullable=False),
    Column("temperature", Integer, nullable=False),
    Column("voltage", Integer, nullable=False)
)


em_grid_pretreatment = Table("em_grid_pretreatment",
    metadata_obj,
    Column("atmosphere", String(128)),
    Column("id", String(20), primary_key=True),
    Column("pressure", Float),
    Column("sample_support_id", String(20), nullable=False),
    Column("time", Integer),
    Column("type", String(128))
)


em_ultramicrotomy = Table("em_ultramicrotomy",
    metadata_obj,
    Column("details", String(255)),
    Column("em_tomography_specimen_id", String(20), nullable=False),
    Column("final_thickness", Integer, nullable=False),
    Column("id", String(20), primary_key=True),
    Column("instrument", String(128), nullable=False),
    Column("temperature", Integer, nullable=False)
)


em_high_pressure_freezing = Table("em_high_pressure_freezing",
    metadata_obj,
    Column("details", String(255)),
    Column("em_tomography_specimen_id", String(20), nullable=False),
    Column("id", String(20), primary_key=True),
    Column("instrument", String(128), nullable=False)
)


em_shadowing = Table("em_shadowing",
    metadata_obj,
    Column("angle", Float, nullable=False),
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("material", String(128), nullable=False),
    Column("specimen_id", String(20), primary_key=True),
    Column("thickness", Float, nullable=False)
)


em_tomography_specimen = Table("em_tomography_specimen",
    metadata_obj,
    Column("cryo_protectant", String(128)),
    Column("details", String(255)),
    Column("fiducial_markers", String(20)),
    Column("high_pressure_freezing", String(20)),
    Column("id", String(20), primary_key=True),
    Column("sectioning", String(128)),
    Column("specimen_id", String(20), nullable=False)
)


em_crystal_formation = Table("em_crystal_formation",
    metadata_obj,
    Column("atmosphere", String(255)),
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("instrument", String(128)),
    Column("lipid_mixture", String(255)),
    Column("lipid_protein_ratio", Float),
    Column("specimen_id", String(20), nullable=False),
    Column("temperature", Integer),
    Column("time", Integer),
    Column("time_unit", String(20))
)


em_staining = Table("em_staining",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("material", String(128), nullable=False),
    Column("specimen_id", String(20), nullable=False),
    Column("type", String(20), nullable=False)
)


em_support_film = Table("em_support_film",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("material", String(128)),
    Column("sample_support_id", String(20), nullable=False),
    Column("thickness", Float),
    Column("topology", String(128))
)


em_buffer_component = Table("em_buffer_component",
    metadata_obj,
    Column("buffer_id", String(20), primary_key=True),
    Column("concentration", Float),
    Column("concentration_units", String(128)),
    Column("formula", String(20)),
    Column("id", String(20), primary_key=True),
    Column("name", String(128))
)


em_diffraction = Table("em_diffraction",
    metadata_obj,
    Column("camera_length", Float, nullable=False),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20), nullable=False),
    Column("tilt_angle_list", String(128))
)


em_diffraction_shell = Table("em_diffraction_shell",
    metadata_obj,
    Column("em_diffraction_stats_id", String(20)),
    Column("fourier_space_coverage", Float, nullable=False),
    Column("high_resolution", Float, nullable=False),
    Column("id", String(20), primary_key=True),
    Column("low_resolution", Float, nullable=False),
    Column("multiplicity", Float, nullable=False),
    Column("num_structure_factors", Integer, nullable=False),
    Column("phase_residual", Float, nullable=False)
)


em_diffraction_stats = Table("em_diffraction_stats",
    metadata_obj,
    Column("details", String(255)),
    Column("fourier_space_coverage", Float, nullable=False),
    Column("high_resolution", Float, nullable=False),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20)),
    Column("num_intensities_measured", Integer, nullable=False),
    Column("num_structure_factors", Integer, nullable=False),
    Column("overall_phase_error", Float),
    Column("overall_phase_residual", Float),
    Column("phase_error_rejection_criteria", String(128), nullable=False),
    Column("r_merge", Float, nullable=False),
    Column("r_sym", Float)
)


em_tomography = Table("em_tomography",
    metadata_obj,
    Column("axis1_angle_increment", Float),
    Column("axis1_max_angle", Float),
    Column("axis1_min_angle", Float),
    Column("axis2_angle_increment", Float),
    Column("axis2_max_angle", Float),
    Column("axis2_min_angle", Float),
    Column("dual_tilt_axis_rotation", Float),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20), primary_key=True)
)


em_image_recording = Table("em_image_recording",
    metadata_obj,
    Column("average_exposure_time", Float),
    Column("avg_electron_dose_per_subtomogram", Float),
    Column("avg_electron_dose_per_image", Float),
    Column("details", String(255)),
    Column("detector_mode", String(128)),
    Column("film_or_detector_model", String(128)),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20), primary_key=True),
    Column("num_diffraction_images", Integer),
    Column("num_grids_imaged", Integer),
    Column("num_real_images", Integer)
)


em_imaging_optics = Table("em_imaging_optics",
    metadata_obj,
    Column("chr_aberration_corrector", String(255)),
    Column("energyfilter_lower", String(128)),
    Column("energyfilter_slit_width", Float),
    Column("energyfilter_name", String(128)),
    Column("energyfilter_upper", String(128)),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20), primary_key=True),
    Column("phase_plate", String(255)),
    Column("sph_aberration_corrector", String(255)),
    Column("details", String(128))
)


em_final_classification = Table("em_final_classification",
    metadata_obj,
    Column("avg_num_images_per_class", Integer),
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), nullable=False),
    Column("num_classes", Integer),
    Column("type", String(20))
)


em_start_model = Table("em_start_model",
    metadata_obj,
    Column("details", String(255)),
    Column("emdb_id", String(15)),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("insilico_model", String(255)),
    Column("orthogonal_tilt_angle1", Float),
    Column("orthogonal_tilt_angle2", Float),
    Column("orthogonal_tilt_num_images", Integer),
    Column("other", String(255)),
    Column("pdb_id", String(20)),
    Column("random_conical_tilt_angle", Float),
    Column("random_conical_tilt_num_images", Integer),
    Column("type", String(128), nullable=False)
)


em_software = Table("em_software",
    metadata_obj,
    Column("category", String(128)),
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20)),
    Column("fitting_id", String(20)),
    Column("imaging_id", String(20)),
    Column("name", String(128)),
    Column("version", String(128))
)


em_euler_angle_assignment = Table("em_euler_angle_assignment",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), nullable=False),
    Column("order", String(20), nullable=False),
    Column("proj_matching_angular_sampling", Float),
    Column("proj_matching_merit_function", String(128)),
    Column("proj_matching_num_projections", Integer),
    Column("type", String(128), nullable=False)
)


em_ctf_correction = Table("em_ctf_correction",
    metadata_obj,
    Column("amplitude_correction", String(20)),
    Column("amplitude_correction_factor", Float),
    Column("amplitude_correction_space", String(20)),
    Column("correction_operation", String(20)),
    Column("details", String(255)),
    Column("em_image_processing_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("phase_reversal", String(20)),
    Column("phase_reversal_anisotropic", String(20)),
    Column("phase_reversal_correction_space", String(20)),
    Column("type", String(128))
)


em_volume_selection = Table("em_volume_selection",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("method", String(255)),
    Column("num_tomograms", Integer, nullable=False),
    Column("num_volumes_extracted", Integer, nullable=False),
    Column("reference_model", String(255))
)


em_3d_crystal_entity = Table("em_3d_crystal_entity",
    metadata_obj,
    Column("angle_alpha", Float, nullable=False, default=90.0),
    Column("angle_beta", Float, nullable=False, default=90.0),
    Column("angle_gamma", Float, nullable=False, default=90.0),
    Column("image_processing_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("length_a", Float, nullable=False),
    Column("length_b", Float, nullable=False),
    Column("length_c", Float, nullable=False),
    Column("space_group_name", String(128), nullable=False),
    Column("space_group_num", Integer, nullable=False)
)


em_2d_crystal_entity = Table("em_2d_crystal_entity",
    metadata_obj,
    Column("angle_gamma", Float, nullable=False, default=90.0),
    Column("c_sampling_length", Float),
    Column("image_processing_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("entity_assembly_id", String(20)),
    Column("length_a", Float, nullable=False),
    Column("length_b", Float, nullable=False),
    Column("length_c", Float, nullable=False),
    Column("space_group_name_H-M", String(128), nullable=False)
)


em_image_processing = Table("em_image_processing",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("image_recording_id", String(20), primary_key=True)
)


em_particle_selection = Table("em_particle_selection",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("method", String(255)),
    Column("num_particles_selected", Integer),
    Column("reference_model", String(255))
)


em_map = Table("em_map",
    metadata_obj,
    Column("annotation_details", String(255)),
    Column("axis_order_fast", String(20), nullable=False),
    Column("axis_order_medium", String(20), nullable=False),
    Column("axis_order_slow", String(20), nullable=False),
    Column("cell_a", Float, nullable=False),
    Column("cell_b", Float, nullable=False),
    Column("cell_c", Float, nullable=False),
    Column("cell_alpha", Float, nullable=False),
    Column("cell_beta", Float, nullable=False),
    Column("cell_gamma", Float, nullable=False),
    Column("contour_level", Float),
    Column("contour_level_source", String(128)),
    Column("data_type", String(128), nullable=False),
    Column("dimensions_col", Integer, nullable=False),
    Column("dimensions_row", Integer, nullable=False),
    Column("dimensions_sec", Integer, nullable=False),
    Column("endian_type", String(20), nullable=False),
    Column("file", String(128)),
    Column("original_file", String(128)),
    Column("format", String(20), nullable=False),
    Column("id", Integer, primary_key=True),
    Column("partition", Integer, nullable=False),
    Column("entry_id", String(20), primary_key=True),
    Column("label", String(255)),
    Column("limit_col", Integer),
    Column("limit_row", Integer),
    Column("limit_sec", Integer),
    Column("origin_col", Integer, nullable=False),
    Column("origin_row", Integer, nullable=False),
    Column("origin_sec", Integer, nullable=False),
    Column("pixel_spacing_x", Float, nullable=False),
    Column("pixel_spacing_y", Float, nullable=False),
    Column("pixel_spacing_z", Float, nullable=False),
    Column("size_kb", Integer, nullable=False),
    Column("spacing_x", Integer, nullable=False),
    Column("spacing_y", Integer, nullable=False),
    Column("spacing_z", Integer, nullable=False),
    Column("statistics_average", Float),
    Column("statistics_maximum", Float),
    Column("statistics_minimum", Float),
    Column("statistics_std", Float),
    Column("symmetry_space_group", Integer, nullable=False),
    Column("type", String(128), nullable=False)
)


em_fsc_curve = Table("em_fsc_curve",
    metadata_obj,
    Column("details", String(255)),
    Column("file", String(128)),
    Column("id", String(20), primary_key=True)
)


em_interpret_figure = Table("em_interpret_figure",
    metadata_obj,
    Column("details", String(255)),
    Column("file", String(128), nullable=False),
    Column("id", String(20), primary_key=True)
)


em_layer_lines = Table("em_layer_lines",
    metadata_obj,
    Column("details", String(255)),
    Column("experiment_id", String(20), primary_key=True),
    Column("file", String(128), nullable=False),
    Column("id", String(20), primary_key=True)
)


em_structure_factors = Table("em_structure_factors",
    metadata_obj,
    Column("details", String(255)),
    Column("experiment_id", String(20), primary_key=True),
    Column("file", String(128), nullable=False),
    Column("id", String(20), primary_key=True)
)


em_depositor_info = Table("em_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("em_method_selection", String(128), nullable=False),
    Column("molecular_description_flag", String(20))
)


em_map_depositor_info = Table("em_map_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("experiment_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("map_type", String(20), nullable=False),
    Column("upload_file_name", String(128), nullable=False),
    Column("upload_format", String(20), nullable=False),
    Column("contour_level", Float),
    Column("annotation_details", String(255)),
    Column("pixel_spacing_x", Float, nullable=False),
    Column("pixel_spacing_y", Float, nullable=False),
    Column("pixel_spacing_z", Float, nullable=False)
)


em_mask_depositor_info = Table("em_mask_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("upload_file_name", String(128), nullable=False),
    Column("upload_format", String(20), nullable=False),
    Column("contour_level", Float),
    Column("annotation_details", String(255)),
    Column("pixel_spacing_x", Float, nullable=False),
    Column("pixel_spacing_y", Float, nullable=False),
    Column("pixel_spacing_z", Float, nullable=False)
)


em_figure_depositor_info = Table("em_figure_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("experiment_id", String(20)),
    Column("upload_file_name", String(128), nullable=False),
    Column("details", String(255))
)


em_layer_lines_depositor_info = Table("em_layer_lines_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("experiment_id", String(20)),
    Column("upload_file_name", String(128), nullable=False),
    Column("details", String(255))
)


em_structure_factors_depositor_info = Table("em_structure_factors_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("experiment_id", String(20)),
    Column("upload_file_name", String(128), nullable=False),
    Column("details", String(255))
)


pdbx_seq_map_depositor_info = Table("pdbx_seq_map_depositor_info",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("auth_asym_id", String(20), primary_key=True),
    Column("one_letter_code", String(255), nullable=False),
    Column("one_letter_code_mod", String(255))
)


pdbx_chem_comp_depositor_info = Table("pdbx_chem_comp_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("comp_id", String(10), nullable=False),
    Column("alt_comp_id", String(10)),
    Column("name", String(255)),
    Column("formula", String(255)),
    Column("type", String(128)),
    Column("descriptor", String(255)),
    Column("descriptor_type", String(50)),
    Column("in_dictionary_flag", String(20)),
    Column("details", String(255)),
    Column("upload_file_name", String(128)),
    Column("upload_file_type", String(20))
)


pdbx_struct_ref_seq_depositor_info = Table("pdbx_struct_ref_seq_depositor_info",
    metadata_obj,
    Column("ref_id", String(20), primary_key=True),
    Column("entity_id", String(20), nullable=False),
    Column("db_align_beg", Integer),
    Column("db_align_end", Integer),
    Column("details", String(255)),
    Column("db_accession", String(20)),
    Column("db_code", String(128)),
    Column("db_name", String(128)),
    Column("db_seq_one_letter_code", String(255)),
    Column("seq_align_begin", String(20)),
    Column("seq_align_end", String(20))
)


pdbx_struct_ref_seq_dif_depositor_info = Table("pdbx_struct_ref_seq_dif_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("ref_id", String(20), nullable=False),
    Column("entity_id", String(20), nullable=False),
    Column("db_mon_id", String(10)),
    Column("db_seq_id", Integer),
    Column("details", String(255)),
    Column("auth_mon_id", String(10)),
    Column("auth_seq_id", Integer),
    Column("db_accession", String(20)),
    Column("db_code", String(128)),
    Column("db_name", String(128)),
    Column("annotation", String(50))
)


pdbx_struct_assembly_prop_depositor_info = Table("pdbx_struct_assembly_prop_depositor_info",
    metadata_obj,
    Column("biol_id", String(20), primary_key=True),
    Column("type", String(128), primary_key=True),
    Column("value", String(255), nullable=False),
    Column("details", String(255))
)


pdbx_struct_assembly_depositor_info = Table("pdbx_struct_assembly_depositor_info",
    metadata_obj,
    Column("details", String(255)),
    Column("id", String(128), primary_key=True),
    Column("method_details", String(255)),
    Column("oligomeric_details", String(128)),
    Column("oligomeric_count", String(128)),
    Column("matrix_flag", String(20)),
    Column("upload_file_name", String(255))
)


pdbx_struct_assembly_gen_depositor_info = Table("pdbx_struct_assembly_gen_depositor_info",
    metadata_obj,
    Column("id", String(128), primary_key=True),
    Column("asym_id_list", String(128), nullable=False),
    Column("assembly_id", String(128), nullable=False),
    Column("oper_expression", String(511), nullable=False),
    Column("full_matrices", String(10)),
    Column("symmetry_operation", String(80)),
    Column("at_unit_matrix", String(2)),
    Column("chain_id_list", String(200)),
    Column("all_chains", String(2)),
    Column("helical_rotation", Float),
    Column("helical_rise", Float)
)


pdbx_struct_oper_list_depositor_info = Table("pdbx_struct_oper_list_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(128), nullable=False),
    Column("name", String(128)),
    Column("symmetry_operation", String(128)),
    Column("matrix[1][1]", Float),
    Column("matrix[1][2]", Float),
    Column("matrix[1][3]", Float),
    Column("matrix[2][1]", Float),
    Column("matrix[2][2]", Float),
    Column("matrix[2][3]", Float),
    Column("matrix[3][1]", Float),
    Column("matrix[3][2]", Float),
    Column("matrix[3][3]", Float),
    Column("vector[1]", Float),
    Column("vector[2]", Float),
    Column("vector[3]", Float)
)


pdbx_point_symmetry_depositor_info = Table("pdbx_point_symmetry_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("Schoenflies_symbol", String(20), nullable=False),
    Column("circular_symmetry", Integer),
    Column("H-M_notation", String(20)),
    Column("status_flag", String(20))
)


pdbx_helical_symmetry_depositor_info = Table("pdbx_helical_symmetry_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("number_of_operations", Integer),
    Column("rotation_per_n_subunits", Float),
    Column("rise_per_n_subunits", Float),
    Column("n_subunits_divisor", Integer),
    Column("dyad_axis", String(20)),
    Column("circular_symmetry", Integer),
    Column("status_flag", String(20))
)


pdbx_struct_assembly_auth_evidence_depositor_info = Table("pdbx_struct_assembly_auth_evidence_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(128), primary_key=True),
    Column("experimental_support", String(128), nullable=False),
    Column("details", String(255))
)


pdbx_solvent_atom_site_mapping = Table("pdbx_solvent_atom_site_mapping",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("label_alt_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_atom_id", String(6)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("PDB_ins_code", String(20)),
    Column("pre_auth_asym_id", String(20)),
    Column("pre_auth_atom_id", String(6)),
    Column("pre_auth_comp_id", String(20)),
    Column("pre_auth_seq_id", String(20)),
    Column("pre_PDB_ins_code", String(20)),
    Column("pre_auth_alt_id", String(20)),
    Column("auth_asym_id", String(20)),
    Column("auth_atom_id", String(6)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("auth_alt_id", String(20)),
    Column("occupancy", Float),
    Column("Cartn_x", Float),
    Column("Cartn_y", Float),
    Column("Cartn_z", Float),
    Column("pre_Cartn_x", Float),
    Column("pre_Cartn_y", Float),
    Column("pre_Cartn_z", Float),
    Column("symmetry", String(10)),
    Column("symmetry_as_xyz", String(128), default="x,y,z")
)


pdbx_molecule_features_depositor_info = Table("pdbx_molecule_features_depositor_info",
    metadata_obj,
    Column("entity_id", String(10), primary_key=True),
    Column("class", String(50)),
    Column("type", String(50)),
    Column("name", String(255)),
    Column("details", String(255))
)


pdbx_chem_comp_instance_depositor_info = Table("pdbx_chem_comp_instance_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("label_alt_id", String(20)),
    Column("comp_id", String(10), nullable=False),
    Column("PDB_ins_code", String(20)),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("in_polymer_flag", String(20)),
    Column("author_provided_flag", String(20)),
    Column("formula", String(255))
)


pdbx_depui_status_flags = Table("pdbx_depui_status_flags",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("primary_citation_status", String(20)),
    Column("corresponding_author_status", String(20)),
    Column("reference_citation_status", String(20)),
    Column("is_grant_funded", String(20)),
    Column("has_ncs_data", String(20)),
    Column("prediction_target", String(20)),
    Column("has_helical_symmetry", String(20)),
    Column("has_point_symmetry", String(20)),
    Column("has_cyclic_symmetry", String(20)),
    Column("has_accepted_terms_and_conditions", String(20), nullable=False),
    Column("has_viewed_validation_report", String(20)),
    Column("validated_model_file_name", String(128)),
    Column("merge_prior_model_file_name", String(128)),
    Column("merge_replace_model_file_name", String(128)),
    Column("merge_output_model_file_name", String(128)),
    Column("is_ligand_processing_complete", String(255), nullable=False),
    Column("sample_xyz_sequence_alignments_valid", String(255), nullable=False),
    Column("has_sas_data", String(20)),
    Column("is_sas_deposited", String(20)),
    Column("use_sas_refine", String(20)),
    Column("merged_fail", String(20)),
    Column("post_rel_replacement_reason", String(128)),
    Column("post_rel_replacement_reason_details", String(255)),
    Column("has_accepted_assemblies", String(20))
)


pdbx_depui_upload = Table("pdbx_depui_upload",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("file_content_type", String(128)),
    Column("file_type", String(128)),
    Column("file_name", String(128)),
    Column("file_size", Integer),
    Column("valid_flag", String(20)),
    Column("diagnostic_message", String(255)),
    Column("sequence_align", String(255))
)


pdbx_depui_validation_status_flags = Table("pdbx_depui_validation_status_flags",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("residual_B_factors_flag", String(20)),
    Column("occupancy_outliers_low", Integer),
    Column("occupancy_outliers_high", Integer),
    Column("adp_outliers_low", Integer),
    Column("solvent_outliers", Integer),
    Column("tls_no_aniso", String(20)),
    Column("adp_outliers_zero", String(255))
)


pdbx_chem_comp_upload_depositor_info = Table("pdbx_chem_comp_upload_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("comp_id", String(10), nullable=False),
    Column("upload_file_type", String(50), nullable=False),
    Column("upload_file_name", String(128), nullable=False)
)


pdbx_depui_entity_status_flags = Table("pdbx_depui_entity_status_flags",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("has_mutation", String(20)),
    Column("sample_xyz_sequence_alignments_valid", String(255), nullable=False)
)


pdbx_depui_entity_features = Table("pdbx_depui_entity_features",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("type", String(50), primary_key=True)
)


pdbx_deposition_message_info = Table("pdbx_deposition_message_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("deposition_data_set_id", String(20), nullable=False),
    Column("message_id", String(20), nullable=False),
    Column("timestamp", String(128), nullable=False),
    Column("sender", String(128), nullable=False),
    Column("content_type", String(128), nullable=False),
    Column("content_value", String(128), nullable=False),
    Column("parent_message_id", String(20), nullable=False),
    Column("message_subject", String(255), nullable=False),
    Column("message_text", String(255), nullable=False),
    Column("message_type", String(20), nullable=False),
    Column("send_status", String(20), nullable=False)
)


pdbx_deposition_message_file_reference = Table("pdbx_deposition_message_file_reference",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("deposition_data_set_id", String(20), nullable=False),
    Column("message_id", String(20), nullable=False),
    Column("content_type", String(20), nullable=False),
    Column("content_format", String(128), nullable=False),
    Column("partition_number", String(20), nullable=False),
    Column("version_id", String(20), nullable=False),
    Column("storage_type", String(20), nullable=False)
)


pdbx_depui_entry_details = Table("pdbx_depui_entry_details",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("wwpdb_site_id", String(20)),
    Column("experimental_methods", String(255), nullable=False),
    Column("requested_accession_types", String(128), nullable=False),
    Column("validated_contact_email", String(128), nullable=False),
    Column("validated_identifier_ORCID", String(20)),
    Column("country", String(128), nullable=False),
    Column("structural_genomics_flag", String(20)),
    Column("related_database_name", String(128)),
    Column("related_database_code", String(128)),
    Column("replace_pdb_id", String(255))
)


pdbx_data_processing_status = Table("pdbx_data_processing_status",
    metadata_obj,
    Column("task_name", String(128), primary_key=True),
    Column("status", String(128), primary_key=True)
)


pdbx_entity_instance_feature = Table("pdbx_entity_instance_feature",
    metadata_obj,
    Column("details", String(255)),
    Column("feature_type", String(128)),
    Column("auth_asym_id", String(20)),
    Column("asym_id", String(20)),
    Column("auth_seq_num", String(20)),
    Column("seq_num", Integer),
    Column("comp_id", String(10)),
    Column("auth_comp_id", String(20)),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_entity_src_gen_depositor_info = Table("pdbx_entity_src_gen_depositor_info",
    metadata_obj,
    Column("src_id", Integer, primary_key=True),
    Column("entity_id", String(20), nullable=False),
    Column("seq_type", String(128)),
    Column("beg_seq_num", Integer, nullable=False),
    Column("end_seq_num", Integer, nullable=False),
    Column("gene_src_gene", String(255)),
    Column("gene_src_scientific_name", String(255)),
    Column("host_org_gene", String(255)),
    Column("host_org_scientific_name", String(255)),
    Column("host_org_strain", String(255)),
    Column("gene_src_ncbi_taxonomy_id", Integer),
    Column("host_org_ncbi_taxonomy_id", Integer),
    Column("host_org_vector_type", String(255)),
    Column("plasmid_name", String(255))
)


pdbx_chem_comp_model = Table("pdbx_chem_comp_model",
    metadata_obj,
    Column("id", String(10), primary_key=True),
    Column("comp_id", String(10), nullable=False)
)


pdbx_chem_comp_model_atom = Table("pdbx_chem_comp_model_atom",
    metadata_obj,
    Column("atom_id", String(6), primary_key=True),
    Column("ordinal_id", Integer, nullable=False),
    Column("model_id", String(10), primary_key=True),
    Column("charge", Integer, default=0),
    Column("model_Cartn_x", Float),
    Column("model_Cartn_y", Float),
    Column("model_Cartn_z", Float),
    Column("type_symbol", String(20), nullable=False)
)


pdbx_chem_comp_model_bond = Table("pdbx_chem_comp_model_bond",
    metadata_obj,
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("model_id", String(10), primary_key=True),
    Column("value_order", String(10), default="sing"),
    Column("ordinal_id", Integer, nullable=False)
)


pdbx_chem_comp_model_feature = Table("pdbx_chem_comp_model_feature",
    metadata_obj,
    Column("model_id", String(10), primary_key=True),
    Column("feature_name", String(128), primary_key=True),
    Column("feature_value", String(255), nullable=False)
)


pdbx_chem_comp_model_descriptor = Table("pdbx_chem_comp_model_descriptor",
    metadata_obj,
    Column("model_id", String(10), primary_key=True),
    Column("descriptor", String(255), nullable=False),
    Column("type", String(50), primary_key=True)
)


pdbx_chem_comp_model_audit = Table("pdbx_chem_comp_model_audit",
    metadata_obj,
    Column("model_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20)),
    Column("processing_site", String(20)),
    Column("details", String(255)),
    Column("action_type", String(128), primary_key=True)
)


pdbx_chem_comp_model_reference = Table("pdbx_chem_comp_model_reference",
    metadata_obj,
    Column("model_id", String(10), primary_key=True),
    Column("db_name", String(128), primary_key=True),
    Column("db_code", String(128), primary_key=True)
)


pdbx_view_category_group = Table("pdbx_view_category_group",
    metadata_obj,
    Column("description", String(255), nullable=False)
)


pdbx_view_category = Table("pdbx_view_category",
    metadata_obj,
    Column("view_group_id", String(20), nullable=False),
    Column("category_view_name", String(128), nullable=False)
)


pdbx_view_item = Table("pdbx_view_item",
    metadata_obj,
    Column("item_name", String(80), primary_key=True),
    Column("category_id", String(20), nullable=False),
    Column("item_view_name", String(128), nullable=False),
    Column("item_view_mandatory_code", String(20), nullable=False),
    Column("item_view_allow_alternate_value", String(20), default="N")
)


pdbx_coord = Table("pdbx_coord",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("chain_atoms_Y_P", String(20), nullable=False),
    Column("hydrogen_atoms_Y_N", String(20), nullable=False),
    Column("solvent_atoms_Y_N", String(20), nullable=False),
    Column("structure_factors_Y_N", String(20), nullable=False)
)


pdbx_connect = Table("pdbx_connect",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("hetgroup_name", String(128)),
    Column("formul", String(128)),
    Column("hetgroup_chemical_name", String(255)),
    Column("parent_residue", String(20)),
    Column("formal_charge", Integer),
    Column("class_1", String(255)),
    Column("class_2", String(255)),
    Column("type", String(255)),
    Column("status", String(20)),
    Column("date", DateTime),
    Column("modified_date", DateTime)
)


pdbx_connect_type = Table("pdbx_connect_type",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("ndbTokenType", String(20)),
    Column("modified", String(20))
)


pdbx_connect_modification = Table("pdbx_connect_modification",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("modification", String(128), nullable=False)
)


pdbx_connect_atom = Table("pdbx_connect_atom",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("atom_name", String(20), primary_key=True),
    Column("connect_to", String(20), primary_key=True),
    Column("type_symbol", String(20), nullable=False),
    Column("charge", Integer, nullable=False),
    Column("bond_type", String(20)),
    Column("align_pos", Integer)
)


pdbx_database_PDB_master = Table("pdbx_database_PDB_master",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("num_remark", Integer),
    Column("num_ftnote", Integer),
    Column("num_het", Integer),
    Column("num_helix", Integer),
    Column("num_sheet", Integer),
    Column("num_turn", Integer),
    Column("num_site", Integer),
    Column("num_trans", Integer),
    Column("num_coord", Integer),
    Column("num_ter", Integer),
    Column("num_conect", Integer),
    Column("num_seqres", Integer)
)


pdbx_database_pdb_omit = Table("pdbx_database_pdb_omit",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("record_name", String(128), primary_key=True)
)


pdbx_dbref = Table("pdbx_dbref",
    metadata_obj,
    Column("pdb_id_code", String(20), primary_key=True),
    Column("chain_id", String(20), primary_key=True),
    Column("begin_res_number", String(20), primary_key=True),
    Column("begin_ins_code", String(20)),
    Column("end_res_number", String(20), primary_key=True),
    Column("end_ins_code", String(20)),
    Column("database_name", String(20), primary_key=True),
    Column("database_accession", String(20)),
    Column("database_id_code", String(20)),
    Column("database_begin_res_number", String(20)),
    Column("database_begin_ins_code", String(20)),
    Column("database_end_res_number", String(20)),
    Column("database_end_ins_code", String(20))
)


pdbx_drug_info = Table("pdbx_drug_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128), primary_key=True),
    Column("num_per_asym_unit", Integer, nullable=False),
    Column("num_of_whole_molecule", Integer),
    Column("size_of_molecule_per_asym_unit", String(20))
)


pdbx_inhibitor_info = Table("pdbx_inhibitor_info",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(128), nullable=False),
    Column("num_per_asym_unit", Integer, nullable=False)
)


pdbx_ion_info = Table("pdbx_ion_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=False),
    Column("numb_per_asym_unit", Integer, nullable=False)
)


pdbx_hybrid = Table("pdbx_hybrid",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("sugar_name", String(128), nullable=False),
    Column("strand_id", String(20), nullable=False),
    Column("residue_names", String(128), nullable=False)
)


pdbx_na_strand_info = Table("pdbx_na_strand_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("num_of_NA_strands_per_asym_unit", Integer, nullable=False),
    Column("num_of_NA_strands_per_biol_unit", Integer),
    Column("fract_NA_strand_per_asym_unit", String(20))
)


pdbx_nonstandard_list = Table("pdbx_nonstandard_list",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("auth_asym_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_seq_num", String(20)),
    Column("label_seq_id", Integer, primary_key=True),
    Column("ins_code", String(20)),
    Column("number_atoms_nh", Integer)
)


pdbx_pdb_compnd = Table("pdbx_pdb_compnd",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("text", String(255))
)


pdbx_pdb_source = Table("pdbx_pdb_source",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("text", String(255))
)


pdbx_protein_info = Table("pdbx_protein_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=False),
    Column("num_per_asym_unit", Integer, nullable=False)
)


pdbx_solvent_info = Table("pdbx_solvent_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=False),
    Column("numb_per_asym_unit", Integer, nullable=False)
)


pdbx_source = Table("pdbx_source",
    metadata_obj,
    Column("src_method", String(255), primary_key=True)
)


pdbx_struct_biol_func = Table("pdbx_struct_biol_func",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("biol_id", String(128), primary_key=True),
    Column("function", String(255), nullable=False)
)


pdbx_struct_pack_gen = Table("pdbx_struct_pack_gen",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("symmetry", String(10), primary_key=True, default="1_555"),
    Column("color_red", Float, default="?"),
    Column("color_green", Float, default="?"),
    Column("color_blue", Float, default="?"),
    Column("crystal_type", Integer, default="?"),
    Column("packing_type", Integer, default="?")
)


pdbx_trna_info = Table("pdbx_trna_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=False),
    Column("num_per_asym_unit", Integer, nullable=False)
)


pdbx_unpair = Table("pdbx_unpair",
    metadata_obj,
    Column("chain_id", String(20), primary_key=True),
    Column("residue_name", String(20)),
    Column("residue_number", String(20))
)


pdbx_refine_ls_restr_ncs = Table("pdbx_refine_ls_restr_ncs",
    metadata_obj,
    Column("dom_id", String(128), primary_key=True),
    Column("type", String(128)),
    Column("number", Integer),
    Column("rms_dev", Float),
    Column("weight", Float)
)


pdbx_struct_ncs_virus_gen = Table("pdbx_struct_ncs_virus_gen",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("oper_id", Integer, nullable=False),
    Column("asym_id", String(20), nullable=False),
    Column("pdb_chain_id", String(20), nullable=False)
)


pdbx_sequence_annotation = Table("pdbx_sequence_annotation",
    metadata_obj,
    Column("pdb_chain_id", String(20), primary_key=True),
    Column("ncbi_taxid", String(20), nullable=False)
)


pdbx_post_process_details = Table("pdbx_post_process_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("text", String(255)),
    Column("seq_details", String(255))
)


pdbx_post_process_status = Table("pdbx_post_process_status",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cycle_id", String(20), primary_key=True),
    Column("date_begin", Date, nullable=False),
    Column("date_end", Date, nullable=False),
    Column("details", String(255), nullable=False),
    Column("annotator", String(128), nullable=False)
)


pdbx_struct_link = Table("pdbx_struct_link",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(10)),
    Column("ptnr1_label_alt_id", String(20)),
    Column("ptnr1_label_asym_id", String(20), nullable=False),
    Column("ptnr1_label_atom_id", String(6), nullable=False),
    Column("ptnr1_label_comp_id", String(10), nullable=False),
    Column("ptnr1_label_seq_id", Integer, nullable=False),
    Column("ptnr1_label_ins_code", String(20)),
    Column("ptnr1_symmetry", String(10), default="1_555"),
    Column("ptnr2_label_alt_id", String(20)),
    Column("ptnr2_label_asym_id", String(20), nullable=False),
    Column("ptnr2_label_atom_id", String(6), nullable=False),
    Column("ptnr2_label_comp_id", String(10), nullable=False),
    Column("ptnr2_label_seq_id", Integer, nullable=False),
    Column("ptnr2_label_ins_code", String(20)),
    Column("ptnr2_symmetry", String(10), default="1_555"),
    Column("details", String(128)),
    Column("pdbx_dist_value", Float)
)


pdbx_missing_residue_list = Table("pdbx_missing_residue_list",
    metadata_obj,
    Column("pdb_model_id", Integer),
    Column("pdb_chain_id", String(20), primary_key=True),
    Column("pdb_residue_name", String(20), primary_key=True),
    Column("pdb_residue_number", String(20), primary_key=True),
    Column("pdb_insertion_code", String(20)),
    Column("label_seq_id", Integer)
)


pdbx_data_processing_cell = Table("pdbx_data_processing_cell",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("a", Float),
    Column("a_tolerance", Float),
    Column("b", Float),
    Column("b_tolerance", Float),
    Column("c", Float),
    Column("c_tolerance", Float),
    Column("alpha", Float),
    Column("alpha_tolerance", Float),
    Column("beta", Float),
    Column("beta_tolerance", Float),
    Column("gamma", Float),
    Column("gamma_tolerance", Float),
    Column("volume", Float),
    Column("mosaicity", Float),
    Column("resolution_range", String(128)),
    Column("space_group", String(128))
)


pdbx_data_processing_reflns = Table("pdbx_data_processing_reflns",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("number_all", Integer),
    Column("number_marked_reject", Integer),
    Column("percent_marked_reject", Float),
    Column("percent_rejected", Float),
    Column("R_factor_all_linear", Float)
)


pdbx_data_processing_detector = Table("pdbx_data_processing_detector",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("wavelength", Float),
    Column("polarization", Float),
    Column("beam_position_x", Float),
    Column("beam_position_y", Float),
    Column("cassette_rot_x", Float),
    Column("cassette_rot_y", Float),
    Column("cassette_rot_z", Float),
    Column("scale_y", Float),
    Column("skew", Float),
    Column("crossfire_x", Float),
    Column("crossfire_y", Float),
    Column("crossfire_xy", Float),
    Column("date", String(128)),
    Column("experimentor", String(255)),
    Column("crystal_data_id", String(255)),
    Column("processing_path", String(255)),
    Column("processing_files", String(255))
)


pdbx_chem_comp_nonstandard = Table("pdbx_chem_comp_nonstandard",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("type", String(128), primary_key=True)
)


pdbx_entity_poly_protein_class = Table("pdbx_entity_poly_protein_class",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("class", String(128), primary_key=True)
)


pdbx_entity_name_taxonomy_tree = Table("pdbx_entity_name_taxonomy_tree",
    metadata_obj,
    Column("id", String(255), primary_key=True),
    Column("parent_id", String(255), primary_key=True)
)


pdbx_entity_name_taxonomy = Table("pdbx_entity_name_taxonomy",
    metadata_obj,
    Column("id", String(255), primary_key=True),
    Column("name", String(255), primary_key=True),
    Column("name_type", String(128), nullable=False)
)


pdbx_entity_name_instance = Table("pdbx_entity_name_instance",
    metadata_obj,
    Column("name", String(255), primary_key=True),
    Column("pdb_id", String(20), primary_key=True),
    Column("rcsb_id", String(20), nullable=False),
    Column("entity_id", String(20), primary_key=True),
    Column("pdb_chain_id", String(20), nullable=False),
    Column("pdb_mol_id", String(20), nullable=False)
)


pdbx_val_angle = Table("pdbx_val_angle",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("auth_atom_id_3", String(6), nullable=False),
    Column("auth_asym_id_3", String(20), nullable=False),
    Column("auth_comp_id_3", String(20), nullable=False),
    Column("auth_seq_id_3", String(20), nullable=False),
    Column("auth_PDB_insert_id_1", String(20)),
    Column("auth_PDB_insert_id_2", String(20)),
    Column("auth_PDB_insert_id_3", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_asym_id_1", String(20)),
    Column("label_atom_id_1", String(6)),
    Column("label_comp_id_1", String(10)),
    Column("label_seq_id_1", Integer),
    Column("label_alt_id_2", String(20)),
    Column("label_asym_id_2", String(20)),
    Column("label_atom_id_2", String(6)),
    Column("label_comp_id_2", String(10)),
    Column("label_seq_id_2", Integer),
    Column("label_alt_id_3", String(20)),
    Column("label_asym_id_3", String(20)),
    Column("label_atom_id_3", String(6)),
    Column("label_comp_id_3", String(10)),
    Column("label_seq_id_3", Integer),
    Column("angle", Float, nullable=False),
    Column("angle_deviation", Float, nullable=False)
)


pdbx_val_bond = Table("pdbx_val_bond",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("auth_PDB_insert_id_1", String(20)),
    Column("auth_PDB_insert_id_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_asym_id_1", String(20)),
    Column("label_atom_id_1", String(6)),
    Column("label_comp_id_1", String(10)),
    Column("label_seq_id_1", Integer),
    Column("label_alt_id_2", String(20)),
    Column("label_asym_id_2", String(20)),
    Column("label_atom_id_2", String(6)),
    Column("label_comp_id_2", String(10)),
    Column("label_seq_id_2", Integer),
    Column("bond", Float, nullable=False),
    Column("bond_deviation", Float, nullable=False)
)


pdbx_val_contact = Table("pdbx_val_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("auth_PDB_insert_id_1", String(20)),
    Column("auth_PDB_insert_id_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_asym_id_1", String(20)),
    Column("label_atom_id_1", String(6)),
    Column("label_comp_id_1", String(10)),
    Column("label_seq_id_1", Integer),
    Column("label_alt_id_2", String(20)),
    Column("label_asym_id_2", String(20)),
    Column("label_atom_id_2", String(6)),
    Column("label_comp_id_2", String(10)),
    Column("label_seq_id_2", Integer),
    Column("dist", Float, nullable=False)
)


pdbx_val_sym_contact = Table("pdbx_val_sym_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id_1", String(20), nullable=False),
    Column("auth_atom_id_1", String(6), nullable=False),
    Column("auth_comp_id_1", String(20), nullable=False),
    Column("auth_seq_id_1", String(20), nullable=False),
    Column("auth_atom_id_2", String(6), nullable=False),
    Column("auth_asym_id_2", String(20), nullable=False),
    Column("auth_comp_id_2", String(20), nullable=False),
    Column("auth_seq_id_2", String(20), nullable=False),
    Column("auth_PDB_insert_id_1", String(20)),
    Column("auth_PDB_insert_id_2", String(20)),
    Column("label_alt_id_1", String(20)),
    Column("label_asym_id_1", String(20)),
    Column("label_atom_id_1", String(6)),
    Column("label_comp_id_1", String(10)),
    Column("label_seq_id_1", Integer),
    Column("label_alt_id_2", String(20)),
    Column("label_asym_id_2", String(20)),
    Column("label_atom_id_2", String(6)),
    Column("label_comp_id_2", String(10)),
    Column("label_seq_id_2", Integer),
    Column("site_symmetry_1", String(20), default="1_555"),
    Column("site_symmetry_2", String(20), default="1_555"),
    Column("dist", Float, nullable=False)
)


pdbx_rmch_outlier = Table("pdbx_rmch_outlier",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("auth_PDB_insert_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("phi", Float, nullable=False),
    Column("psi", Float, nullable=False)
)


pdbx_missing_atom_poly = Table("pdbx_missing_atom_poly",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("auth_PDB_insert_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("atom_name", String(20), nullable=False)
)


pdbx_missing_atom_nonpoly = Table("pdbx_missing_atom_nonpoly",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("auth_PDB_insert_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("atom_name", String(20), nullable=False)
)


pdbx_val_chiral = Table("pdbx_val_chiral",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id", String(20), nullable=False),
    Column("auth_comp_id", String(20), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("auth_PDB_insert_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("chiral_center_atom_name", String(20), nullable=False),
    Column("chiral_neighbor_atom_name", String(20), nullable=False),
    Column("chiral_center_atom_alt_id", String(20)),
    Column("chiral_neighbor_atom_alt_id", String(20))
)


pdbx_atlas = Table("pdbx_atlas",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("page_id", Integer, primary_key=True),
    Column("page_name", String(255), nullable=False)
)


pdbx_summary_flags = Table("pdbx_summary_flags",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("flag_id", String(128), primary_key=True),
    Column("flag_value", String(20), nullable=False)
)


pdbx_entity_func_bind_mode = Table("pdbx_entity_func_bind_mode",
    metadata_obj,
    Column("domain_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("protein_binds_to", String(20), nullable=False),
    Column("type", String(10), nullable=False)
)


pdbx_entity_func_enzyme = Table("pdbx_entity_func_enzyme",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50), nullable=False)
)


pdbx_entity_func_regulatory = Table("pdbx_entity_func_regulatory",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50), nullable=False)
)


pdbx_entity_func_structural = Table("pdbx_entity_func_structural",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50), nullable=False)
)


pdbx_entity_func_other = Table("pdbx_entity_func_other",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50), nullable=False)
)


pdbx_entity_poly_domain = Table("pdbx_entity_poly_domain",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("begin_mon_id", String(10), nullable=False),
    Column("begin_seq_num", Integer, nullable=False),
    Column("end_mon_id", String(10), nullable=False),
    Column("end_seq_num", Integer, nullable=False)
)


pdbx_na_struct_keywds = Table("pdbx_na_struct_keywds",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("conformation_type", String(128)),
    Column("strand_description", String(128)),
    Column("special_feature", String(128))
)


pdbx_entity_poly_na_type = Table("pdbx_entity_poly_na_type",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("type", String(128), primary_key=True)
)


pdbx_entity_poly_na_nonstandard = Table("pdbx_entity_poly_na_nonstandard",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("feature", String(128), primary_key=True)
)


pdbx_virtual_angle = Table("pdbx_virtual_angle",
    metadata_obj,
    Column("model_id", Integer, primary_key=True),
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20)),
    Column("atom_site_label_atom_id_1", String(6)),
    Column("atom_site_label_comp_id_1", String(10)),
    Column("atom_site_label_seq_id_1", Integer),
    Column("atom_site_label_asym_id_1", String(20)),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20)),
    Column("atom_site_label_atom_id_2", String(6)),
    Column("atom_site_label_comp_id_2", String(10)),
    Column("atom_site_label_seq_id_2", Integer),
    Column("atom_site_label_asym_id_2", String(20)),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20)),
    Column("atom_site_label_atom_id_3", String(6)),
    Column("atom_site_label_comp_id_3", String(10)),
    Column("atom_site_label_seq_id_3", Integer),
    Column("atom_site_label_asym_id_3", String(20)),
    Column("atom_site_auth_asym_id_1", String(20)),
    Column("atom_site_auth_atom_id_1", String(6)),
    Column("atom_site_auth_comp_id_1", String(20)),
    Column("atom_site_auth_seq_id_1", String(20)),
    Column("atom_site_auth_atom_id_2", String(6)),
    Column("atom_site_auth_asym_id_2", String(20)),
    Column("atom_site_auth_comp_id_2", String(20)),
    Column("atom_site_auth_seq_id_2", String(20)),
    Column("atom_site_auth_atom_id_3", String(6)),
    Column("atom_site_auth_asym_id_3", String(20)),
    Column("atom_site_auth_comp_id_3", String(20)),
    Column("atom_site_auth_seq_id_3", String(20)),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("value", Float),
    Column("value_esd", Float, default=0.0)
)


pdbx_virtual_bond = Table("pdbx_virtual_bond",
    metadata_obj,
    Column("model_id", Integer, primary_key=True),
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20)),
    Column("atom_site_label_atom_id_1", String(6)),
    Column("atom_site_label_comp_id_1", String(10)),
    Column("atom_site_label_seq_id_1", Integer),
    Column("atom_site_label_asym_id_1", String(20)),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20)),
    Column("atom_site_label_atom_id_2", String(6)),
    Column("atom_site_label_comp_id_2", String(10)),
    Column("atom_site_label_seq_id_2", Integer),
    Column("atom_site_label_asym_id_2", String(20)),
    Column("atom_site_auth_atom_id_1", String(6)),
    Column("atom_site_auth_asym_id_1", String(20)),
    Column("atom_site_auth_comp_id_1", String(20)),
    Column("atom_site_auth_seq_id_1", String(20)),
    Column("atom_site_auth_atom_id_2", String(6)),
    Column("atom_site_auth_asym_id_2", String(20)),
    Column("atom_site_auth_comp_id_2", String(20)),
    Column("atom_site_auth_seq_id_2", Integer),
    Column("dist", Float),
    Column("dist_esd", Float, default=0.0),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555")
)


pdbx_virtual_torsion = Table("pdbx_virtual_torsion",
    metadata_obj,
    Column("model_id", Integer, primary_key=True),
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20)),
    Column("atom_site_label_atom_id_1", String(6)),
    Column("atom_site_label_comp_id_1", String(10)),
    Column("atom_site_label_seq_id_1", Integer),
    Column("atom_site_label_asym_id_1", String(20)),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20)),
    Column("atom_site_label_atom_id_2", String(6)),
    Column("atom_site_label_comp_id_2", String(10)),
    Column("atom_site_label_seq_id_2", Integer),
    Column("atom_site_label_asym_id_2", String(20)),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20)),
    Column("atom_site_label_atom_id_3", String(6)),
    Column("atom_site_label_comp_id_3", String(10)),
    Column("atom_site_label_seq_id_3", Integer),
    Column("atom_site_label_asym_id_3", String(20)),
    Column("atom_site_id_4", String(20), primary_key=True),
    Column("atom_site_label_alt_id_4", String(20)),
    Column("atom_site_label_atom_id_4", String(6)),
    Column("atom_site_label_comp_id_4", String(10)),
    Column("atom_site_label_seq_id_4", Integer),
    Column("atom_site_label_asym_id_4", String(20)),
    Column("atom_site_auth_atom_id_1", String(6)),
    Column("atom_site_auth_asym_id_1", String(20)),
    Column("atom_site_auth_comp_id_1", String(20)),
    Column("atom_site_auth_seq_id_1", String(20)),
    Column("atom_site_auth_atom_id_2", String(6)),
    Column("atom_site_auth_asym_id_2", String(20)),
    Column("atom_site_auth_comp_id_2", String(20)),
    Column("atom_site_auth_seq_id_2", String(20)),
    Column("atom_site_auth_atom_id_3", String(6)),
    Column("atom_site_auth_asym_id_3", String(20)),
    Column("atom_site_auth_comp_id_3", String(20)),
    Column("atom_site_auth_seq_id_3", String(20)),
    Column("atom_site_auth_atom_id_4", String(6)),
    Column("atom_site_auth_asym_id_4", String(20)),
    Column("atom_site_auth_comp_id_4", String(20)),
    Column("atom_site_auth_seq_id_4", String(20)),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_4", String(10), primary_key=True, default="1_555"),
    Column("value", Float),
    Column("value_esd", Float, default=0.0)
)


pdbx_sequence_pattern = Table("pdbx_sequence_pattern",
    metadata_obj,
    Column("label_asym_id", String(20), primary_key=True),
    Column("auth_asym_id", String(20)),
    Column("pattern_count", Integer, nullable=False),
    Column("sequence_pattern", String(20), primary_key=True)
)


pdbx_stereochemistry = Table("pdbx_stereochemistry",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("label_seq_id", Integer, nullable=False),
    Column("label_atom_id", String(6), nullable=False),
    Column("label_alt_id", String(20), nullable=False),
    Column("label_atom_id_u", String(6), nullable=False),
    Column("label_alt_id_u", String(20), nullable=False),
    Column("label_atom_id_v", String(6), nullable=False),
    Column("label_alt_id_v", String(20), nullable=False),
    Column("label_atom_id_w", String(6), nullable=False),
    Column("label_alt_id_w", String(20), nullable=False),
    Column("volume3", Float, nullable=False),
    Column("angle_out_of_plane", Float, nullable=False)
)


pdbx_rms_devs_covalent = Table("pdbx_rms_devs_covalent",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("rms_bonds", Float, nullable=False),
    Column("num_bonds", Integer, nullable=False),
    Column("rms_bonds_base", Float, nullable=False),
    Column("num_bonds_base", Integer, nullable=False),
    Column("rms_bonds_sugar", Float, nullable=False),
    Column("num_bonds_sugar", Integer, nullable=False),
    Column("rms_bonds_phosphate", Float, nullable=False),
    Column("num_bonds_phosphate", Integer, nullable=False),
    Column("rms_angles", Float, nullable=False),
    Column("num_angles", Integer, nullable=False),
    Column("rms_angles_base", Float, nullable=False),
    Column("num_angles_base", Integer, nullable=False),
    Column("rms_angles_sugar", Float, nullable=False),
    Column("num_angles_sugar", Integer, nullable=False),
    Column("rms_angles_phosphate", Float, nullable=False),
    Column("num_angles_phosphate", Integer, nullable=False)
)


pdbx_rms_devs_cov_by_monomer = Table("pdbx_rms_devs_cov_by_monomer",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10), nullable=False),
    Column("auth_seq_id", String(20), nullable=False),
    Column("label_seq_id", Integer, nullable=False),
    Column("rms_bonds", Float, nullable=False),
    Column("num_bonds", Integer, nullable=False),
    Column("rms_angles", Float, nullable=False),
    Column("num_angles", Integer, nullable=False)
)


pdbx_sugar_phosphate_geometry = Table("pdbx_sugar_phosphate_geometry",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer, nullable=False),
    Column("auth_asym_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10), nullable=False),
    Column("auth_seq_id", String(20)),
    Column("label_seq_id", Integer, nullable=False),
    Column("neighbor_comp_id_5prime", String(10)),
    Column("neighbor_comp_id_3prime", String(10)),
    Column("o3_p_o5_c5", Float),
    Column("p_o5_c5_c4", Float),
    Column("o5_c5_c4_c3", Float),
    Column("c5_c4_c3_o3", Float),
    Column("c4_c3_o3_p", Float),
    Column("c3_o3_p_o5", Float),
    Column("c4_o4_c1_n1_9", Float),
    Column("o4_c1_n1_9_c2_4", Float),
    Column("o4_c1_n1_9_c6_8", Float),
    Column("c4_o4_c1_c2", Float),
    Column("o4_c1_c2_c3", Float),
    Column("c1_c2_c3_c4", Float),
    Column("c2_c3_c4_o4", Float),
    Column("c3_c4_o4_c1", Float),
    Column("c5_c4_c3_c2", Float),
    Column("o4_c4_c3_o3", Float),
    Column("o3_c3_c2_o2", Float),
    Column("o5_c5_c4_o4", Float),
    Column("pseudorot", Float),
    Column("maxtorsion", Float),
    Column("next_label_comp_id", String(10)),
    Column("next_label_seq_id", Integer),
    Column("next_o3_p_o5_c5", Float),
    Column("next_p_o5_c5_c4", Float),
    Column("next_o5_c5_c4_c3", Float),
    Column("next_c5_c4_c3_o3", Float),
    Column("next_c4_c3_o3_p", Float),
    Column("next_c3_o3_p_o5", Float),
    Column("next_c4_o4_c1_n1_9", Float),
    Column("next_o4_c1_n1_9_c2_4", Float),
    Column("c1_c2", Float),
    Column("c2_c3", Float),
    Column("c3_c4", Float),
    Column("c4_o4", Float),
    Column("o4_c1", Float),
    Column("p_o5", Float),
    Column("o5_c5", Float),
    Column("c5_c4", Float),
    Column("c3_o3", Float),
    Column("o3_p", Float),
    Column("p_o1p", Float),
    Column("p_o2p", Float),
    Column("c1_n9_1", Float),
    Column("n1_c2", Float),
    Column("n1_c6", Float),
    Column("n9_c4", Float),
    Column("n9_c8", Float),
    Column("c1_c2_c3", Float),
    Column("c2_c3_c4", Float),
    Column("c3_c4_o4", Float),
    Column("c4_o4_c1", Float),
    Column("o4_c1_c2", Float),
    Column("p_o5_c5", Float),
    Column("o5_c5_c4", Float),
    Column("c5_c4_c3", Float),
    Column("c4_c3_o3", Float),
    Column("c3_o3_p", Float),
    Column("o3_p_o5", Float),
    Column("o4_c1_n1_9", Float),
    Column("c1_n1_9_c2_4", Float),
    Column("c5_c4_o4", Float),
    Column("c2_c3_o3", Float),
    Column("o1p_p_o2p", Float),
    Column("c2_c1_n1_9", Float),
    Column("c1_n1_9_c6_8", Float)
)


pdbx_nmr_computing = Table("pdbx_nmr_computing",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("collection", String(128)),
    Column("collection_version", String(20)),
    Column("processing", String(128)),
    Column("processing_version", String(20)),
    Column("data_analysis", String(128)),
    Column("data_analysis_version", String(20)),
    Column("structure_solution", String(128)),
    Column("structure_solution_version", String(20)),
    Column("refinement", String(128)),
    Column("refinement_version", String(20)),
    Column("iterative_relaxation_matrix", String(128)),
    Column("iterative_relaxation_matrix_version", String(20))
)


pdbx_audit_conform_extension = Table("pdbx_audit_conform_extension",
    metadata_obj,
    Column("extension_dict_location", String(255)),
    Column("extension_dict_name", String(128), primary_key=True),
    Column("extension_dict_version", String(128), primary_key=True)
)


pdbx_dcc_mapman = Table("pdbx_dcc_mapman",
    metadata_obj,
    Column("pdbid", String(20), primary_key=True),
    Column("details", String(255))
)


pdbx_dcc_rscc_mapman = Table("pdbx_dcc_rscc_mapman",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", String(20)),
    Column("pdb_id", String(20)),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("label_alt_id", String(20)),
    Column("label_ins_code", String(20)),
    Column("correlation", Float),
    Column("real_space_R", Float),
    Column("weighted_real_space_R", Float),
    Column("real_space_Zscore", Float),
    Column("Biso_mean", Float),
    Column("occupancy_mean", Float),
    Column("flag", String(128))
)


pdbx_dcc_rscc_mapman_overall = Table("pdbx_dcc_rscc_mapman_overall",
    metadata_obj,
    Column("pdbid", String(20), primary_key=True),
    Column("correlation", Float),
    Column("correlation_sigma", Float),
    Column("real_space_R", Float),
    Column("real_space_R_sigma", Float)
)


pdbx_dcc_density = Table("pdbx_dcc_density",
    metadata_obj,
    Column("DCC_version", String(128)),
    Column("pdbid", String(20), primary_key=True),
    Column("pdbtype", String(128)),
    Column("unit_cell", String(128)),
    Column("space_group_name_H-M", String(128)),
    Column("space_group_pointless", String(128)),
    Column("ls_d_res_high", Float),
    Column("ls_d_res_high_sf", Float),
    Column("ls_d_res_low_sf", Float),
    Column("R_value_R_work", Float),
    Column("R_value_R_free", Float),
    Column("working_set_count", Integer),
    Column("free_set_count", Integer),
    Column("occupancy_min", Float),
    Column("occupancy_max", Float),
    Column("occupancy_mean", Float),
    Column("Biso_min", Float),
    Column("Biso_max", Float),
    Column("Biso_mean", Float),
    Column("B_wilson", Float),
    Column("B_wilson_scale", Float),
    Column("mean_I2_over_mean_I_square", Float),
    Column("mean_F_square_over_mean_F2", Float),
    Column("mean_E2_1_abs", Float),
    Column("Padilla-Yeates_L_mean", Float),
    Column("Padilla-Yeates_L2_mean", Float),
    Column("Padilla-Yeates_L2_mean_pointless", Float),
    Column("Z_score_L_test", Float),
    Column("twin_type", String(128)),
    Column("twin_operator_xtriage", String(255)),
    Column("twin_fraction_xtriage", Float),
    Column("twin_Rfactor", Float),
    Column("I_over_sigI_resh", Float),
    Column("I_over_sigI_diff", Float),
    Column("I_over_sigI_mean", Float),
    Column("ice_ring", String(128)),
    Column("anisotropy", Float),
    Column("Z-score", Float),
    Column("prob_peak_value", Float),
    Column("translational_pseudo_symmetry", String(128)),
    Column("wavelength", Float),
    Column("B_solvent", Float),
    Column("K_solvent", Float),
    Column("TLS_refinement_reported", String(128)),
    Column("partial_B_value_correction_attempted", String(128)),
    Column("partial_B_value_correction_success", String(128)),
    Column("reflection_status_archived", String(128)),
    Column("reflection_status_used", String(128)),
    Column("iso_B_value_type", String(128)),
    Column("reflns_twin", String(128)),
    Column("twin_by_xtriage", String(128)),
    Column("twin_operator", String(128)),
    Column("twin_fraction", String(128)),
    Column("tls_group_number", Integer),
    Column("ncs_group_number", Integer),
    Column("mtrix_number", Integer),
    Column("Matthew_coeff", Float),
    Column("solvent_content", Float),
    Column("Cruickshank_dpi_xyz", Float),
    Column("dpi_free_R", Float),
    Column("fom", Float),
    Column("correlation_overall", Float),
    Column("real_space_R_overall", Float),
    Column("mFo-DFc-3sigma_positive", Integer),
    Column("mFo-DFc-6sigma_positive", Integer),
    Column("mFo-DFc-3sigma_negative", Integer),
    Column("mFo-DFc-6sigma_negative", Integer),
    Column("Bmean-Bwilson", Float),
    Column("Rfree-Rwork", Float),
    Column("error", String(255))
)


pdbx_dcc_geometry = Table("pdbx_dcc_geometry",
    metadata_obj,
    Column("pdbid", String(20), primary_key=True),
    Column("Ramachandran_outlier_percent", Float),
    Column("Ramachandran_outlier_number", Integer),
    Column("Ramachandran_allowed_percent", Float),
    Column("Ramachandran_allowed_number", Integer),
    Column("Ramachandran_favored_percent", Float),
    Column("Ramachandran_favored_number", Integer),
    Column("rotamer_outliers_percent", Float),
    Column("rotamer_outliers_number", Integer),
    Column("cbeta_deviations", Integer),
    Column("all_atom_clashscore", Float),
    Column("overall_score", Float),
    Column("bond_overall_rms", Float),
    Column("bond_overall_max", Float),
    Column("bond_ligand_rms", Float),
    Column("bond_ligand_max", Float),
    Column("angle_overall_rms", Float),
    Column("angle_overall_max", Float),
    Column("angle_ligand_rms", Float),
    Column("angle_ligand_max", Float),
    Column("dihedral_overall_rms", Float),
    Column("dihedral_overall_max", Float),
    Column("chirality_overall_rms", Float),
    Column("chirality_overall_max", Float),
    Column("planarity_overall_rms", Float),
    Column("planarity_overall_max", Float),
    Column("non-bonded_rms", Float)
)


pdbx_dcc_density_corr = Table("pdbx_dcc_density_corr",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("program", String(128)),
    Column("ls_d_res_high", Float),
    Column("ls_d_res_low", Float),
    Column("ls_R_factor_R_all", Float),
    Column("ls_R_factor_R_work", Float),
    Column("ls_R_factor_R_free", Float),
    Column("ls_number_reflns_obs", Integer),
    Column("ls_percent_reflns_obs", Float),
    Column("ls_number_reflns_R_free", Integer),
    Column("correlation_coeff_Fo_to_Fc", Float),
    Column("real_space_R", Float),
    Column("correlation", Float),
    Column("details", String(128))
)


pdbx_dcc_map = Table("pdbx_dcc_map",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", String(20)),
    Column("pdb_id", String(20)),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("label_alt_id", String(20)),
    Column("label_ins_code", String(20)),
    Column("RSCC", Float),
    Column("RSR", Float),
    Column("weighted_RSR", Float),
    Column("RSRZ", Float),
    Column("weighted_RSRZ", Float),
    Column("Biso_mean", Float),
    Column("occupancy_mean", Float),
    Column("RSCC_main_chain", Float),
    Column("RSR_main_chain", Float),
    Column("wRSR_main_chain", Float),
    Column("RSRZ_main_chain", Float),
    Column("wRSRZ_main_chain", Float),
    Column("Biso_mean_main_chain", Float),
    Column("occupancy_mean_main_chain", Float),
    Column("RSCC_side_chain", Float),
    Column("RSR_side_chain", Float),
    Column("wRSR_side_chain", Float),
    Column("RSRZ_side_chain", Float),
    Column("wRSRZ_side_chain", Float),
    Column("Biso_mean_side_chain", Float),
    Column("occupancy_mean_side_chain", Float),
    Column("RSCC_phosphate_group", Float),
    Column("RSR_phosphate_group", Float),
    Column("wRSR_phosphate_group", Float),
    Column("RSRZ_phosphate_group", Float),
    Column("wRSRZ_phosphate_group", Float),
    Column("Biso_mean_phosphate_group", Float),
    Column("occupancy_mean_phosphate_group", Float),
    Column("shift", Float),
    Column("shift_main_chain", Float),
    Column("shift_side_chain", Float),
    Column("density_connectivity", Float),
    Column("density_index_main_chain", Float),
    Column("density_index_side_chain", Float),
    Column("RSZD", Float),
    Column("RSZO", Float),
    Column("RSZO_Zscore", Float),
    Column("LLDF", Float),
    Column("RSZD_main_chain", Float),
    Column("RSZO_main_chain", Float),
    Column("RSZD_side_chain", Float),
    Column("RSZO_side_chain", Float),
    Column("RSZD_phosphate_group", Float),
    Column("RSZO_phosphate_group", Float),
    Column("quality_indicator", String(128))
)


pdbx_deposit_group = Table("pdbx_deposit_group",
    metadata_obj,
    Column("group_id", String(20), primary_key=True),
    Column("group_title", String(255)),
    Column("group_description", String(255)),
    Column("group_type", String(255))
)


pdbx_deposit_group_index = Table("pdbx_deposit_group_index",
    metadata_obj,
    Column("group_id", String(20), primary_key=True),
    Column("ordinal_id", Integer, primary_key=True),
    Column("dep_set_id", String(20)),
    Column("pdb_id_code", String(20)),
    Column("group_file_name", String(20)),
    Column("group_file_timestamp", Date),
    Column("auth_file_label", String(128)),
    Column("auth_file_content_type", String(128)),
    Column("auth_file_format_type", String(20)),
    Column("auth_file_name", String(128)),
    Column("auth_file_size", Integer)
)


pdbx_struct_assembly_auth_evidence = Table("pdbx_struct_assembly_auth_evidence",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(128), primary_key=True),
    Column("experimental_support", String(128), nullable=False),
    Column("details", String(255))
)


pdbx_struct_assembly_auth_classification = Table("pdbx_struct_assembly_auth_classification",
    metadata_obj,
    Column("assembly_id", String(128), primary_key=True),
    Column("reason_for_interest", String(128), nullable=False)
)


pdbx_crystal_alignment = Table("pdbx_crystal_alignment",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("oscillation_range", Float),
    Column("oscillation_start", Float),
    Column("oscillation_end", Float),
    Column("xbeam", Float),
    Column("xbeam_esd", Float),
    Column("ybeam", Float),
    Column("ybeam_esd", Float),
    Column("crysx_spindle", Float),
    Column("crysx_spindle_esd", Float),
    Column("crysy_vertical", Float),
    Column("crysy_vertical_esd", Float),
    Column("crysz_beam", Float),
    Column("crysz_beam_esd", Float),
    Column("crystal_to_detector_distance", Float),
    Column("crystal_to_detector_distance_esd", Float),
    Column("crossfire_x", Float),
    Column("crossfire_x_esd", Float),
    Column("crossfire_y", Float),
    Column("crossfire_y_esd", Float),
    Column("crossfire_xy", Float),
    Column("crossfire_xy_esd", Float),
    Column("overall_beam_divergence", Float),
    Column("overall_beam_divergence_esd", Float)
)


pdbx_audit_revision_history = Table("pdbx_audit_revision_history",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("major_revision", Integer, nullable=False),
    Column("minor_revision", Integer, nullable=False),
    Column("revision_date", DateTime, nullable=False),
    Column("internal_version", Integer),
    Column("internal_deposition_id", String(20))
)


pdbx_audit_revision_group = Table("pdbx_audit_revision_group",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("group", String(128), nullable=False)
)


pdbx_audit_revision_category = Table("pdbx_audit_revision_category",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("category", String(20), nullable=False)
)


pdbx_audit_revision_details = Table("pdbx_audit_revision_details",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("provider", String(128)),
    Column("type", String(128)),
    Column("description", String(255)),
    Column("details", String(255))
)


pdbx_audit_revision_item = Table("pdbx_audit_revision_item",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("item", String(20), nullable=False)
)


pdbx_supporting_exp_data_set = Table("pdbx_supporting_exp_data_set",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), nullable=False),
    Column("data_version_major", Integer),
    Column("data_version_minor", Integer),
    Column("details", String(255))
)


pdbx_database_doi = Table("pdbx_database_doi",
    metadata_obj,
    Column("db_name", String(10), primary_key=True),
    Column("db_DOI", String(10), nullable=False)
)


pdbx_audit_conform = Table("pdbx_audit_conform",
    metadata_obj,
    Column("dict_location", String(255)),
    Column("dict_name", String(255), primary_key=True),
    Column("dict_version", String(255), primary_key=True)
)


pdbx_serial_crystallography_measurement = Table("pdbx_serial_crystallography_measurement",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("pulse_energy", Float),
    Column("pulse_duration", Float),
    Column("xfel_pulse_repetition_rate", Float),
    Column("pulse_photon_energy", Float),
    Column("photons_per_pulse", Float),
    Column("source_size", Float),
    Column("source_distance", Float),
    Column("focal_spot_size", Float),
    Column("collimation", String(255)),
    Column("collection_time_total", Float)
)


pdbx_serial_crystallography_sample_delivery = Table("pdbx_serial_crystallography_sample_delivery",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("description", String(255)),
    Column("method", String(255), nullable=False)
)


pdbx_serial_crystallography_sample_delivery_injection = Table("pdbx_serial_crystallography_sample_delivery_injection",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("description", String(255)),
    Column("injector_diameter", Float),
    Column("injector_temperature", Float),
    Column("injector_pressure", Float),
    Column("flow_rate", Float),
    Column("carrier_solvent", String(255)),
    Column("crystal_concentration", Float),
    Column("preparation", String(255)),
    Column("power_by", String(255)),
    Column("injector_nozzle", String(255)),
    Column("jet_diameter", Float),
    Column("filter_size", Float)
)


pdbx_serial_crystallography_sample_delivery_fixed_target = Table("pdbx_serial_crystallography_sample_delivery_fixed_target",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("description", String(255)),
    Column("sample_holding", String(255)),
    Column("support_base", String(255)),
    Column("sample_unit_size", Float),
    Column("crystals_per_unit", Integer),
    Column("sample_solvent", String(255)),
    Column("sample_dehydration_prevention", String(128)),
    Column("motion_control", String(128)),
    Column("velocity_horizontal", Float),
    Column("velocity_vertical", Float),
    Column("details", String(255))
)


pdbx_serial_crystallography_data_reduction = Table("pdbx_serial_crystallography_data_reduction",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("frames_total", Integer),
    Column("xfel_pulse_events", Integer),
    Column("frame_hits", Integer),
    Column("crystal_hits", Integer),
    Column("droplet_hits", Integer),
    Column("frames_failed_index", Integer),
    Column("frames_indexed", Integer),
    Column("lattices_indexed", Integer),
    Column("xfel_run_numbers", String(255)),
    Column("lattices_merged", Integer)
)


pdbx_audit_support = Table("pdbx_audit_support",
    metadata_obj,
    Column("funding_organization", String(255)),
    Column("country", String(128)),
    Column("grant_number", String(128)),
    Column("details", String(128)),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_entity_branch_list = Table("pdbx_entity_branch_list",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("hetero", String(10), default="no"),
    Column("comp_id", String(10), primary_key=True),
    Column("num", Integer, primary_key=True)
)


pdbx_entity_branch_link = Table("pdbx_entity_branch_link",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("details", String(255)),
    Column("entity_id", String(20), nullable=False),
    Column("entity_branch_list_num_1", Integer, nullable=False),
    Column("entity_branch_list_num_2", Integer, nullable=False),
    Column("comp_id_1", String(20), nullable=False),
    Column("comp_id_2", String(20), nullable=False),
    Column("atom_id_1", String(6), nullable=False),
    Column("leaving_atom_id_1", String(6), nullable=False),
    Column("atom_stereo_config_1", String(10), default="N"),
    Column("atom_id_2", String(6), nullable=False),
    Column("leaving_atom_id_2", String(6), nullable=False),
    Column("atom_stereo_config_2", String(10), default="N"),
    Column("value_order", String(10), default="sing")
)


pdbx_entity_branch = Table("pdbx_entity_branch",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("type", String(20), nullable=False)
)


pdbx_branch_scheme = Table("pdbx_branch_scheme",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("hetero", String(10), default="no"),
    Column("asym_id", String(20), primary_key=True),
    Column("mon_id", String(10), primary_key=True),
    Column("num", Integer, primary_key=True),
    Column("pdb_asym_id", String(20), nullable=False),
    Column("pdb_seq_num", String(20), nullable=False),
    Column("pdb_ins_code", String(20)),
    Column("pdb_mon_id", String(20), nullable=False),
    Column("auth_asym_id", String(20)),
    Column("auth_seq_num", String(20)),
    Column("auth_mon_id", String(20))
)


pdbx_chem_comp_related = Table("pdbx_chem_comp_related",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("related_comp_id", String(10), primary_key=True),
    Column("relationship_type", String(128), primary_key=True),
    Column("details", String(255))
)


pdbx_chem_comp_atom_related = Table("pdbx_chem_comp_atom_related",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("related_comp_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("atom_id", String(6), nullable=False),
    Column("related_atom_id", String(6)),
    Column("related_type", String(128), nullable=False)
)


pdbx_refln_signal_binning = Table("pdbx_refln_signal_binning",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("upper_threshold", Float, nullable=False)
)


pdbx_sifts_xref_db = Table("pdbx_sifts_xref_db",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("seq_id_ordinal", Integer, primary_key=True),
    Column("seq_id", Integer, primary_key=True),
    Column("mon_id", String(10), nullable=False),
    Column("mon_id_one_letter_code", String(10), nullable=False),
    Column("unp_res", String(10)),
    Column("unp_num", Integer),
    Column("unp_acc", String(128)),
    Column("unp_segment_id", Integer),
    Column("unp_instance_id", Integer),
    Column("res_type", String(128)),
    Column("observed", String(2), nullable=False),
    Column("mh_id", Integer),
    Column("xref_db_name", String(20)),
    Column("xref_db_acc", String(20)),
    Column("xref_domain_name", String(128)),
    Column("xref_db_segment_id", Integer),
    Column("xref_db_instance_id", Integer)
)


pdbx_sifts_xref_db_segments = Table("pdbx_sifts_xref_db_segments",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("xref_db", String(128), primary_key=True),
    Column("xref_db_acc", String(20), primary_key=True),
    Column("domain_name", String(128)),
    Column("segment_id", Integer, primary_key=True),
    Column("instance_id", Integer, primary_key=True),
    Column("seq_id_start", Integer, primary_key=True),
    Column("seq_id_end", Integer, primary_key=True)
)


pdbx_sifts_unp_segments = Table("pdbx_sifts_unp_segments",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("unp_acc", String(128), primary_key=True),
    Column("segment_id", Integer, primary_key=True),
    Column("instance_id", Integer, primary_key=True),
    Column("unp_start", Integer, nullable=False),
    Column("unp_end", Integer, nullable=False),
    Column("seq_id_start", Integer, nullable=False),
    Column("seq_id_end", Integer, nullable=False),
    Column("best_mapping", String(2), nullable=False),
    Column("identity", Float, nullable=False)
)


pdbx_data_usage = Table("pdbx_data_usage",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(20), nullable=False),
    Column("details", String(255), nullable=False),
    Column("url", String(20)),
    Column("name", String(128))
)


pdbx_entity_remapping = Table("pdbx_entity_remapping",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("orig_entity_id", String(20), nullable=False)
)


pdbx_chain_remapping = Table("pdbx_chain_remapping",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("auth_asym_id", String(20), nullable=False),
    Column("orig_label_asym_id", String(20), nullable=False),
    Column("orig_auth_asym_id", String(20), nullable=False),
    Column("applied_operations", String(20), nullable=False)
)


pdbx_initial_refinement_model = Table("pdbx_initial_refinement_model",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("entity_id_list", String(255)),
    Column("type", String(128), nullable=False),
    Column("source_name", String(20)),
    Column("accession_code", String(128)),
    Column("details", String(128))
)


pdbx_investigation = Table("pdbx_investigation",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(128), nullable=False),
    Column("resource_name", String(20), nullable=False),
    Column("resource_accession", String(20), nullable=False),
    Column("details", String(255))
)


pdbx_chem_comp_pcm = Table("pdbx_chem_comp_pcm",
    metadata_obj,
    Column("pcm_id", Integer, primary_key=True),
    Column("comp_id", String(10), nullable=False),
    Column("modified_residue_id", String(50)),
    Column("type", String(128), nullable=False),
    Column("category", String(128), nullable=False),
    Column("position", String(128), nullable=False),
    Column("polypeptide_position", String(128), nullable=False),
    Column("comp_id_linking_atom", String(6)),
    Column("modified_residue_id_linking_atom", String(6)),
    Column("uniprot_specific_ptm_accession", String(20)),
    Column("uniprot_generic_ptm_accession", String(20)),
    Column("first_instance_model_db_code", String(128))
)


pdbx_modification_feature = Table("pdbx_modification_feature",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("label_comp_id", String(10), nullable=False),
    Column("label_asym_id", String(20), nullable=False),
    Column("label_seq_id", Integer),
    Column("label_alt_id", String(20)),
    Column("modified_residue_label_comp_id", String(10)),
    Column("modified_residue_label_asym_id", String(20)),
    Column("modified_residue_label_seq_id", Integer),
    Column("modified_residue_label_alt_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_asym_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20)),
    Column("symmetry", String(10)),
    Column("modified_residue_auth_comp_id", String(20)),
    Column("modified_residue_auth_asym_id", String(20)),
    Column("modified_residue_auth_seq_id", String(20)),
    Column("modified_residue_PDB_ins_code", String(20)),
    Column("modified_residue_symmetry", String(10)),
    Column("comp_id_linking_atom", String(6)),
    Column("modified_residue_id_linking_atom", String(6)),
    Column("modified_residue_id", String(50)),
    Column("ref_pcm_id", Integer),
    Column("ref_comp_id", String(10)),
    Column("type", String(128), nullable=False),
    Column("category", String(128), nullable=False)
)


pdbx_diffrn_batch = Table("pdbx_diffrn_batch",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("diffrn_id", String(20)),
    Column("cell_id", String(20)),
    Column("wavelength_id", String(20)),
    Column("space_group_id", String(20)),
    Column("detector_id", String(20), default="1"),
    Column("orientation_id", String(20))
)


pdbx_diffrn_cell = Table("pdbx_diffrn_cell",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("angle_alpha", Float, default=90.0),
    Column("angle_alpha_esd", Float),
    Column("angle_beta", Float, default=90.0),
    Column("angle_beta_esd", Float),
    Column("angle_gamma", Float, default=90.0),
    Column("angle_gamma_esd", Float),
    Column("length_a", Float, nullable=False),
    Column("length_a_esd", Float),
    Column("length_b", Float, nullable=False),
    Column("length_b_esd", Float),
    Column("length_c", Float, nullable=False),
    Column("length_c_esd", Float)
)


pdbx_diffrn_orientation = Table("pdbx_diffrn_orientation",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("matrix[1][1]", Float),
    Column("matrix[1][2]", Float),
    Column("matrix[1][3]", Float),
    Column("matrix[2][1]", Float),
    Column("matrix[2][2]", Float),
    Column("matrix[2][3]", Float),
    Column("matrix[3][1]", Float),
    Column("matrix[3][2]", Float),
    Column("matrix[3][3]", Float),
    Column("type", String(128))
)


pdbx_diffrn_batch_scan = Table("pdbx_diffrn_batch_scan",
    metadata_obj,
    Column("batch_id", String(20), primary_key=True),
    Column("scan_id", String(20), nullable=False)
)


pdbx_diffrn_detector_panel_mapping = Table("pdbx_diffrn_detector_panel_mapping",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("detector_id", String(20), nullable=False, default="1"),
    Column("array_id", String(20), nullable=False, default="1"),
    Column("array_section_id", String(20), nullable=False)
)


diffrn_scan = Table("diffrn_scan",
    metadata_obj,
    Column("date_end", DateTime),
    Column("date_end_estimated", DateTime),
    Column("date_start", DateTime),
    Column("integration_time", Float),
    Column("frame_id_start", String(20), nullable=False),
    Column("frame_id_end", String(20), nullable=False),
    Column("frames", Integer),
    Column("time_period", Float),
    Column("time_rstrt_incr", Float)
)


diffrn_scan_axis = Table("diffrn_scan_axis",
    metadata_obj,
    Column("scan_id", String(20), primary_key=True),
    Column("axis_id", String(20), primary_key=True),
    Column("angle_start", Float, default=0.0),
    Column("angle_range", Float, default=0.0),
    Column("angle_increment", Float, default=0.0),
    Column("angle_rstrt_incr", Float, default=0.0),
    Column("displacement_start", Float, default=0.0),
    Column("displacement_range", Float, default=0.0),
    Column("displacement_increment", Float, default=0.0),
    Column("displacement_rstrt_incr", Float, default=0.0),
    Column("reference_angle", Float, default=0.0),
    Column("reference_displacement", Float)
)


diffrn_scan_collection = Table("diffrn_scan_collection",
    metadata_obj,
    Column("details", String(255)),
    Column("scan_id", String(20), primary_key=True),
    Column("type", String(255), default="rotation"),
    Column("translation_width", Float, default=0.0)
)


diffrn_scan_frame = Table("diffrn_scan_frame",
    metadata_obj,
    Column("date", DateTime),
    Column("frame_id", String(20), primary_key=True),
    Column("frame_number", Integer),
    Column("integration_time", Float, nullable=False),
    Column("polarizn_Stokes_I", Float, default=1.0),
    Column("scan_id", String(20), primary_key=True),
    Column("time_period", Float),
    Column("time_rstrt_incr", Float)
)


diffrn_scan_frame_axis = Table("diffrn_scan_frame_axis",
    metadata_obj,
    Column("axis_id", String(20), primary_key=True),
    Column("angle", Float, default=0.0),
    Column("angle_increment", Float, default=0.0),
    Column("angle_rstrt_incr", Float, default=0.0),
    Column("displacement", Float, default=0.0),
    Column("displacement_increment", Float, default=0.0),
    Column("displacement_rstrt_incr", Float, default=0.0),
    Column("frame_id", String(20), primary_key=True),
    Column("reference_angle", Float, default=0.0),
    Column("reference_displacement", Float)
)


array_intensities = Table("array_intensities",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, default="1"),
    Column("binary_id", Integer, primary_key=True, default=1),
    Column("details", String(255)),
    Column("gain", Float, nullable=False),
    Column("gain_esd", Float, nullable=False),
    Column("linearity", String(20), nullable=False),
    Column("offset", Float),
    Column("overload", Float),
    Column("pixel_fast_bin_size", Float, default=1.0),
    Column("pixel_slow_bin_size", Float, default=1.0),
    Column("pixel_binning_method", String(20), default="unspecified"),
    Column("scaling", Float),
    Column("undefined_value", Float),
    Column("underload", Float)
)


array_structure = Table("array_structure",
    metadata_obj,
    Column("byte_order", String(10), nullable=False),
    Column("compression_type", String(10), default="none"),
    Column("compression_type_flag", String(10)),
    Column("encoding_type", String(50), nullable=False)
)


array_data = Table("array_data",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, default="1"),
    Column("data", String(255), nullable=False),
    Column("external_data_id", String(20), default="1"),
    Column("header_contents", String(255)),
    Column("header_convention", String(20))
)


array_structure_list = Table("array_structure_list",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, default="1"),
    Column("array_section_id", String(20), default="1"),
    Column("dimension", Integer, nullable=False),
    Column("direction", String(20), nullable=False),
    Column("precedence", Integer, nullable=False)
)


array_structure_list_axis = Table("array_structure_list_axis",
    metadata_obj,
    Column("axis_id", String(20), primary_key=True),
    Column("axis_set_id", String(20), primary_key=True),
    Column("angle", Float, default=0.0),
    Column("angle_increment", Float, default=0.0),
    Column("displacement", Float, default=0.0),
    Column("fract_displacement", Float, default=0.0),
    Column("displacement_increment", Float, default=0.0),
    Column("fract_displacement_increment", Float, default=0.0),
    Column("angular_pitch", Float, default=0.0),
    Column("radial_pitch", Float, default=0.0),
    Column("reference_angle", Float),
    Column("reference_displacement", Float)
)


array_structure_list_section = Table("array_structure_list_section",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, default="1"),
    Column("end", Integer),
    Column("id", String(20), primary_key=True),
    Column("index", Integer, primary_key=True),
    Column("start", Integer),
    Column("stride", Integer, default=1)
)


diffrn_data_frame = Table("diffrn_data_frame",
    metadata_obj,
    Column("array_id", String(20), default="1"),
    Column("array_section_id", String(20)),
    Column("binary_id", Integer, default=1),
    Column("center_fast", Float),
    Column("center_slow", Float),
    Column("center_derived", String(10), default="yes"),
    Column("center_units", String(20)),
    Column("detector_element_id", String(20), primary_key=True),
    Column("details", String(255))
)


diffrn_detector_axis = Table("diffrn_detector_axis",
    metadata_obj,
    Column("axis_id", String(20), primary_key=True),
    Column("detector_id", String(20), primary_key=True, default="1")
)


diffrn_detector_element = Table("diffrn_detector_element",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("detector_id", String(20), primary_key=True),
    Column("reference_center_fast", Float),
    Column("reference_center_slow", Float),
    Column("reference_center_units", String(20))
)


def drop_schema(engine):
    with engine.connect() as conn:
        with conn.begin():
            metadata_obj.drop_all(conn)


def create_all_tables(engine):
    with engine.connect() as conn:
        with conn.begin():
            metadata_obj.create_all(conn)


def create_tables(engine, categories):
    with engine.connect() as conn:
        with conn.begin():
            for category in categories:
                if category in metadata_obj.tables:
                    metadata_obj.tables[category].create(conn, checkfirst=True)


def get_table(table_name):
    return metadata_obj.tables.get(table_name)


def cast_type(table_obj: Table, tag: str, value):
    if not isinstance(table_obj.c[tag].type, String) and value == "":
        return None

    if isinstance(table_obj.c[tag].type, Float):
        return float(value)

    if isinstance(table_obj.c[tag].type, Integer):
        return int(value)

    if isinstance(table_obj.c[tag].type, DateTime):
        try:
            return parse(value)
        except ValueError:
            return value

    if isinstance(table_obj.c[tag].type, Date):
        return date.fromisoformat(value)

    if isinstance(table_obj.c[tag].type, Boolean):
        return bool(value)

    return value
