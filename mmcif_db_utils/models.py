from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Date, DateTime


metadata_obj = MetaData()


atom_site_anisotrop = Table("atom_site_anisotrop",
    metadata_obj,
    Column("B[1][1]", Float, nullable=True),
    Column("B[1][1]_esd", Float, nullable=True),
    Column("B[1][2]", Float, nullable=True),
    Column("B[1][2]_esd", Float, nullable=True),
    Column("B[1][3]", Float, nullable=True),
    Column("B[1][3]_esd", Float, nullable=True),
    Column("B[2][2]", Float, nullable=True),
    Column("B[2][2]_esd", Float, nullable=True),
    Column("B[2][3]", Float, nullable=True),
    Column("B[2][3]_esd", Float, nullable=True),
    Column("B[3][3]", Float, nullable=True),
    Column("B[3][3]_esd", Float, nullable=True),
    Column("ratio", Float, nullable=True),
    Column("id", String(20), primary_key=True),
    Column("type_symbol", String(20)),
    Column("U[1][1]", Float, nullable=True),
    Column("U[1][1]_esd", Float, nullable=True),
    Column("U[1][2]", Float, nullable=True),
    Column("U[1][2]_esd", Float, nullable=True),
    Column("U[1][3]", Float, nullable=True),
    Column("U[1][3]_esd", Float, nullable=True),
    Column("U[2][2]", Float, nullable=True),
    Column("U[2][2]_esd", Float, nullable=True),
    Column("U[2][3]", Float, nullable=True),
    Column("U[2][3]_esd", Float, nullable=True),
    Column("U[3][3]", Float, nullable=True),
    Column("U[3][3]_esd", Float, nullable=True),
    Column("pdbx_auth_seq_id", String(20), nullable=True),
    Column("pdbx_auth_alt_id", String(20), nullable=True),
    Column("pdbx_auth_asym_id", String(20), nullable=True),
    Column("pdbx_auth_atom_id", String(6), nullable=True),
    Column("pdbx_auth_comp_id", String(20), nullable=True),
    Column("pdbx_label_seq_id", Integer, nullable=True),
    Column("pdbx_label_alt_id", String(20), nullable=True),
    Column("pdbx_label_asym_id", String(20), nullable=True),
    Column("pdbx_label_atom_id", String(6), nullable=True),
    Column("pdbx_label_comp_id", String(10), nullable=True),
    Column("pdbx_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_PDB_model_num", Integer, nullable=True),
    Column("pdbx_not_in_asym", String(20), nullable=True),
    Column("pdbx_PDB_residue_no", String(20), nullable=True),
    Column("pdbx_PDB_residue_name", String(20), nullable=True),
    Column("pdbx_PDB_strand_id", String(20), nullable=True),
    Column("pdbx_PDB_atom_name", String(6), nullable=True),
    Column("pdbx_auth_atom_name", String(6), nullable=True),
    Column("pdbx_label_ins_code", String(20), nullable=True)
)


atom_sites = Table("atom_sites",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("Cartn_transf_matrix[1][1]", Float, nullable=True),
    Column("Cartn_transf_matrix[1][2]", Float, nullable=True),
    Column("Cartn_transf_matrix[1][3]", Float, nullable=True),
    Column("Cartn_transf_matrix[2][1]", Float, nullable=True),
    Column("Cartn_transf_matrix[2][2]", Float, nullable=True),
    Column("Cartn_transf_matrix[2][3]", Float, nullable=True),
    Column("Cartn_transf_matrix[3][1]", Float, nullable=True),
    Column("Cartn_transf_matrix[3][2]", Float, nullable=True),
    Column("Cartn_transf_matrix[3][3]", Float, nullable=True),
    Column("Cartn_transf_vector[1]", Float, nullable=True),
    Column("Cartn_transf_vector[2]", Float, nullable=True),
    Column("Cartn_transf_vector[3]", Float, nullable=True),
    Column("Cartn_transform_axes", String(255), nullable=True),
    Column("fract_transf_matrix[1][1]", Float, nullable=True),
    Column("fract_transf_matrix[1][2]", Float, nullable=True),
    Column("fract_transf_matrix[1][3]", Float, nullable=True),
    Column("fract_transf_matrix[2][1]", Float, nullable=True),
    Column("fract_transf_matrix[2][2]", Float, nullable=True),
    Column("fract_transf_matrix[2][3]", Float, nullable=True),
    Column("fract_transf_matrix[3][1]", Float, nullable=True),
    Column("fract_transf_matrix[3][2]", Float, nullable=True),
    Column("fract_transf_matrix[3][3]", Float, nullable=True),
    Column("fract_transf_vector[1]", Float, nullable=True),
    Column("fract_transf_vector[2]", Float, nullable=True),
    Column("fract_transf_vector[3]", Float, nullable=True),
    Column("solution_primary", String(10), nullable=True),
    Column("solution_secondary", String(10), nullable=True),
    Column("solution_hydrogens", String(10), nullable=True),
    Column("special_details", String(255), nullable=True)
)


atom_sites_alt = Table("atom_sites_alt",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True, nullable=True)
)


atom_sites_alt_ens = Table("atom_sites_alt_ens",
    metadata_obj,
    Column("details", String(255), nullable=True)
)


atom_sites_alt_gen = Table("atom_sites_alt_gen",
    metadata_obj,
    Column("alt_id", String(20), primary_key=True),
    Column("ens_id", String(20), primary_key=True)
)


atom_sites_footnote = Table("atom_sites_footnote",
    metadata_obj,
    Column("text", String(255), nullable=True)
)


atom_type = Table("atom_type",
    metadata_obj,
    Column("analytical_mass_percent", Float, nullable=True),
    Column("description", String(255), nullable=True),
    Column("number_in_cell", Integer, nullable=True),
    Column("oxidation_number", Integer, nullable=True, default=0),
    Column("radius_bond", Float, nullable=True),
    Column("radius_contact", Float, nullable=True),
    Column("scat_Cromer_Mann_a1", Float, nullable=True),
    Column("scat_Cromer_Mann_a2", Float, nullable=True),
    Column("scat_Cromer_Mann_a3", Float, nullable=True),
    Column("scat_Cromer_Mann_a4", Float, nullable=True),
    Column("scat_Cromer_Mann_b1", Float, nullable=True),
    Column("scat_Cromer_Mann_b2", Float, nullable=True),
    Column("scat_Cromer_Mann_b3", Float, nullable=True),
    Column("scat_Cromer_Mann_b4", Float, nullable=True),
    Column("scat_Cromer_Mann_c", Float, nullable=True),
    Column("scat_dispersion_imag", Float, nullable=True),
    Column("scat_dispersion_real", Float, nullable=True),
    Column("scat_length_neutron", String(255), nullable=True),
    Column("scat_source", String(255), nullable=True),
    Column("scat_versus_stol_list", String(255), nullable=True),
    Column("scat_dispersion_source", String(255), nullable=True),
    Column("pdbx_scat_Cromer_Mann_a5", Float, nullable=True),
    Column("pdbx_scat_Cromer_Mann_b5", Float, nullable=True),
    Column("pdbx_scat_Cromer_Mann_a6", Float, nullable=True),
    Column("pdbx_scat_Cromer_Mann_b6", Float, nullable=True),
    Column("pdbx_scat_Z", Integer, nullable=True),
    Column("pdbx_N_electrons", Integer, nullable=True)
)


audit = Table("audit",
    metadata_obj,
    Column("creation_date", DateTime, nullable=True),
    Column("creation_method", String(255), nullable=True),
    Column("revision_id", String(20), primary_key=True),
    Column("update_record", String(255), nullable=True)
)


audit_author = Table("audit_author",
    metadata_obj,
    Column("address", String(255), nullable=True),
    Column("name", String(128)),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("identifier_ORCID", String(20), nullable=True)
)


audit_conform = Table("audit_conform",
    metadata_obj,
    Column("dict_location", String(255), nullable=True),
    Column("dict_name", String(255), primary_key=True),
    Column("dict_version", String(255), primary_key=True)
)


audit_contact_author = Table("audit_contact_author",
    metadata_obj,
    Column("address", String(255), nullable=True),
    Column("email", String(128), nullable=True),
    Column("fax", String(128), nullable=True),
    Column("name", String(128), primary_key=True),
    Column("phone", String(128), nullable=True)
)


cell_measurement = Table("cell_measurement",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("pressure", Float, nullable=True),
    Column("pressure_esd", Float, nullable=True),
    Column("radiation", String(128), nullable=True),
    Column("reflns_used", Integer, nullable=True),
    Column("temp", Float, nullable=True),
    Column("temp_esd", Float, nullable=True),
    Column("theta_max", Float, nullable=True),
    Column("theta_min", Float, nullable=True),
    Column("wavelength", Float, nullable=True)
)


cell_measurement_refln = Table("cell_measurement_refln",
    metadata_obj,
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("theta", Float, nullable=True)
)


chem_comp = Table("chem_comp",
    metadata_obj,
    Column("formula", String(255), nullable=True),
    Column("formula_weight", Float, nullable=True),
    Column("model_details", String(255), nullable=True),
    Column("model_erf", String(128), nullable=True),
    Column("model_source", String(255), nullable=True),
    Column("mon_nstd_class", String(255), nullable=True),
    Column("mon_nstd_details", String(255), nullable=True),
    Column("mon_nstd_flag", String(10), nullable=True, default="no"),
    Column("mon_nstd_parent", String(20), nullable=True),
    Column("mon_nstd_parent_comp_id", String(50), nullable=True),
    Column("name", String(255), nullable=True),
    Column("number_atoms_all", Integer, nullable=True),
    Column("number_atoms_nh", Integer, nullable=True),
    Column("one_letter_code", String(10), nullable=True),
    Column("three_letter_code", String(6), nullable=True),
    Column("pdbx_synonyms", String(255), nullable=True),
    Column("pdbx_modification_details", String(255), nullable=True),
    Column("pdbx_component_no", Integer, nullable=True),
    Column("pdbx_type", String(50), nullable=True),
    Column("pdbx_ambiguous_flag", String(20), nullable=True),
    Column("pdbx_replaced_by", String(10), nullable=True),
    Column("pdbx_replaces", String(50), nullable=True),
    Column("pdbx_formal_charge", Integer, nullable=True, default=0),
    Column("pdbx_subcomponent_list", String(255), nullable=True),
    Column("pdbx_model_coordinates_details", String(255), nullable=True),
    Column("pdbx_model_coordinates_db_code", String(128), nullable=True),
    Column("pdbx_ideal_coordinates_details", String(255), nullable=True),
    Column("pdbx_ideal_coordinates_missing_flag", String(10), nullable=True, default="N"),
    Column("pdbx_model_coordinates_missing_flag", String(10), nullable=True, default="N"),
    Column("pdbx_initial_date", DateTime, nullable=True),
    Column("pdbx_modified_date", DateTime, nullable=True),
    Column("pdbx_release_status", String(128), nullable=True),
    Column("pdbx_processing_site", String(20), nullable=True),
    Column("pdbx_number_subcomponents", Integer, nullable=True),
    Column("pdbx_class_1", String(128), nullable=True),
    Column("pdbx_class_2", String(128), nullable=True),
    Column("pdbx_comp_type", String(128), nullable=True),
    Column("pdbx_reserved_name", String(255), nullable=True),
    Column("pdbx_status", String(20), nullable=True),
    Column("pdbx_type_modified", Integer, nullable=True),
    Column("pdbx_casnum", String(128), nullable=True),
    Column("pdbx_smiles", String(255), nullable=True),
    Column("pdbx_nscnum", String(20), nullable=True),
    Column("pdbx_pcm", String(20), nullable=True)
)


chem_comp_angle = Table("chem_comp_angle",
    metadata_obj,
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("atom_id_3", String(6), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("value_angle", Float, nullable=True),
    Column("value_angle_esd", Float, nullable=True),
    Column("value_dist", Float, nullable=True),
    Column("value_dist_esd", Float, nullable=True)
)


chem_comp_atom = Table("chem_comp_atom",
    metadata_obj,
    Column("alt_atom_id", String(128), nullable=True),
    Column("charge", Integer, nullable=True, default=0),
    Column("model_Cartn_x", Float, nullable=True),
    Column("model_Cartn_x_esd", Float, nullable=True),
    Column("model_Cartn_y", Float, nullable=True),
    Column("model_Cartn_y_esd", Float, nullable=True),
    Column("model_Cartn_z", Float, nullable=True),
    Column("model_Cartn_z_esd", Float, nullable=True),
    Column("comp_id", String(10), primary_key=True),
    Column("partial_charge", Float, nullable=True),
    Column("substruct_code", String(10), nullable=True),
    Column("type_symbol", String(20)),
    Column("pdbx_align", Integer, nullable=True),
    Column("pdbx_ordinal", Integer, nullable=True),
    Column("pdbx_component_atom_id", String(6), nullable=True),
    Column("pdbx_component_comp_id", String(10), nullable=True),
    Column("pdbx_alt_atom_id", String(6), nullable=True),
    Column("pdbx_alt_comp_id", String(10), nullable=True),
    Column("pdbx_model_Cartn_x_ideal", Float, nullable=True),
    Column("pdbx_model_Cartn_y_ideal", Float, nullable=True),
    Column("pdbx_model_Cartn_z_ideal", Float, nullable=True),
    Column("pdbx_stereo_config", String(10), nullable=True),
    Column("pdbx_aromatic_flag", String(10), nullable=True),
    Column("pdbx_leaving_atom_flag", String(10), nullable=True),
    Column("pdbx_residue_numbering", Integer, nullable=True),
    Column("pdbx_polymer_type", String(128), nullable=True),
    Column("pdbx_ref_id", String(10), nullable=True),
    Column("pdbx_component_id", Integer, nullable=True),
    Column("pdbx_component_entity_id", Integer, nullable=True),
    Column("pdbx_stnd_atom_id", String(128), nullable=True),
    Column("pdbx_backbone_atom_flag", String(10), nullable=True),
    Column("pdbx_n_terminal_atom_flag", String(10), nullable=True),
    Column("pdbx_c_terminal_atom_flag", String(10), nullable=True)
)


chem_comp_bond = Table("chem_comp_bond",
    metadata_obj,
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("value_order", String(10), nullable=True, default="sing"),
    Column("value_dist", Float, nullable=True),
    Column("value_dist_esd", Float, nullable=True),
    Column("pdbx_ordinal", Integer, nullable=True),
    Column("pdbx_stereo_config", String(10), nullable=True),
    Column("pdbx_aromatic_flag", String(10), nullable=True)
)


chem_comp_chir = Table("chem_comp_chir",
    metadata_obj,
    Column("atom_id", String(6)),
    Column("atom_config", String(10), nullable=True),
    Column("comp_id", String(10), primary_key=True),
    Column("number_atoms_all", Integer, nullable=True),
    Column("number_atoms_nh", Integer, nullable=True),
    Column("volume_flag", String(10), nullable=True),
    Column("volume_three", Float, nullable=True),
    Column("volume_three_esd", Float, nullable=True)
)


chem_comp_chir_atom = Table("chem_comp_chir_atom",
    metadata_obj,
    Column("atom_id", String(6), primary_key=True),
    Column("chir_id", String(20), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("dev", Float, nullable=True)
)


chem_comp_link = Table("chem_comp_link",
    metadata_obj,
    Column("link_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("type_comp_1", String(50)),
    Column("type_comp_2", String(50))
)


chem_comp_plane = Table("chem_comp_plane",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("number_atoms_all", Integer, nullable=True),
    Column("number_atoms_nh", Integer, nullable=True)
)


chem_comp_plane_atom = Table("chem_comp_plane_atom",
    metadata_obj,
    Column("atom_id", String(6), primary_key=True),
    Column("comp_id", String(10), primary_key=True),
    Column("plane_id", String(20), primary_key=True),
    Column("dist_esd", Float, nullable=True)
)


chem_comp_tor = Table("chem_comp_tor",
    metadata_obj,
    Column("atom_id_1", String(6)),
    Column("atom_id_2", String(6)),
    Column("atom_id_3", String(6)),
    Column("atom_id_4", String(6)),
    Column("comp_id", String(10), primary_key=True)
)


chem_comp_tor_value = Table("chem_comp_tor_value",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("tor_id", String(20), primary_key=True),
    Column("angle", Float),
    Column("angle_esd", Float),
    Column("dist", Float, nullable=True),
    Column("dist_esd", Float, nullable=True)
)


chem_link = Table("chem_link",
    metadata_obj,
    Column("details", String(255), nullable=True)
)


chem_link_angle = Table("chem_link_angle",
    metadata_obj,
    Column("atom_1_comp_id", String(10), nullable=True),
    Column("atom_2_comp_id", String(10), nullable=True),
    Column("atom_3_comp_id", String(10), nullable=True),
    Column("atom_id_1", String(20), primary_key=True),
    Column("atom_id_2", String(20), primary_key=True),
    Column("atom_id_3", String(20), primary_key=True),
    Column("link_id", String(20), primary_key=True),
    Column("value_angle", Float, nullable=True),
    Column("value_angle_esd", Float, nullable=True),
    Column("value_dist", Float, nullable=True),
    Column("value_dist_esd", Float, nullable=True)
)


chem_link_bond = Table("chem_link_bond",
    metadata_obj,
    Column("atom_1_comp_id", String(10), nullable=True),
    Column("atom_2_comp_id", String(10), nullable=True),
    Column("atom_id_1", String(20), primary_key=True),
    Column("atom_id_2", String(20), primary_key=True),
    Column("link_id", String(20), primary_key=True),
    Column("value_dist", Float, nullable=True),
    Column("value_dist_esd", Float, nullable=True),
    Column("value_order", String(10), nullable=True, default="sing")
)


chem_link_chir = Table("chem_link_chir",
    metadata_obj,
    Column("atom_comp_id", String(10), nullable=True),
    Column("atom_id", String(20)),
    Column("atom_config", String(10), nullable=True),
    Column("link_id", String(20), primary_key=True),
    Column("number_atoms_all", Integer, nullable=True),
    Column("number_atoms_nh", Integer, nullable=True),
    Column("volume_flag", String(10), nullable=True),
    Column("volume_three", Float, nullable=True),
    Column("volume_three_esd", Float, nullable=True)
)


chem_link_chir_atom = Table("chem_link_chir_atom",
    metadata_obj,
    Column("atom_comp_id", String(10), nullable=True),
    Column("atom_id", String(20), primary_key=True),
    Column("chir_id", String(20), primary_key=True),
    Column("dev", Float, nullable=True)
)


chem_link_plane = Table("chem_link_plane",
    metadata_obj,
    Column("link_id", String(20), primary_key=True),
    Column("number_atoms_all", Integer, nullable=True),
    Column("number_atoms_nh", Integer, nullable=True)
)


chem_link_plane_atom = Table("chem_link_plane_atom",
    metadata_obj,
    Column("atom_comp_id", String(10), nullable=True),
    Column("atom_id", String(20), primary_key=True),
    Column("plane_id", String(20), primary_key=True)
)


chem_link_tor = Table("chem_link_tor",
    metadata_obj,
    Column("atom_1_comp_id", String(10), nullable=True),
    Column("atom_2_comp_id", String(10), nullable=True),
    Column("atom_3_comp_id", String(10), nullable=True),
    Column("atom_4_comp_id", String(10), nullable=True),
    Column("atom_id_1", String(20)),
    Column("atom_id_2", String(20)),
    Column("atom_id_3", String(20)),
    Column("atom_id_4", String(20)),
    Column("link_id", String(20), primary_key=True)
)


chem_link_tor_value = Table("chem_link_tor_value",
    metadata_obj,
    Column("tor_id", String(20), primary_key=True),
    Column("angle", Float),
    Column("angle_esd", Float),
    Column("dist", Float, nullable=True),
    Column("dist_esd", Float, nullable=True)
)


chemical = Table("chemical",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("compound_source", String(255), nullable=True),
    Column("melting_point", Float, nullable=True),
    Column("name_common", String(255), nullable=True),
    Column("name_mineral", String(255), nullable=True),
    Column("name_structure_type", String(255), nullable=True),
    Column("name_systematic", String(255), nullable=True),
    Column("absolute_configuration", String(20), nullable=True),
    Column("melting_point_gt", Float, nullable=True),
    Column("melting_point_lt", Float, nullable=True),
    Column("optical_rotation", String(128), nullable=True),
    Column("properties_biological", String(255), nullable=True),
    Column("properties_physical", String(255), nullable=True),
    Column("temperature_decomposition", Float, nullable=True),
    Column("temperature_decomposition_esd", Float, nullable=True),
    Column("temperature_decomposition_gt", Float, nullable=True),
    Column("temperature_decomposition_lt", Float, nullable=True),
    Column("temperature_sublimation", Float, nullable=True),
    Column("temperature_sublimation_esd", Float, nullable=True),
    Column("temperature_sublimation_gt", Float, nullable=True),
    Column("temperature_sublimation_lt", Float, nullable=True)
)


chemical_conn_atom = Table("chemical_conn_atom",
    metadata_obj,
    Column("charge", Integer, nullable=True, default=0),
    Column("display_x", Float, nullable=True),
    Column("display_y", Float, nullable=True),
    Column("NCA", Integer, nullable=True),
    Column("NH", Integer, nullable=True),
    Column("type_symbol", String(20))
)


chemical_conn_bond = Table("chemical_conn_bond",
    metadata_obj,
    Column("atom_1", Integer, primary_key=True),
    Column("atom_2", Integer, primary_key=True),
    Column("type", String(10), nullable=True, default="sing")
)


chemical_formula = Table("chemical_formula",
    metadata_obj,
    Column("analytical", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("iupac", String(255), nullable=True),
    Column("moiety", String(255), nullable=True),
    Column("structural", String(255), nullable=True),
    Column("sum", String(255), nullable=True),
    Column("weight", Float, nullable=True),
    Column("weight_meas", Float, nullable=True)
)


citation = Table("citation",
    metadata_obj,
    Column("abstract", String(255), nullable=True),
    Column("abstract_id_CAS", String(255), nullable=True),
    Column("book_id_ISBN", String(128), nullable=True),
    Column("book_publisher", String(255), nullable=True),
    Column("book_publisher_city", String(255), nullable=True),
    Column("book_title", String(255), nullable=True),
    Column("coordinate_linkage", String(10), nullable=True),
    Column("country", String(128), nullable=True),
    Column("database_id_Medline", Integer, nullable=True),
    Column("details", String(255), nullable=True),
    Column("journal_abbrev", String(128), nullable=True),
    Column("journal_id_ASTM", String(128), nullable=True),
    Column("journal_id_CSD", String(128), nullable=True),
    Column("journal_id_ISSN", String(128), nullable=True),
    Column("journal_full", String(255), nullable=True),
    Column("journal_issue", String(128), nullable=True),
    Column("journal_volume", String(128), nullable=True),
    Column("language", String(128), nullable=True),
    Column("page_first", String(128), nullable=True),
    Column("page_last", String(128), nullable=True),
    Column("title", String(255), nullable=True),
    Column("year", Integer, nullable=True),
    Column("database_id_CSD", String(20), nullable=True),
    Column("pdbx_database_id_DOI", String(20), nullable=True),
    Column("pdbx_database_id_PubMed", Integer, nullable=True),
    Column("pdbx_database_id_patent", String(128), nullable=True),
    Column("unpublished_flag", String(20), nullable=True)
)


citation_author = Table("citation_author",
    metadata_obj,
    Column("citation_id", String(20), primary_key=True),
    Column("name", String(128), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("identifier_ORCID", String(20), nullable=True)
)


citation_editor = Table("citation_editor",
    metadata_obj,
    Column("citation_id", String(20), primary_key=True),
    Column("name", String(128), primary_key=True),
    Column("ordinal", Integer, nullable=True)
)


computing = Table("computing",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cell_refinement", String(255), nullable=True),
    Column("data_collection", String(255), nullable=True),
    Column("data_reduction", String(255), nullable=True),
    Column("molecular_graphics", String(255), nullable=True),
    Column("publication_material", String(255), nullable=True),
    Column("structure_refinement", String(255), nullable=True),
    Column("structure_solution", String(255), nullable=True),
    Column("pdbx_structure_refinement_method", String(255), nullable=True),
    Column("pdbx_data_reduction_ii", String(255), nullable=True),
    Column("pdbx_data_reduction_ds", String(255), nullable=True)
)


database_2 = Table("database_2",
    metadata_obj,
    Column("database_id", String(10), primary_key=True),
    Column("database_code", String(128), primary_key=True),
    Column("pdbx_database_accession", String(20), nullable=True),
    Column("pdbx_DOI", String(128), nullable=True)
)


database_PDB_caveat = Table("database_PDB_caveat",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("text", String(255), nullable=True)
)


database_PDB_matrix = Table("database_PDB_matrix",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("origx[1][1]", Float, nullable=True, default=1.0),
    Column("origx[1][2]", Float, nullable=True, default=0.0),
    Column("origx[1][3]", Float, nullable=True, default=0.0),
    Column("origx[2][1]", Float, nullable=True, default=0.0),
    Column("origx[2][2]", Float, nullable=True, default=1.0),
    Column("origx[2][3]", Float, nullable=True, default=0.0),
    Column("origx[3][1]", Float, nullable=True, default=0.0),
    Column("origx[3][2]", Float, nullable=True, default=0.0),
    Column("origx[3][3]", Float, nullable=True, default=1.0),
    Column("origx_vector[1]", Float, nullable=True, default=0.0),
    Column("origx_vector[2]", Float, nullable=True, default=0.0),
    Column("origx_vector[3]", Float, nullable=True, default=0.0),
    Column("scale[1][1]", Float, nullable=True, default=1.0),
    Column("scale[1][2]", Float, nullable=True, default=0.0),
    Column("scale[1][3]", Float, nullable=True, default=0.0),
    Column("scale[2][1]", Float, nullable=True, default=0.0),
    Column("scale[2][2]", Float, nullable=True, default=1.0),
    Column("scale[2][3]", Float, nullable=True, default=0.0),
    Column("scale[3][1]", Float, nullable=True, default=0.0),
    Column("scale[3][2]", Float, nullable=True, default=0.0),
    Column("scale[3][3]", Float, nullable=True, default=1.0),
    Column("scale_vector[1]", Float, nullable=True, default=0.0),
    Column("scale_vector[2]", Float, nullable=True, default=0.0),
    Column("scale_vector[3]", Float, nullable=True, default=0.0)
)


database_PDB_remark = Table("database_PDB_remark",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("text", String(255), nullable=True)
)


database_PDB_rev = Table("database_PDB_rev",
    metadata_obj,
    Column("author_name", String(128), nullable=True),
    Column("date", DateTime, nullable=True),
    Column("date_original", DateTime, nullable=True),
    Column("mod_type", Integer, nullable=True),
    Column("replaced_by", String(128), nullable=True),
    Column("replaces", String(128), nullable=True),
    Column("status", String(50), nullable=True),
    Column("pdbx_record_revised_1", String(20), nullable=True),
    Column("pdbx_record_revised_2", String(20), nullable=True),
    Column("pdbx_record_revised_3", String(20), nullable=True),
    Column("pdbx_record_revised_4", String(20), nullable=True)
)


database_PDB_rev_record = Table("database_PDB_rev_record",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("rev_num", Integer, primary_key=True),
    Column("type", String(128), primary_key=True)
)


database_PDB_tvect = Table("database_PDB_tvect",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("vector[1]", Float, nullable=True, default=0.0),
    Column("vector[2]", Float, nullable=True, default=0.0),
    Column("vector[3]", Float, nullable=True, default=0.0)
)


diffrn = Table("diffrn",
    metadata_obj,
    Column("ambient_environment", String(128), nullable=True),
    Column("ambient_temp", Float, nullable=True),
    Column("ambient_temp_details", String(255), nullable=True),
    Column("ambient_temp_esd", Float, nullable=True),
    Column("crystal_id", String(20)),
    Column("crystal_support", String(255), nullable=True),
    Column("crystal_treatment", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("ambient_pressure", Float, nullable=True),
    Column("ambient_pressure_esd", Float, nullable=True),
    Column("ambient_pressure_gt", Float, nullable=True),
    Column("ambient_pressure_lt", Float, nullable=True),
    Column("ambient_temp_gt", Float, nullable=True),
    Column("ambient_temp_lt", Float, nullable=True),
    Column("pdbx_serial_crystal_experiment", String(255), nullable=True)
)


diffrn_attenuator = Table("diffrn_attenuator",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("scale", Float, nullable=True),
    Column("material", String(255), nullable=True)
)


diffrn_detector = Table("diffrn_detector",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("detector", String(255), nullable=True),
    Column("diffrn_id", String(20), primary_key=True),
    Column("type", String(255), nullable=True),
    Column("area_resol_mean", Float, nullable=True),
    Column("dtime", Float, nullable=True),
    Column("pdbx_frames_total", Integer, nullable=True),
    Column("pdbx_collection_time_total", Float, nullable=True),
    Column("pdbx_collection_date", DateTime, nullable=True),
    Column("pdbx_frequency", Float, nullable=True),
    Column("number_of_axes", Integer, nullable=True)
)


diffrn_measurement = Table("diffrn_measurement",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("device", String(255), nullable=True),
    Column("device_details", String(255), nullable=True),
    Column("device_type", String(255), nullable=True),
    Column("method", String(255), nullable=True),
    Column("specimen_support", String(255), nullable=True),
    Column("pdbx_date", DateTime, nullable=True)
)


diffrn_orient_matrix = Table("diffrn_orient_matrix",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("type", String(255), nullable=True),
    Column("UB[1][1]", Float, nullable=True),
    Column("UB[1][2]", Float, nullable=True),
    Column("UB[1][3]", Float, nullable=True),
    Column("UB[2][1]", Float, nullable=True),
    Column("UB[2][2]", Float, nullable=True),
    Column("UB[2][3]", Float, nullable=True),
    Column("UB[3][1]", Float, nullable=True),
    Column("UB[3][2]", Float, nullable=True),
    Column("UB[3][3]", Float, nullable=True)
)


diffrn_orient_refln = Table("diffrn_orient_refln",
    metadata_obj,
    Column("angle_chi", Float, nullable=True),
    Column("angle_kappa", Float, nullable=True),
    Column("angle_omega", Float, nullable=True),
    Column("angle_phi", Float, nullable=True),
    Column("angle_psi", Float, nullable=True),
    Column("angle_theta", Float, nullable=True),
    Column("diffrn_id", String(20), primary_key=True),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True)
)


diffrn_radiation = Table("diffrn_radiation",
    metadata_obj,
    Column("collimation", String(255), nullable=True),
    Column("diffrn_id", String(20), primary_key=True),
    Column("filter_edge", Float, nullable=True),
    Column("inhomogeneity", Float, nullable=True),
    Column("monochromator", String(255), nullable=True),
    Column("polarisn_norm", Float, nullable=True),
    Column("polarisn_ratio", Float, nullable=True),
    Column("probe", String(128), nullable=True),
    Column("type", String(128), nullable=True),
    Column("xray_symbol", String(128), nullable=True),
    Column("wavelength_id", String(20), nullable=True),
    Column("pdbx_monochromatic_or_laue_m_l", String(20), nullable=True, default="M"),
    Column("pdbx_wavelength_list", String(128), nullable=True),
    Column("pdbx_wavelength", String(128), nullable=True),
    Column("pdbx_diffrn_protocol", String(128), nullable=True, default="SINGLE WAVELENGTH"),
    Column("pdbx_analyzer", String(255), nullable=True),
    Column("pdbx_scattering_type", String(128), nullable=True)
)


diffrn_radiation_wavelength = Table("diffrn_radiation_wavelength",
    metadata_obj,
    Column("wavelength", Float),
    Column("wt", Float, nullable=True, default=1.0)
)


diffrn_refln = Table("diffrn_refln",
    metadata_obj,
    Column("angle_chi", Float, nullable=True),
    Column("angle_kappa", Float, nullable=True),
    Column("angle_omega", Float, nullable=True),
    Column("angle_phi", Float, nullable=True),
    Column("angle_psi", Float, nullable=True),
    Column("angle_theta", Float, nullable=True),
    Column("attenuator_code", String(20), nullable=True),
    Column("counts_bg_1", Integer, nullable=True),
    Column("counts_bg_2", Integer, nullable=True),
    Column("counts_net", Integer, nullable=True),
    Column("counts_peak", Integer, nullable=True),
    Column("counts_total", Integer, nullable=True),
    Column("detect_slit_horiz", Float, nullable=True),
    Column("detect_slit_vert", Float, nullable=True),
    Column("diffrn_id", String(20), primary_key=True),
    Column("elapsed_time", Float, nullable=True),
    Column("id", String(20), primary_key=True),
    Column("index_h", Integer),
    Column("index_k", Integer),
    Column("index_l", Integer),
    Column("intensity_net", Float, nullable=True),
    Column("intensity_sigma", Float, nullable=True),
    Column("scale_group_code", String(20), nullable=True),
    Column("scan_mode", String(10), nullable=True),
    Column("scan_mode_backgd", String(10), nullable=True),
    Column("scan_rate", Float, nullable=True),
    Column("scan_time_backgd", Float, nullable=True),
    Column("scan_width", Float, nullable=True),
    Column("sint_over_lambda", Float, nullable=True),
    Column("standard_code", String(20), nullable=True),
    Column("wavelength", Float, nullable=True),
    Column("wavelength_id", String(20), nullable=True),
    Column("pdbx_image_id", Integer, nullable=True),
    Column("pdbx_scan_angle", Float, nullable=True),
    Column("class_code", String(20), nullable=True),
    Column("intensity_u", Float, nullable=True),
    Column("pdbx_detector_x", Float, nullable=True),
    Column("pdbx_detector_y", Float, nullable=True),
    Column("pdbx_rotation_angle", Float, nullable=True),
    Column("pdbx_scale_value", Float, nullable=True),
    Column("frame_id", String(20), nullable=True),
    Column("pdbx_batch_id", String(20), nullable=True),
    Column("pdbx_detector_obs_fast", Float, nullable=True),
    Column("pdbx_detector_obs_slow", Float, nullable=True),
    Column("pdbx_detector_calc_fast", Float, nullable=True),
    Column("pdbx_detector_calc_slow", Float, nullable=True),
    Column("pdbx_panel_mapping_id", String(20), nullable=True)
)


diffrn_reflns = Table("diffrn_reflns",
    metadata_obj,
    Column("av_R_equivalents", Float, nullable=True),
    Column("av_sigmaI_over_netI", Float, nullable=True),
    Column("diffrn_id", String(20), primary_key=True),
    Column("limit_h_max", Integer, nullable=True),
    Column("limit_h_min", Integer, nullable=True),
    Column("limit_k_max", Integer, nullable=True),
    Column("limit_k_min", Integer, nullable=True),
    Column("limit_l_max", Integer, nullable=True),
    Column("limit_l_min", Integer, nullable=True),
    Column("number", Integer, nullable=True),
    Column("reduction_process", String(255), nullable=True),
    Column("theta_max", Float, nullable=True),
    Column("theta_min", Float, nullable=True),
    Column("transf_matrix[1][1]", Float, nullable=True),
    Column("transf_matrix[1][2]", Float, nullable=True),
    Column("transf_matrix[1][3]", Float, nullable=True),
    Column("transf_matrix[2][1]", Float, nullable=True),
    Column("transf_matrix[2][2]", Float, nullable=True),
    Column("transf_matrix[2][3]", Float, nullable=True),
    Column("transf_matrix[3][1]", Float, nullable=True),
    Column("transf_matrix[3][2]", Float, nullable=True),
    Column("transf_matrix[3][3]", Float, nullable=True),
    Column("av_unetI/netI", Float, nullable=True),
    Column("pdbx_d_res_low", Float, nullable=True),
    Column("pdbx_d_res_high", Float, nullable=True),
    Column("pdbx_percent_possible_obs", Float, nullable=True),
    Column("pdbx_Rmerge_I_obs", Float, nullable=True),
    Column("pdbx_Rsym_value", Float, nullable=True),
    Column("pdbx_chi_squared", Float, nullable=True),
    Column("pdbx_redundancy", Float, nullable=True),
    Column("pdbx_rejects", Integer, nullable=True),
    Column("pdbx_observed_criterion", Float, nullable=True),
    Column("pdbx_number_obs", Integer, nullable=True)
)


diffrn_scale_group = Table("diffrn_scale_group",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("I_net", Float, nullable=True)
)


diffrn_source = Table("diffrn_source",
    metadata_obj,
    Column("current", Float, nullable=True),
    Column("details", String(255), nullable=True),
    Column("diffrn_id", String(20), primary_key=True),
    Column("power", Float, nullable=True),
    Column("size", String(255), nullable=True),
    Column("source", String(255), nullable=True),
    Column("target", String(20), nullable=True),
    Column("type", String(255), nullable=True),
    Column("voltage", Float, nullable=True),
    Column("take-off_angle", Float, nullable=True),
    Column("pdbx_wavelength_list", String(128), nullable=True),
    Column("pdbx_wavelength", String(128), nullable=True),
    Column("pdbx_synchrotron_beamline", String(128), nullable=True),
    Column("pdbx_synchrotron_site", String(128), nullable=True),
    Column("pdbx_synchrotron_y_n", String(255), nullable=True),
    Column("pdbx_source_specific_beamline", String(255), nullable=True)
)


diffrn_standard_refln = Table("diffrn_standard_refln",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("index_h", Integer),
    Column("index_k", Integer),
    Column("index_l", Integer)
)


diffrn_standards = Table("diffrn_standards",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("decay_%", Float, nullable=True),
    Column("interval_count", Integer, nullable=True),
    Column("interval_time", Float, nullable=True),
    Column("number", Integer, nullable=True),
    Column("scale_sigma", Float, nullable=True),
    Column("scale_u", Float, nullable=True)
)


entity = Table("entity",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("formula_weight", Float, nullable=True),
    Column("src_method", String(10), nullable=True),
    Column("type", String(10), nullable=True),
    Column("pdbx_description", String(128), nullable=True),
    Column("pdbx_number_of_molecules", Integer, nullable=True),
    Column("pdbx_parent_entity_id", String(20), nullable=True),
    Column("pdbx_mutation", String(128), nullable=True),
    Column("pdbx_fragment", String(128), nullable=True),
    Column("pdbx_ec", String(10), nullable=True),
    Column("pdbx_modification", String(128), nullable=True),
    Column("pdbx_formula_weight_exptl", Float, nullable=True),
    Column("pdbx_formula_weight_exptl_method", String(128), nullable=True),
    Column("pdbx_target_id", String(20), nullable=True),
    Column("pdbx_entities_per_biological_unit", Float, nullable=True)
)


entity_keywords = Table("entity_keywords",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("text", String(255), nullable=True),
    Column("pdbx_mutation", String(128), nullable=True),
    Column("pdbx_fragment", String(128), nullable=True),
    Column("pdbx_ec", String(128), nullable=True),
    Column("pdbx_antibody_isotype", String(255), nullable=True)
)


entity_link = Table("entity_link",
    metadata_obj,
    Column("link_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("entity_id_1", String(20)),
    Column("entity_id_2", String(20)),
    Column("entity_seq_num_1", Integer, nullable=True),
    Column("entity_seq_num_2", Integer, nullable=True)
)


entity_name_com = Table("entity_name_com",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("name", String(255), nullable=True),
    Column("pdbx_provenance", String(128), nullable=True)
)


entity_name_sys = Table("entity_name_sys",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("name", String(255), nullable=True),
    Column("system", String(255), nullable=True)
)


entity_poly = Table("entity_poly",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("nstd_chirality", String(10), nullable=True),
    Column("nstd_linkage", String(10), nullable=True),
    Column("nstd_monomer", String(10), nullable=True),
    Column("number_of_monomers", Integer, nullable=True),
    Column("type", String(128), nullable=True),
    Column("type_details", String(255), nullable=True),
    Column("pdbx_strand_id", String(128), nullable=True),
    Column("pdbx_seq_one_letter_code", String(255), nullable=True),
    Column("pdbx_seq_one_letter_code_can", String(255), nullable=True),
    Column("pdbx_target_identifier", String(128), nullable=True),
    Column("pdbx_seq_one_letter_code_sample", String(255), nullable=True),
    Column("pdbx_explicit_linking_flag", String(10), nullable=True, default="N"),
    Column("pdbx_sequence_evidence_code", String(128), nullable=True),
    Column("pdbx_build_self_reference", String(2), nullable=True),
    Column("pdbx_N_terminal_seq_one_letter_code", String(255), nullable=True),
    Column("pdbx_C_terminal_seq_one_letter_code", String(255), nullable=True),
    Column("pdbx_seq_three_letter_code", String(255), nullable=True),
    Column("pdbx_seq_db_name", String(128), nullable=True),
    Column("pdbx_seq_db_id", String(128), nullable=True),
    Column("pdbx_seq_align_begin", Integer, nullable=True),
    Column("pdbx_seq_align_end", Integer, nullable=True)
)


entity_poly_seq = Table("entity_poly_seq",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("hetero", String(10), nullable=True, default="no"),
    Column("mon_id", String(10), primary_key=True)
)


entry = Table("entry",
    metadata_obj,
    Column("pdbx_DOI", String(20), nullable=True)
)


entry_link = Table("entry_link",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("details", String(255), nullable=True)
)


exptl = Table("exptl",
    metadata_obj,
    Column("absorpt_coefficient_mu", Float, nullable=True),
    Column("absorpt_correction_T_max", Float, nullable=True),
    Column("absorpt_correction_T_min", Float, nullable=True),
    Column("absorpt_correction_type", String(10), nullable=True),
    Column("absorpt_process_details", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("crystals_number", Integer, nullable=True),
    Column("details", String(255), nullable=True),
    Column("method", String(128), primary_key=True),
    Column("method_details", String(255), nullable=True)
)


exptl_crystal = Table("exptl_crystal",
    metadata_obj,
    Column("colour", String(128), nullable=True),
    Column("density_diffrn", Float, nullable=True),
    Column("density_Matthews", Float, nullable=True),
    Column("density_method", String(255), nullable=True),
    Column("density_percent_sol", Float, nullable=True),
    Column("description", String(255), nullable=True),
    Column("F_000", Integer, nullable=True),
    Column("preparation", String(255), nullable=True),
    Column("size_max", Float, nullable=True),
    Column("size_mid", Float, nullable=True),
    Column("size_min", Float, nullable=True),
    Column("size_rad", Float, nullable=True),
    Column("colour_lustre", String(128), nullable=True),
    Column("colour_modifier", String(128), nullable=True),
    Column("colour_primary", String(128), nullable=True),
    Column("density_meas", Float, nullable=True),
    Column("density_meas_esd", Float, nullable=True),
    Column("density_meas_gt", Float, nullable=True),
    Column("density_meas_lt", Float, nullable=True),
    Column("density_meas_temp", Float, nullable=True),
    Column("density_meas_temp_esd", Float, nullable=True),
    Column("density_meas_temp_gt", Float, nullable=True),
    Column("density_meas_temp_lt", Float, nullable=True),
    Column("pdbx_crystal_image_url", String(128), nullable=True),
    Column("pdbx_crystal_image_format", String(128), nullable=True),
    Column("pdbx_mosaicity", Float, nullable=True),
    Column("pdbx_mosaicity_esd", Float, nullable=True),
    Column("pdbx_crystal_image", String(20), nullable=True),
    Column("pdbx_x-ray_image", String(20), nullable=True),
    Column("pdbx_x-ray_image_type", String(255), nullable=True),
    Column("pdbx_crystal_diffrn_limit", Float, nullable=True),
    Column("pdbx_crystal_diffrn_lifetime", Float, nullable=True),
    Column("pdbx_crystal_direction_1", Float, nullable=True),
    Column("pdbx_crystal_direction_2", Float, nullable=True),
    Column("pdbx_crystal_direction_3", Float, nullable=True),
    Column("pdbx_mosaic_method", String(10), nullable=True),
    Column("pdbx_mosaic_block_size", Float, nullable=True),
    Column("pdbx_mosaic_block_size_esd", Float, nullable=True)
)


exptl_crystal_face = Table("exptl_crystal_face",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("diffr_chi", Float, nullable=True),
    Column("diffr_kappa", Float, nullable=True),
    Column("diffr_phi", Float, nullable=True),
    Column("diffr_psi", Float, nullable=True),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("perp_dist", Float, nullable=True)
)


exptl_crystal_grow = Table("exptl_crystal_grow",
    metadata_obj,
    Column("apparatus", String(255), nullable=True),
    Column("atmosphere", String(255), nullable=True),
    Column("crystal_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("method", String(255), nullable=True),
    Column("method_ref", String(255), nullable=True),
    Column("pH", Float, nullable=True),
    Column("pressure", Float, nullable=True),
    Column("pressure_esd", Float, nullable=True),
    Column("seeding", String(255), nullable=True),
    Column("seeding_ref", String(255), nullable=True),
    Column("temp_details", String(255), nullable=True),
    Column("temp_esd", Float, nullable=True),
    Column("time", String(255), nullable=True),
    Column("pdbx_details", String(255), nullable=True),
    Column("pdbx_pH_range", String(128), nullable=True),
    Column("temp", Float, nullable=True)
)


exptl_crystal_grow_comp = Table("exptl_crystal_grow_comp",
    metadata_obj,
    Column("conc", String(128), nullable=True),
    Column("details", String(255), nullable=True),
    Column("crystal_id", String(20), primary_key=True),
    Column("id", String(128), primary_key=True),
    Column("name", String(128), nullable=True),
    Column("sol_id", String(128), nullable=True),
    Column("volume", String(128), nullable=True),
    Column("pdbx_conc_final", String(128), nullable=True),
    Column("pdbx_bath", String(128), nullable=True),
    Column("pdbx_salt", String(128), nullable=True),
    Column("pdbx_soak_salt", String(128), nullable=True),
    Column("pdbx_soak_solv", String(128), nullable=True),
    Column("pdbx_solv", String(128), nullable=True)
)


geom = Table("geom",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True)
)


geom_angle = Table("geom_angle",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20), nullable=True),
    Column("atom_site_label_atom_id_1", String(6), nullable=True),
    Column("atom_site_label_comp_id_1", String(10), nullable=True),
    Column("atom_site_label_seq_id_1", Integer, nullable=True),
    Column("atom_site_label_asym_id_1", String(20), nullable=True),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20), nullable=True),
    Column("atom_site_label_atom_id_2", String(6), nullable=True),
    Column("atom_site_label_comp_id_2", String(10), nullable=True),
    Column("atom_site_label_seq_id_2", Integer, nullable=True),
    Column("atom_site_label_asym_id_2", String(20), nullable=True),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20), nullable=True),
    Column("atom_site_label_atom_id_3", String(6), nullable=True),
    Column("atom_site_label_comp_id_3", String(10), nullable=True),
    Column("atom_site_label_seq_id_3", Integer, nullable=True),
    Column("atom_site_label_asym_id_3", String(20), nullable=True),
    Column("atom_site_auth_asym_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_1", String(6), nullable=True),
    Column("atom_site_auth_comp_id_1", String(20), nullable=True),
    Column("atom_site_auth_seq_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_2", String(6), nullable=True),
    Column("atom_site_auth_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_comp_id_2", String(20), nullable=True),
    Column("atom_site_auth_seq_id_2", String(20), nullable=True),
    Column("atom_site_auth_atom_id_3", String(6), nullable=True),
    Column("atom_site_auth_asym_id_3", String(20), nullable=True),
    Column("atom_site_auth_comp_id_3", String(20), nullable=True),
    Column("atom_site_auth_seq_id_3", String(20), nullable=True),
    Column("publ_flag", String(10), nullable=True),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("value", Float, nullable=True),
    Column("value_esd", Float, nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20), nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20), nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_3", String(20), nullable=True),
    Column("pdbx_PDB_model_num", Integer, nullable=True)
)


geom_bond = Table("geom_bond",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20), nullable=True),
    Column("atom_site_label_atom_id_1", String(6), nullable=True),
    Column("atom_site_label_comp_id_1", String(10), nullable=True),
    Column("atom_site_label_seq_id_1", Integer, nullable=True),
    Column("atom_site_label_asym_id_1", String(20), nullable=True),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20), nullable=True),
    Column("atom_site_label_atom_id_2", String(6), nullable=True),
    Column("atom_site_label_comp_id_2", String(10), nullable=True),
    Column("atom_site_label_seq_id_2", Integer, nullable=True),
    Column("atom_site_label_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_atom_id_1", String(6), nullable=True),
    Column("atom_site_auth_asym_id_1", String(20), nullable=True),
    Column("atom_site_auth_comp_id_1", String(20), nullable=True),
    Column("atom_site_auth_seq_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_2", String(6), nullable=True),
    Column("atom_site_auth_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_comp_id_2", String(20), nullable=True),
    Column("atom_site_auth_seq_id_2", String(20), nullable=True),
    Column("dist", Float, nullable=True),
    Column("dist_esd", Float, nullable=True),
    Column("publ_flag", String(10), nullable=True),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("valence", Integer, nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20), nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20), nullable=True),
    Column("pdbx_PDB_model_num", Integer, nullable=True)
)


geom_contact = Table("geom_contact",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20), nullable=True),
    Column("atom_site_label_atom_id_1", String(6), nullable=True),
    Column("atom_site_label_comp_id_1", String(10), nullable=True),
    Column("atom_site_label_seq_id_1", Integer, nullable=True),
    Column("atom_site_label_asym_id_1", String(20), nullable=True),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20), nullable=True),
    Column("atom_site_label_atom_id_2", String(6), nullable=True),
    Column("atom_site_label_comp_id_2", String(10), nullable=True),
    Column("atom_site_label_seq_id_2", Integer, nullable=True),
    Column("atom_site_label_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_atom_id_1", String(6), nullable=True),
    Column("atom_site_auth_asym_id_1", String(20), nullable=True),
    Column("atom_site_auth_comp_id_1", String(20), nullable=True),
    Column("atom_site_auth_seq_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_2", String(6), nullable=True),
    Column("atom_site_auth_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_comp_id_2", String(20), nullable=True),
    Column("atom_site_auth_seq_id_2", String(20), nullable=True),
    Column("dist", Float, nullable=True),
    Column("dist_esd", Float, nullable=True),
    Column("publ_flag", String(10), nullable=True),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20), nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20), nullable=True),
    Column("pdbx_PDB_model_num", Integer, nullable=True)
)


geom_hbond = Table("geom_hbond",
    metadata_obj,
    Column("angle_DHA", Float, nullable=True),
    Column("angle_DHA_esd", Float, nullable=True),
    Column("atom_site_id_A", String(20), primary_key=True),
    Column("atom_site_label_alt_id_A", String(20), nullable=True),
    Column("atom_site_label_asym_id_A", String(20), nullable=True),
    Column("atom_site_label_atom_id_A", String(6), nullable=True),
    Column("atom_site_label_comp_id_A", String(10), nullable=True),
    Column("atom_site_label_seq_id_A", Integer, nullable=True),
    Column("atom_site_id_D", String(20), primary_key=True),
    Column("atom_site_label_alt_id_D", String(20), nullable=True),
    Column("atom_site_label_asym_id_D", String(20), nullable=True),
    Column("atom_site_label_atom_id_D", String(6), nullable=True),
    Column("atom_site_label_comp_id_D", String(10), nullable=True),
    Column("atom_site_label_seq_id_D", Integer, nullable=True),
    Column("atom_site_id_H", String(20), primary_key=True),
    Column("atom_site_label_alt_id_H", String(20), nullable=True),
    Column("atom_site_label_asym_id_H", String(20), nullable=True),
    Column("atom_site_label_atom_id_H", String(6), nullable=True),
    Column("atom_site_label_comp_id_H", String(10), nullable=True),
    Column("atom_site_label_seq_id_H", Integer, nullable=True),
    Column("atom_site_auth_asym_id_A", String(20), nullable=True),
    Column("atom_site_auth_atom_id_A", String(6), nullable=True),
    Column("atom_site_auth_comp_id_A", String(20), nullable=True),
    Column("atom_site_auth_seq_id_A", String(20), nullable=True),
    Column("atom_site_auth_asym_id_D", String(20), nullable=True),
    Column("atom_site_auth_atom_id_D", String(6), nullable=True),
    Column("atom_site_auth_comp_id_D", String(20), nullable=True),
    Column("atom_site_auth_seq_id_D", String(20), nullable=True),
    Column("atom_site_auth_asym_id_H", String(20), nullable=True),
    Column("atom_site_auth_atom_id_H", String(6), nullable=True),
    Column("atom_site_auth_comp_id_H", String(20), nullable=True),
    Column("atom_site_auth_seq_id_H", String(20), nullable=True),
    Column("dist_DA", Float, nullable=True),
    Column("dist_DA_esd", Float, nullable=True),
    Column("dist_DH", Float, nullable=True),
    Column("dist_DH_esd", Float, nullable=True),
    Column("dist_HA", Float, nullable=True),
    Column("dist_HA_esd", Float, nullable=True),
    Column("publ_flag", String(10), nullable=True),
    Column("site_symmetry_A", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_D", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_H", String(10), primary_key=True, default="1_555")
)


geom_torsion = Table("geom_torsion",
    metadata_obj,
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20), nullable=True),
    Column("atom_site_label_atom_id_1", String(6), nullable=True),
    Column("atom_site_label_comp_id_1", String(10), nullable=True),
    Column("atom_site_label_seq_id_1", Integer, nullable=True),
    Column("atom_site_label_asym_id_1", String(20), nullable=True),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20), nullable=True),
    Column("atom_site_label_atom_id_2", String(6), nullable=True),
    Column("atom_site_label_comp_id_2", String(10), nullable=True),
    Column("atom_site_label_seq_id_2", Integer, nullable=True),
    Column("atom_site_label_asym_id_2", String(20), nullable=True),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20), nullable=True),
    Column("atom_site_label_atom_id_3", String(6), nullable=True),
    Column("atom_site_label_comp_id_3", String(10), nullable=True),
    Column("atom_site_label_seq_id_3", Integer, nullable=True),
    Column("atom_site_label_asym_id_3", String(20), nullable=True),
    Column("atom_site_id_4", String(20), primary_key=True),
    Column("atom_site_label_alt_id_4", String(20), nullable=True),
    Column("atom_site_label_atom_id_4", String(6), nullable=True),
    Column("atom_site_label_comp_id_4", String(10), nullable=True),
    Column("atom_site_label_seq_id_4", Integer, nullable=True),
    Column("atom_site_label_asym_id_4", String(20), nullable=True),
    Column("atom_site_auth_atom_id_1", String(6), nullable=True),
    Column("atom_site_auth_asym_id_1", String(20), nullable=True),
    Column("atom_site_auth_comp_id_1", String(20), nullable=True),
    Column("atom_site_auth_seq_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_2", String(6), nullable=True),
    Column("atom_site_auth_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_comp_id_2", String(20), nullable=True),
    Column("atom_site_auth_seq_id_2", String(20), nullable=True),
    Column("atom_site_auth_atom_id_3", String(6), nullable=True),
    Column("atom_site_auth_asym_id_3", String(20), nullable=True),
    Column("atom_site_auth_comp_id_3", String(20), nullable=True),
    Column("atom_site_auth_seq_id_3", String(20), nullable=True),
    Column("atom_site_auth_atom_id_4", String(6), nullable=True),
    Column("atom_site_auth_asym_id_4", String(20), nullable=True),
    Column("atom_site_auth_comp_id_4", String(20), nullable=True),
    Column("atom_site_auth_seq_id_4", String(20), nullable=True),
    Column("publ_flag", String(10), nullable=True),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_4", String(10), primary_key=True, default="1_555"),
    Column("value", Float, nullable=True),
    Column("value_esd", Float, nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_1", String(20), nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_2", String(20), nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_3", String(20), nullable=True),
    Column("pdbx_atom_site_PDB_ins_code_4", String(20), nullable=True),
    Column("pdbx_PDB_model_num", Integer, nullable=True)
)


journal = Table("journal",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("coden_ASTM", String(128), nullable=True),
    Column("coden_Cambridge", String(128), nullable=True),
    Column("coeditor_address", String(255), nullable=True),
    Column("coeditor_code", String(128), nullable=True),
    Column("coeditor_email", String(128), nullable=True),
    Column("coeditor_fax", String(128), nullable=True),
    Column("coeditor_name", String(128), nullable=True),
    Column("coeditor_notes", String(255), nullable=True),
    Column("coeditor_phone", String(128), nullable=True),
    Column("data_validation_number", String(20), nullable=True),
    Column("date_accepted", DateTime, nullable=True),
    Column("date_from_coeditor", DateTime, nullable=True),
    Column("date_to_coeditor", DateTime, nullable=True),
    Column("date_printers_final", DateTime, nullable=True),
    Column("date_printers_first", DateTime, nullable=True),
    Column("date_proofs_in", DateTime, nullable=True),
    Column("date_proofs_out", DateTime, nullable=True),
    Column("date_recd_copyright", DateTime, nullable=True),
    Column("date_recd_electronic", DateTime, nullable=True),
    Column("date_recd_hard_copy", DateTime, nullable=True),
    Column("issue", String(128), nullable=True),
    Column("language", String(128), nullable=True),
    Column("name_full", String(128), nullable=True),
    Column("page_first", String(128), nullable=True),
    Column("page_last", String(128), nullable=True),
    Column("paper_category", String(128), nullable=True),
    Column("suppl_publ_number", String(128), nullable=True),
    Column("suppl_publ_pages", String(128), nullable=True),
    Column("techeditor_address", String(255), nullable=True),
    Column("techeditor_code", String(128), nullable=True),
    Column("techeditor_email", String(128), nullable=True),
    Column("techeditor_fax", String(128), nullable=True),
    Column("techeditor_name", String(128), nullable=True),
    Column("techeditor_notes", String(255), nullable=True),
    Column("techeditor_phone", String(128), nullable=True),
    Column("volume", String(128), nullable=True),
    Column("year", String(128), nullable=True)
)


journal_index = Table("journal_index",
    metadata_obj,
    Column("subterm", String(128), nullable=True),
    Column("term", String(128), primary_key=True),
    Column("type", String(128), primary_key=True)
)


phasing = Table("phasing",
    metadata_obj,
    Column("method", String(10), primary_key=True)
)


phasing_averaging = Table("phasing_averaging",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255), nullable=True)
)


phasing_isomorphous = Table("phasing_isomorphous",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255), nullable=True),
    Column("parent", String(255), nullable=True)
)


phasing_MAD = Table("phasing_MAD",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255), nullable=True),
    Column("pdbx_d_res_low", Float, nullable=True),
    Column("pdbx_d_res_high", Float, nullable=True),
    Column("pdbx_reflns_acentric", Integer, nullable=True),
    Column("pdbx_reflns_centric", Integer, nullable=True),
    Column("pdbx_reflns", Integer, nullable=True),
    Column("pdbx_fom_acentric", Float, nullable=True),
    Column("pdbx_fom_centric", Float, nullable=True),
    Column("pdbx_fom", Float, nullable=True),
    Column("pdbx_R_cullis_centric", Float, nullable=True),
    Column("pdbx_R_cullis_acentric", Float, nullable=True),
    Column("pdbx_R_cullis", Float, nullable=True),
    Column("pdbx_R_kraut_centric", Float, nullable=True),
    Column("pdbx_R_kraut_acentric", Float, nullable=True),
    Column("pdbx_R_kraut", Float, nullable=True),
    Column("pdbx_loc_centric", Float, nullable=True),
    Column("pdbx_loc_acentric", Float, nullable=True),
    Column("pdbx_loc", Float, nullable=True),
    Column("pdbx_power_centric", Float, nullable=True),
    Column("pdbx_power_acentric", Float, nullable=True),
    Column("pdbx_power", Float, nullable=True),
    Column("pdbx_number_data_sets", Integer, nullable=True),
    Column("pdbx_anom_scat_method", String(255), nullable=True)
)


phasing_MAD_clust = Table("phasing_MAD_clust",
    metadata_obj,
    Column("expt_id", String(128), primary_key=True),
    Column("number_set", Integer, nullable=True)
)


phasing_MAD_expt = Table("phasing_MAD_expt",
    metadata_obj,
    Column("delta_delta_phi", Float, nullable=True),
    Column("delta_phi", Float, nullable=True),
    Column("delta_phi_sigma", Float, nullable=True),
    Column("mean_fom", Float, nullable=True),
    Column("number_clust", Integer, nullable=True),
    Column("R_normal_all", Float, nullable=True),
    Column("R_normal_anom_scat", Float, nullable=True)
)


phasing_MAD_ratio = Table("phasing_MAD_ratio",
    metadata_obj,
    Column("d_res_high", Float, nullable=True),
    Column("d_res_low", Float, nullable=True),
    Column("expt_id", String(128), primary_key=True),
    Column("clust_id", String(128), primary_key=True),
    Column("ratio_one_wl", Float, nullable=True),
    Column("ratio_one_wl_centric", Float, nullable=True),
    Column("ratio_two_wl", Float, nullable=True),
    Column("wavelength_1", Float, primary_key=True),
    Column("wavelength_2", Float, primary_key=True)
)


phasing_MAD_set = Table("phasing_MAD_set",
    metadata_obj,
    Column("clust_id", String(128), primary_key=True),
    Column("d_res_high", Float, nullable=True),
    Column("d_res_low", Float, nullable=True),
    Column("expt_id", String(128), primary_key=True),
    Column("f_double_prime", Float, nullable=True),
    Column("f_prime", Float, nullable=True),
    Column("set_id", String(128), primary_key=True),
    Column("wavelength_details", String(255), nullable=True),
    Column("pdbx_atom_type", String(20), nullable=True),
    Column("pdbx_f_prime_refined", Float, nullable=True),
    Column("pdbx_f_double_prime_refined", Float, nullable=True)
)


phasing_MIR = Table("phasing_MIR",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("entry_id", String(20), primary_key=True),
    Column("FOM", Float, nullable=True),
    Column("FOM_acentric", Float, nullable=True),
    Column("FOM_centric", Float, nullable=True),
    Column("method", String(255), nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("reflns_acentric", Integer, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("reflns_criterion", String(255), nullable=True),
    Column("pdbx_number_derivatives", Integer, nullable=True)
)


phasing_MIR_der = Table("phasing_MIR_der",
    metadata_obj,
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("der_set_id", String(128)),
    Column("details", String(255), nullable=True),
    Column("native_set_id", String(128)),
    Column("number_of_sites", Integer, nullable=True),
    Column("power_acentric", Float, nullable=True),
    Column("power_centric", Float, nullable=True),
    Column("R_cullis_acentric", Float, nullable=True),
    Column("R_cullis_anomalous", Float, nullable=True),
    Column("R_cullis_centric", Float, nullable=True),
    Column("reflns_acentric", Integer, nullable=True),
    Column("reflns_anomalous", Integer, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("reflns_criteria", String(255), nullable=True),
    Column("pdbx_R_kraut_centric", Float, nullable=True),
    Column("pdbx_R_kraut_acentric", Float, nullable=True),
    Column("pdbx_R_kraut", Float, nullable=True),
    Column("pdbx_loc_centric", Float, nullable=True),
    Column("pdbx_loc_acentric", Float, nullable=True),
    Column("pdbx_loc", Float, nullable=True),
    Column("pdbx_fom_centric", Float, nullable=True),
    Column("pdbx_fom_acentric", Float, nullable=True),
    Column("pdbx_fom", Float, nullable=True),
    Column("pdbx_power", Float, nullable=True),
    Column("pdbx_R_cullis", Float, nullable=True),
    Column("pdbx_reflns", Integer, nullable=True)
)


phasing_MIR_der_refln = Table("phasing_MIR_der_refln",
    metadata_obj,
    Column("der_id", String(128), primary_key=True),
    Column("F_calc", Float, nullable=True),
    Column("F_calc_au", Float, nullable=True),
    Column("F_meas", Float, nullable=True),
    Column("F_meas_au", Float, nullable=True),
    Column("F_meas_sigma", Float, nullable=True),
    Column("F_meas_sigma_au", Float, nullable=True),
    Column("HL_A_iso", Float, nullable=True),
    Column("HL_B_iso", Float, nullable=True),
    Column("HL_C_iso", Float, nullable=True),
    Column("HL_D_iso", Float, nullable=True),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("phase_calc", Float, nullable=True),
    Column("set_id", String(128), primary_key=True)
)


phasing_MIR_der_shell = Table("phasing_MIR_der_shell",
    metadata_obj,
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("der_id", String(128), primary_key=True),
    Column("fom", Float, nullable=True),
    Column("ha_ampl", Float, nullable=True),
    Column("loc", Float, nullable=True),
    Column("phase", Float, nullable=True),
    Column("power", Float, nullable=True),
    Column("R_cullis", Float, nullable=True),
    Column("R_kraut", Float, nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("pdbx_R_cullis_centric", Float, nullable=True),
    Column("pdbx_R_cullis_acentric", Float, nullable=True),
    Column("pdbx_R_kraut_centric", Float, nullable=True),
    Column("pdbx_R_kraut_acentric", Float, nullable=True),
    Column("pdbx_loc_centric", Float, nullable=True),
    Column("pdbx_loc_acentric", Float, nullable=True),
    Column("pdbx_power_centric", Float, nullable=True),
    Column("pdbx_power_acentric", Float, nullable=True),
    Column("pdbx_fom_centric", Float, nullable=True),
    Column("pdbx_fom_acentric", Float, nullable=True),
    Column("pdbx_reflns_centric", Float, nullable=True),
    Column("pdbx_reflns_acentric", Integer, nullable=True)
)


phasing_MIR_der_site = Table("phasing_MIR_der_site",
    metadata_obj,
    Column("atom_type_symbol", String(20)),
    Column("B_iso", Float, nullable=True),
    Column("B_iso_esd", Float, nullable=True),
    Column("Cartn_x", Float, nullable=True),
    Column("Cartn_x_esd", Float, nullable=True),
    Column("Cartn_y", Float, nullable=True),
    Column("Cartn_y_esd", Float, nullable=True),
    Column("Cartn_z", Float, nullable=True),
    Column("Cartn_z_esd", Float, nullable=True),
    Column("der_id", String(128), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("fract_x", Float, nullable=True),
    Column("fract_x_esd", Float, nullable=True),
    Column("fract_y", Float, nullable=True),
    Column("fract_y_esd", Float, nullable=True),
    Column("fract_z", Float, nullable=True),
    Column("fract_z_esd", Float, nullable=True),
    Column("id", String(20), primary_key=True),
    Column("occupancy", Float, nullable=True, default=1.0),
    Column("occupancy_anom", Float, nullable=True),
    Column("occupancy_anom_su", Float, nullable=True),
    Column("occupancy_iso", Float, nullable=True),
    Column("occupancy_iso_su", Float, nullable=True)
)


phasing_MIR_shell = Table("phasing_MIR_shell",
    metadata_obj,
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("FOM", Float, nullable=True),
    Column("FOM_acentric", Float, nullable=True),
    Column("FOM_centric", Float, nullable=True),
    Column("loc", Float, nullable=True),
    Column("mean_phase", Float, nullable=True),
    Column("power", Float, nullable=True),
    Column("R_cullis", Float, nullable=True),
    Column("R_kraut", Float, nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("reflns_acentric", Integer, nullable=True),
    Column("reflns_anomalous", Integer, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("pdbx_loc_centric", Float, nullable=True),
    Column("pdbx_loc_acentric", Float, nullable=True),
    Column("pdbx_power_centric", Float, nullable=True),
    Column("pdbx_power_acentric", Float, nullable=True),
    Column("pdbx_R_kraut_centric", Float, nullable=True),
    Column("pdbx_R_kraut_acentric", Float, nullable=True),
    Column("pdbx_R_cullis_centric", Float, nullable=True),
    Column("pdbx_R_cullis_acentric", Float, nullable=True)
)


phasing_set = Table("phasing_set",
    metadata_obj,
    Column("cell_angle_alpha", Float, nullable=True, default=90.0),
    Column("cell_angle_beta", Float, nullable=True, default=90.0),
    Column("cell_angle_gamma", Float, nullable=True, default=90.0),
    Column("cell_length_a", Float, nullable=True),
    Column("cell_length_b", Float, nullable=True),
    Column("cell_length_c", Float, nullable=True),
    Column("detector_specific", String(255), nullable=True),
    Column("detector_type", String(255), nullable=True),
    Column("radiation_source_specific", String(255), nullable=True),
    Column("radiation_wavelength", Float, nullable=True),
    Column("temp", Float, nullable=True),
    Column("pdbx_temp_details", String(255), nullable=True),
    Column("pdbx_d_res_high", Float),
    Column("pdbx_d_res_low", Float)
)


phasing_set_refln = Table("phasing_set_refln",
    metadata_obj,
    Column("set_id", String(128), primary_key=True),
    Column("F_meas", Float, nullable=True),
    Column("F_meas_au", Float, nullable=True),
    Column("F_meas_sigma", Float, nullable=True),
    Column("F_meas_sigma_au", Float, nullable=True),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True)
)


publ = Table("publ",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("contact_author", String(255), nullable=True),
    Column("contact_author_address", String(255), nullable=True),
    Column("contact_author_email", String(128), nullable=True),
    Column("contact_author_fax", String(128), nullable=True),
    Column("contact_author_name", String(255), nullable=True),
    Column("contact_author_phone", String(128), nullable=True),
    Column("contact_letter", String(255), nullable=True),
    Column("manuscript_creation", String(255), nullable=True),
    Column("manuscript_processed", String(255), nullable=True),
    Column("manuscript_text", String(255), nullable=True),
    Column("requested_category", String(128), nullable=True, default="FA"),
    Column("requested_coeditor_name", String(128), nullable=True),
    Column("requested_journal", String(128), nullable=True),
    Column("section_abstract", String(255), nullable=True),
    Column("section_acknowledgements", String(255), nullable=True),
    Column("section_comment", String(255), nullable=True),
    Column("section_discussion", String(255), nullable=True),
    Column("section_experimental", String(255), nullable=True),
    Column("section_exptl_prep", String(255), nullable=True),
    Column("section_exptl_refinement", String(255), nullable=True),
    Column("section_exptl_solution", String(255), nullable=True),
    Column("section_figure_captions", String(255), nullable=True),
    Column("section_introduction", String(255), nullable=True),
    Column("section_references", String(255), nullable=True),
    Column("section_synopsis", String(255), nullable=True),
    Column("section_table_legends", String(255), nullable=True),
    Column("section_title", String(255), nullable=True),
    Column("section_title_footnote", String(255), nullable=True)
)


publ_author = Table("publ_author",
    metadata_obj,
    Column("address", String(255), nullable=True),
    Column("email", String(255), nullable=True),
    Column("footnote", String(128), nullable=True),
    Column("name", String(128), primary_key=True),
    Column("id_iucr", String(20), nullable=True)
)


publ_body = Table("publ_body",
    metadata_obj,
    Column("contents", String(255), nullable=True),
    Column("element", String(20), primary_key=True),
    Column("format", String(20), nullable=True),
    Column("label", String(20), primary_key=True),
    Column("title", String(255), nullable=True)
)


publ_manuscript_incl = Table("publ_manuscript_incl",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("extra_defn", String(128), nullable=True),
    Column("extra_info", String(255), nullable=True),
    Column("extra_item", String(128), nullable=True)
)


refine = Table("refine",
    metadata_obj,
    Column("aniso_B[1][1]", Float, nullable=True),
    Column("aniso_B[1][2]", Float, nullable=True),
    Column("aniso_B[1][3]", Float, nullable=True),
    Column("aniso_B[2][2]", Float, nullable=True),
    Column("aniso_B[2][3]", Float, nullable=True),
    Column("aniso_B[3][3]", Float, nullable=True),
    Column("B_iso_max", Float, nullable=True),
    Column("B_iso_mean", Float, nullable=True),
    Column("B_iso_min", Float, nullable=True),
    Column("correlation_coeff_Fo_to_Fc", Float, nullable=True),
    Column("correlation_coeff_Fo_to_Fc_free", Float, nullable=True),
    Column("details", String(255), nullable=True),
    Column("diff_density_max", Float, nullable=True),
    Column("diff_density_max_esd", Float, nullable=True),
    Column("diff_density_min", Float, nullable=True),
    Column("diff_density_min_esd", Float, nullable=True),
    Column("diff_density_rms", Float, nullable=True),
    Column("diff_density_rms_esd", Float, nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("ls_abs_structure_details", String(255), nullable=True),
    Column("ls_abs_structure_Flack", Float, nullable=True),
    Column("ls_abs_structure_Flack_esd", Float, nullable=True),
    Column("ls_abs_structure_Rogers", Float, nullable=True),
    Column("ls_abs_structure_Rogers_esd", Float, nullable=True),
    Column("ls_d_res_high", Float),
    Column("ls_d_res_low", Float, nullable=True),
    Column("ls_extinction_coef", Float, nullable=True),
    Column("ls_extinction_coef_esd", Float, nullable=True),
    Column("ls_extinction_expression", String(255), nullable=True),
    Column("ls_extinction_method", String(255), nullable=True),
    Column("ls_goodness_of_fit_all", Float, nullable=True),
    Column("ls_goodness_of_fit_all_esd", Float, nullable=True),
    Column("ls_goodness_of_fit_obs", Float, nullable=True),
    Column("ls_goodness_of_fit_obs_esd", Float, nullable=True),
    Column("ls_hydrogen_treatment", String(10), nullable=True),
    Column("ls_matrix_type", String(10), nullable=True),
    Column("ls_number_constraints", Integer, nullable=True),
    Column("ls_number_parameters", Integer, nullable=True),
    Column("ls_number_reflns_all", Integer, nullable=True),
    Column("ls_number_reflns_obs", Integer, nullable=True),
    Column("ls_number_reflns_R_free", Integer, nullable=True),
    Column("ls_number_reflns_R_work", Integer, nullable=True),
    Column("ls_number_restraints", Integer, nullable=True),
    Column("ls_percent_reflns_obs", Float, nullable=True),
    Column("ls_percent_reflns_R_free", Float, nullable=True),
    Column("ls_R_factor_all", Float, nullable=True),
    Column("ls_R_factor_obs", Float, nullable=True),
    Column("ls_R_factor_R_free", Float, nullable=True),
    Column("ls_R_factor_R_free_error", Float, nullable=True),
    Column("ls_R_factor_R_free_error_details", String(255), nullable=True),
    Column("ls_R_factor_R_work", Float, nullable=True),
    Column("ls_R_Fsqd_factor_obs", Float, nullable=True),
    Column("ls_R_I_factor_obs", Float, nullable=True),
    Column("ls_redundancy_reflns_all", Float, nullable=True),
    Column("ls_redundancy_reflns_obs", Float, nullable=True),
    Column("ls_restrained_S_all", Float, nullable=True),
    Column("ls_restrained_S_obs", Float, nullable=True),
    Column("ls_shift_over_esd_max", Float, nullable=True),
    Column("ls_shift_over_esd_mean", Float, nullable=True),
    Column("ls_structure_factor_coef", String(10), nullable=True),
    Column("ls_weighting_details", String(255), nullable=True),
    Column("ls_weighting_scheme", String(10), nullable=True),
    Column("ls_wR_factor_all", Float, nullable=True),
    Column("ls_wR_factor_obs", Float, nullable=True),
    Column("ls_wR_factor_R_free", Float, nullable=True),
    Column("ls_wR_factor_R_work", Float, nullable=True),
    Column("occupancy_max", Float, nullable=True),
    Column("occupancy_min", Float, nullable=True),
    Column("solvent_model_details", String(255), nullable=True),
    Column("solvent_model_param_bsol", Float, nullable=True),
    Column("solvent_model_param_ksol", Float, nullable=True),
    Column("pdbx_R_complete", Float, nullable=True),
    Column("ls_R_factor_gt", Float, nullable=True),
    Column("ls_goodness_of_fit_gt", Float, nullable=True),
    Column("ls_goodness_of_fit_ref", Float, nullable=True),
    Column("ls_shift_over_su_max", Float, nullable=True),
    Column("ls_shift_over_su_max_lt", Float, nullable=True),
    Column("ls_shift_over_su_mean", Float, nullable=True),
    Column("ls_shift_over_su_mean_lt", Float, nullable=True),
    Column("pdbx_ls_sigma_I", Float, nullable=True),
    Column("pdbx_ls_sigma_F", Float, nullable=True),
    Column("pdbx_ls_sigma_Fsqd", Float, nullable=True),
    Column("pdbx_data_cutoff_high_absF", Float, nullable=True),
    Column("pdbx_data_cutoff_high_rms_absF", Float, nullable=True),
    Column("pdbx_data_cutoff_low_absF", Float, nullable=True),
    Column("pdbx_isotropic_thermal_model", String(255), nullable=True),
    Column("pdbx_ls_cross_valid_method", String(255), nullable=True),
    Column("pdbx_method_to_determine_struct", String(255), nullable=True),
    Column("pdbx_starting_model", String(255), nullable=True),
    Column("pdbx_stereochemistry_target_values", String(255), nullable=True),
    Column("pdbx_R_Free_selection_details", String(255), nullable=True),
    Column("pdbx_stereochem_target_val_spec_case", String(255), nullable=True),
    Column("pdbx_overall_ESU_R", Float, nullable=True),
    Column("pdbx_overall_ESU_R_Free", Float, nullable=True),
    Column("pdbx_solvent_vdw_probe_radii", Float, nullable=True),
    Column("pdbx_solvent_ion_probe_radii", Float, nullable=True),
    Column("pdbx_solvent_shrinkage_radii", Float, nullable=True),
    Column("pdbx_real_space_R", Float, nullable=True),
    Column("pdbx_density_correlation", Float, nullable=True),
    Column("pdbx_pd_number_of_powder_patterns", Integer, nullable=True),
    Column("pdbx_pd_number_of_points", Integer, nullable=True),
    Column("pdbx_pd_meas_number_of_points", Integer, nullable=True),
    Column("pdbx_pd_proc_ls_prof_R_factor", Float, nullable=True),
    Column("pdbx_pd_proc_ls_prof_wR_factor", Float, nullable=True),
    Column("pdbx_pd_Marquardt_correlation_coeff", Float, nullable=True),
    Column("pdbx_pd_Fsqrd_R_factor", Float, nullable=True),
    Column("pdbx_pd_ls_matrix_band_width", Integer, nullable=True),
    Column("pdbx_overall_phase_error", Float, nullable=True),
    Column("pdbx_overall_SU_R_free_Cruickshank_DPI", Float, nullable=True),
    Column("pdbx_overall_SU_R_free_Blow_DPI", Float, nullable=True),
    Column("pdbx_overall_SU_R_Blow_DPI", Float, nullable=True),
    Column("pdbx_TLS_residual_ADP_flag", String(128), nullable=True),
    Column("pdbx_diffrn_id", String(20), nullable=True),
    Column("overall_SU_B", Float, nullable=True),
    Column("overall_SU_ML", Float, nullable=True),
    Column("overall_SU_R_Cruickshank_DPI", Float, nullable=True),
    Column("overall_SU_R_free", Float, nullable=True),
    Column("overall_FOM_free_R_set", Float, nullable=True),
    Column("overall_FOM_work_R_set", Float, nullable=True),
    Column("pdbx_average_fsc_overall", Float, nullable=True),
    Column("pdbx_average_fsc_work", Float, nullable=True),
    Column("pdbx_average_fsc_free", Float, nullable=True),
    Column("pdbx_overall_ESU_B", Float, nullable=True),
    Column("pdbx_overall_ESU_ML", Float, nullable=True)
)


refine_analyze = Table("refine_analyze",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("Luzzati_coordinate_error_free", Float, nullable=True),
    Column("Luzzati_coordinate_error_obs", Float, nullable=True),
    Column("Luzzati_d_res_low_free", Float, nullable=True),
    Column("Luzzati_d_res_low_obs", Float, nullable=True),
    Column("Luzzati_sigma_a_free", Float, nullable=True),
    Column("Luzzati_sigma_a_free_details", String(255), nullable=True),
    Column("Luzzati_sigma_a_obs", Float, nullable=True),
    Column("Luzzati_sigma_a_obs_details", String(255), nullable=True),
    Column("number_disordered_residues", Float, nullable=True),
    Column("occupancy_sum_hydrogen", Float, nullable=True),
    Column("occupancy_sum_non_hydrogen", Float, nullable=True),
    Column("RG_d_res_high", Float, nullable=True),
    Column("RG_d_res_low", Float, nullable=True),
    Column("RG_free", Float, nullable=True),
    Column("RG_work", Float, nullable=True),
    Column("RG_free_work_ratio", Float, nullable=True),
    Column("pdbx_Luzzati_d_res_high_obs", Float, nullable=True)
)


refine_B_iso = Table("refine_B_iso",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("class", String(255), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("treatment", String(10), nullable=True),
    Column("value", Float, nullable=True),
    Column("pdbx_residue_name", String(20), nullable=True),
    Column("pdbx_strand", String(20), nullable=True),
    Column("pdbx_residue_num", String(20), nullable=True)
)


refine_funct_minimized = Table("refine_funct_minimized",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("number_terms", Integer, nullable=True),
    Column("residual", Float, nullable=True),
    Column("type", String(128), primary_key=True),
    Column("weight", Float, nullable=True)
)


refine_hist = Table("refine_hist",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("cycle_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("d_res_high", Float),
    Column("d_res_low", Float),
    Column("number_atoms_solvent", Integer, nullable=True),
    Column("number_atoms_total", Integer, nullable=True),
    Column("number_reflns_all", Integer, nullable=True),
    Column("number_reflns_obs", Integer, nullable=True),
    Column("number_reflns_R_free", Integer, nullable=True),
    Column("number_reflns_R_work", Integer, nullable=True),
    Column("R_factor_all", Float, nullable=True),
    Column("R_factor_obs", Float, nullable=True),
    Column("R_factor_R_free", Float, nullable=True),
    Column("R_factor_R_work", Float, nullable=True),
    Column("pdbx_number_residues_total", Integer, nullable=True),
    Column("pdbx_B_iso_mean_ligand", Float, nullable=True),
    Column("pdbx_B_iso_mean_solvent", Float, nullable=True),
    Column("pdbx_number_atoms_protein", Integer, nullable=True),
    Column("pdbx_number_atoms_nucleic_acid", Integer, nullable=True),
    Column("pdbx_number_atoms_ligand", Integer, nullable=True),
    Column("pdbx_number_atoms_lipid", Integer, nullable=True),
    Column("pdbx_number_atoms_carb", Integer, nullable=True),
    Column("pdbx_pseudo_atom_details", String(255), nullable=True),
    Column("pdbx_number_atoms_solvent", Integer, nullable=True),
    Column("pdbx_number_atoms_total", Integer, nullable=True)
)


refine_ls_restr = Table("refine_ls_restr",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("criterion", String(255), nullable=True),
    Column("dev_ideal", Float, nullable=True),
    Column("dev_ideal_target", Float, nullable=True),
    Column("number", Integer, nullable=True),
    Column("rejects", Integer, nullable=True),
    Column("weight", Float, nullable=True),
    Column("pdbx_restraint_function", String(255), nullable=True)
)


refine_ls_restr_ncs = Table("refine_ls_restr_ncs",
    metadata_obj,
    Column("pdbx_refine_id", String(128)),
    Column("dom_id", String(20)),
    Column("ncs_model_details", String(255), nullable=True),
    Column("rms_dev_B_iso", Float, nullable=True),
    Column("rms_dev_position", Float, nullable=True),
    Column("weight_B_iso", Float, nullable=True),
    Column("weight_position", Float, nullable=True),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("pdbx_type", String(255)),
    Column("pdbx_asym_id", String(20), nullable=True),
    Column("pdbx_auth_asym_id", String(20)),
    Column("pdbx_number", Integer, nullable=True),
    Column("pdbx_rms", Float, nullable=True),
    Column("pdbx_weight", Float, nullable=True),
    Column("pdbx_ens_id", String(20))
)


refine_ls_restr_type = Table("refine_ls_restr_type",
    metadata_obj,
    Column("distance_cutoff_high", Float, nullable=True),
    Column("distance_cutoff_low", Float, nullable=True),
    Column("type", String(128), primary_key=True)
)


refine_ls_shell = Table("refine_ls_shell",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float, nullable=True),
    Column("number_reflns_all", Integer, nullable=True),
    Column("number_reflns_obs", Integer, nullable=True),
    Column("number_reflns_R_free", Integer, nullable=True),
    Column("number_reflns_R_work", Integer, nullable=True),
    Column("percent_reflns_obs", Float, nullable=True),
    Column("percent_reflns_R_free", Float, nullable=True),
    Column("R_factor_all", Float, nullable=True),
    Column("R_factor_obs", Float, nullable=True),
    Column("R_factor_R_free_error", Float, nullable=True),
    Column("R_factor_R_work", Float, nullable=True),
    Column("redundancy_reflns_all", Float, nullable=True),
    Column("redundancy_reflns_obs", Float, nullable=True),
    Column("wR_factor_all", Float, nullable=True),
    Column("wR_factor_obs", Float, nullable=True),
    Column("wR_factor_R_free", Float, nullable=True),
    Column("wR_factor_R_work", Float, nullable=True),
    Column("pdbx_R_complete", Float, nullable=True),
    Column("pdbx_total_number_of_bins_used", Integer, nullable=True),
    Column("pdbx_phase_error", Float, nullable=True),
    Column("pdbx_fsc_work", Float, nullable=True),
    Column("pdbx_fsc_free", Float, nullable=True),
    Column("R_factor_R_free", Float, nullable=True)
)


refine_occupancy = Table("refine_occupancy",
    metadata_obj,
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("class", String(255), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("treatment", String(10), nullable=True),
    Column("value", Float, nullable=True)
)


refln = Table("refln",
    metadata_obj,
    Column("A_calc", Float, nullable=True),
    Column("A_calc_au", Float, nullable=True),
    Column("A_meas", Float, nullable=True),
    Column("A_meas_au", Float, nullable=True),
    Column("B_calc", Float, nullable=True),
    Column("B_calc_au", Float, nullable=True),
    Column("B_meas", Float, nullable=True),
    Column("B_meas_au", Float, nullable=True),
    Column("crystal_id", String(20), nullable=True),
    Column("F_calc", Float, nullable=True),
    Column("F_calc_au", Float, nullable=True),
    Column("F_meas", Float, nullable=True),
    Column("F_meas_au", Float, nullable=True),
    Column("F_meas_sigma", Float, nullable=True),
    Column("F_meas_sigma_au", Float, nullable=True),
    Column("F_squared_calc", Float, nullable=True),
    Column("F_squared_meas", Float, nullable=True),
    Column("F_squared_sigma", Float, nullable=True),
    Column("fom", Float, nullable=True),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("intensity_calc", Float, nullable=True),
    Column("intensity_meas", Float, nullable=True),
    Column("intensity_sigma", Float, nullable=True),
    Column("status", String(10), nullable=True),
    Column("phase_calc", Float, nullable=True),
    Column("phase_meas", Float, nullable=True),
    Column("refinement_status", String(10), nullable=True, default="incl"),
    Column("scale_group_code", String(128), nullable=True),
    Column("sint_over_lambda", Float, nullable=True),
    Column("symmetry_epsilon", Integer, nullable=True),
    Column("symmetry_multiplicity", Integer, nullable=True),
    Column("wavelength", Float, nullable=True),
    Column("wavelength_id", String(20), nullable=True),
    Column("class_code", String(20), nullable=True),
    Column("d_spacing", Float, nullable=True),
    Column("include_status", String(20), nullable=True),
    Column("mean_path_length_tbar", Float, nullable=True),
    Column("pdbx_F_calc_part_solvent", Float, nullable=True),
    Column("pdbx_phase_calc_part_solvent", Float, nullable=True),
    Column("pdbx_F_calc_with_solvent", Float, nullable=True),
    Column("pdbx_phase_calc_with_solvent", Float, nullable=True),
    Column("pdbx_anom_difference", Float, nullable=True),
    Column("pdbx_anom_difference_sigma", Float, nullable=True),
    Column("pdbx_I_plus", Float, nullable=True),
    Column("pdbx_I_minus", Float, nullable=True),
    Column("pdbx_F_plus", Float, nullable=True),
    Column("pdbx_F_minus", Float, nullable=True),
    Column("pdbx_I_plus_sigma", Float, nullable=True),
    Column("pdbx_I_minus_sigma", Float, nullable=True),
    Column("pdbx_F_minus_sigma", Float, nullable=True),
    Column("pdbx_F_plus_sigma", Float, nullable=True),
    Column("pdbx_HL_A_iso", Float, nullable=True),
    Column("pdbx_HL_B_iso", Float, nullable=True),
    Column("pdbx_HL_C_iso", Float, nullable=True),
    Column("pdbx_HL_D_iso", Float, nullable=True),
    Column("pdbx_fiber_layer", Integer, nullable=True),
    Column("pdbx_fiber_coordinate", Float, nullable=True),
    Column("pdbx_fiber_F_meas_au", Float, nullable=True),
    Column("pdbx_FWT", Float, nullable=True),
    Column("pdbx_PHWT", Float, nullable=True),
    Column("pdbx_DELFWT", Float, nullable=True),
    Column("pdbx_DELPHWT", Float, nullable=True),
    Column("pdbx_diffrn_id", String(20), nullable=True),
    Column("pdbx_r_free_flag", Integer, nullable=True),
    Column("pdbx_anomalous_diff", Float, nullable=True),
    Column("pdbx_anomalous_diff_sigma", Float, nullable=True),
    Column("pdbx_phase_cycle", Float, nullable=True),
    Column("pdbx_cos_phase_calc", Float, nullable=True),
    Column("pdbx_sin_phase_calc", Float, nullable=True),
    Column("pdbx_signal", Float, nullable=True),
    Column("pdbx_signal_status", String(20), nullable=True)
)


refln_sys_abs = Table("refln_sys_abs",
    metadata_obj,
    Column("I", Float, nullable=True),
    Column("I_over_sigmaI", Float, nullable=True),
    Column("index_h", Integer, primary_key=True),
    Column("index_k", Integer, primary_key=True),
    Column("index_l", Integer, primary_key=True),
    Column("sigmaI", Float, nullable=True)
)


reflns = Table("reflns",
    metadata_obj,
    Column("B_iso_Wilson_estimate", Float, nullable=True),
    Column("entry_id", String(20)),
    Column("data_reduction_details", String(255), nullable=True),
    Column("data_reduction_method", String(255), nullable=True),
    Column("d_resolution_high", Float, nullable=True),
    Column("d_resolution_low", Float, nullable=True),
    Column("details", String(255), nullable=True),
    Column("limit_h_max", Integer, nullable=True),
    Column("limit_h_min", Integer, nullable=True),
    Column("limit_k_max", Integer, nullable=True),
    Column("limit_k_min", Integer, nullable=True),
    Column("limit_l_max", Integer, nullable=True),
    Column("limit_l_min", Integer, nullable=True),
    Column("number_all", Integer, nullable=True),
    Column("number_obs", Integer, nullable=True),
    Column("observed_criterion", String(255), nullable=True),
    Column("observed_criterion_F_max", Float, nullable=True),
    Column("observed_criterion_F_min", Float, nullable=True),
    Column("observed_criterion_I_max", Float, nullable=True),
    Column("observed_criterion_I_min", Float, nullable=True),
    Column("observed_criterion_sigma_F", Float, nullable=True),
    Column("observed_criterion_sigma_I", Float, nullable=True),
    Column("percent_possible_obs", Float, nullable=True),
    Column("R_free_details", String(255), nullable=True),
    Column("Rmerge_F_all", Float, nullable=True),
    Column("Rmerge_F_obs", Float, nullable=True),
    Column("Friedel_coverage", Float, nullable=True),
    Column("number_gt", Integer, nullable=True),
    Column("threshold_expression", String(255), nullable=True),
    Column("pdbx_redundancy", Float, nullable=True),
    Column("pdbx_netI_over_av_sigmaI", Float, nullable=True),
    Column("pdbx_netI_over_sigmaI", Float, nullable=True),
    Column("pdbx_res_netI_over_av_sigmaI_2", Float, nullable=True),
    Column("pdbx_res_netI_over_sigmaI_2", Float, nullable=True),
    Column("pdbx_chi_squared", Float, nullable=True),
    Column("pdbx_scaling_rejects", Integer, nullable=True),
    Column("pdbx_d_res_high_opt", Float, nullable=True),
    Column("pdbx_d_res_low_opt", Float, nullable=True),
    Column("pdbx_d_res_opt_method", String(255), nullable=True),
    Column("phase_calculation_details", String(255), nullable=True),
    Column("pdbx_Rrim_I_all", Float, nullable=True),
    Column("pdbx_Rpim_I_all", Float, nullable=True),
    Column("pdbx_d_opt", Float, nullable=True),
    Column("pdbx_number_measured_all", Integer, nullable=True),
    Column("pdbx_diffrn_id", String(20)),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("pdbx_CC_half", Float, nullable=True),
    Column("pdbx_CC_star", Float, nullable=True),
    Column("pdbx_R_split", Float, nullable=True),
    Column("pdbx_redundancy_reflns_obs", Float, nullable=True),
    Column("pdbx_number_anomalous", Integer, nullable=True),
    Column("pdbx_Rrim_I_all_anomalous", Float, nullable=True),
    Column("pdbx_Rpim_I_all_anomalous", Float, nullable=True),
    Column("pdbx_Rmerge_I_anomalous", Float, nullable=True),
    Column("pdbx_Rmerge_I_obs", Float, nullable=True),
    Column("pdbx_Rmerge_I_all", Float, nullable=True),
    Column("pdbx_Rsym_value", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_1_ortho[1]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_1_ortho[2]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_1_ortho[3]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_2_ortho[1]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_2_ortho[2]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_2_ortho[3]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_3_ortho[1]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_3_ortho[2]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_axis_3_ortho[3]", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_1", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_2", Float, nullable=True),
    Column("pdbx_aniso_diffraction_limit_3", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_1_ortho[1]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_1_ortho[2]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_1_ortho[3]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_2_ortho[1]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_2_ortho[2]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_2_ortho[3]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_3_ortho[1]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_3_ortho[2]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvector_3_ortho[3]", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvalue_1", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvalue_2", Float, nullable=True),
    Column("pdbx_aniso_B_tensor_eigenvalue_3", Float, nullable=True),
    Column("pdbx_orthogonalization_convention", String(20), nullable=True),
    Column("pdbx_percent_possible_ellipsoidal", Float, nullable=True),
    Column("pdbx_percent_possible_spherical", Float, nullable=True),
    Column("pdbx_percent_possible_ellipsoidal_anomalous", Float, nullable=True),
    Column("pdbx_percent_possible_spherical_anomalous", Float, nullable=True),
    Column("pdbx_redundancy_anomalous", Float, nullable=True),
    Column("pdbx_CC_half_anomalous", Float, nullable=True),
    Column("pdbx_absDiff_over_sigma_anomalous", Float, nullable=True),
    Column("pdbx_percent_possible_anomalous", Float, nullable=True),
    Column("pdbx_observed_signal_threshold", Float, nullable=True),
    Column("pdbx_signal_type", String(128), nullable=True),
    Column("pdbx_signal_details", String(255), nullable=True),
    Column("pdbx_signal_software_id", String(255), nullable=True),
    Column("pdbx_CC_split_method", String(10), nullable=True)
)


reflns_scale = Table("reflns_scale",
    metadata_obj,
    Column("meas_F", Float, nullable=True),
    Column("meas_F_squared", Float, nullable=True),
    Column("meas_intensity", Float, nullable=True)
)


reflns_shell = Table("reflns_shell",
    metadata_obj,
    Column("d_res_high", Float),
    Column("d_res_low", Float, nullable=True),
    Column("meanI_over_sigI_all", Float, nullable=True),
    Column("meanI_over_sigI_obs", Float, nullable=True),
    Column("number_measured_all", Integer, nullable=True),
    Column("number_measured_obs", Integer, nullable=True),
    Column("number_possible", Integer, nullable=True),
    Column("number_unique_all", Integer, nullable=True),
    Column("number_unique_obs", Integer, nullable=True),
    Column("percent_possible_obs", Float, nullable=True),
    Column("Rmerge_F_all", Float, nullable=True),
    Column("Rmerge_F_obs", Float, nullable=True),
    Column("meanI_over_sigI_gt", Float, nullable=True),
    Column("meanI_over_uI_all", Float, nullable=True),
    Column("meanI_over_uI_gt", Float, nullable=True),
    Column("number_measured_gt", Integer, nullable=True),
    Column("number_unique_gt", Integer, nullable=True),
    Column("percent_possible_gt", Float, nullable=True),
    Column("Rmerge_F_gt", Float, nullable=True),
    Column("Rmerge_I_gt", Float, nullable=True),
    Column("pdbx_redundancy", Float, nullable=True),
    Column("pdbx_chi_squared", Float, nullable=True),
    Column("pdbx_netI_over_sigmaI_all", Float, nullable=True),
    Column("pdbx_netI_over_sigmaI_obs", Float, nullable=True),
    Column("pdbx_Rrim_I_all", Float, nullable=True),
    Column("pdbx_Rpim_I_all", Float, nullable=True),
    Column("pdbx_rejects", Integer, nullable=True),
    Column("pdbx_ordinal", Integer, primary_key=True),
    Column("pdbx_diffrn_id", String(20), nullable=True),
    Column("pdbx_CC_half", Float, nullable=True),
    Column("pdbx_CC_star", Float, nullable=True),
    Column("pdbx_R_split", Float, nullable=True),
    Column("pdbx_redundancy_reflns_obs", Float, nullable=True),
    Column("pdbx_number_anomalous", Integer, nullable=True),
    Column("pdbx_Rrim_I_all_anomalous", Float, nullable=True),
    Column("pdbx_Rpim_I_all_anomalous", Float, nullable=True),
    Column("pdbx_Rmerge_I_all_anomalous", Float, nullable=True),
    Column("percent_possible_all", Float, nullable=True),
    Column("Rmerge_I_all", Float, nullable=True),
    Column("Rmerge_I_obs", Float, nullable=True),
    Column("pdbx_Rsym_value", Float, nullable=True),
    Column("pdbx_percent_possible_ellipsoidal", Float, nullable=True),
    Column("pdbx_percent_possible_spherical", Float, nullable=True),
    Column("pdbx_percent_possible_ellipsoidal_anomalous", Float, nullable=True),
    Column("pdbx_percent_possible_spherical_anomalous", Float, nullable=True),
    Column("pdbx_redundancy_anomalous", Float, nullable=True),
    Column("pdbx_CC_half_anomalous", Float, nullable=True),
    Column("pdbx_absDiff_over_sigma_anomalous", Float, nullable=True),
    Column("pdbx_percent_possible_anomalous", Float, nullable=True)
)


software = Table("software",
    metadata_obj,
    Column("citation_id", String(20), nullable=True),
    Column("classification", String(50)),
    Column("compiler_name", String(128), nullable=True),
    Column("compiler_version", String(128), nullable=True),
    Column("contact_author", String(128), nullable=True),
    Column("contact_author_email", String(128), nullable=True),
    Column("date", String(128), nullable=True),
    Column("description", String(128), nullable=True),
    Column("dependencies", String(128), nullable=True),
    Column("hardware", String(128), nullable=True),
    Column("language", String(50), nullable=True),
    Column("location", String(128), nullable=True),
    Column("mods", String(128), nullable=True),
    Column("name", String(255)),
    Column("os", String(255), nullable=True),
    Column("os_version", String(255), nullable=True),
    Column("type", String(50), nullable=True),
    Column("version", String(128), nullable=True),
    Column("pdbx_ordinal", Integer, primary_key=True)
)


struct = Table("struct",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("title", String(255), nullable=True),
    Column("pdbx_center_of_mass_x", Float, nullable=True),
    Column("pdbx_center_of_mass_y", Float, nullable=True),
    Column("pdbx_center_of_mass_z", Float, nullable=True),
    Column("pdbx_structure_determination_methodology", String(128), nullable=True),
    Column("pdbx_descriptor", String(255), nullable=True),
    Column("pdbx_model_details", String(255), nullable=True),
    Column("pdbx_formula_weight", Float, nullable=True),
    Column("pdbx_formula_weight_method", String(128), nullable=True),
    Column("pdbx_model_type_details", String(128), nullable=True),
    Column("pdbx_CASP_flag", String(2), nullable=True),
    Column("pdbx_details", String(255), nullable=True),
    Column("pdbx_title_text", String(255), nullable=True)
)


struct_asym = Table("struct_asym",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("entity_id", String(20)),
    Column("pdbx_modified", String(255), nullable=True),
    Column("pdbx_blank_PDB_chainid_flag", String(20), nullable=True),
    Column("pdbx_PDB_id", String(20), nullable=True),
    Column("pdbx_alt_id", String(20), nullable=True),
    Column("pdbx_type", String(10), nullable=True),
    Column("pdbx_order", Integer, nullable=True),
    Column("pdbx_fraction_per_asym_unit", String(255), nullable=True),
    Column("pdbx_missing_num_begin_of_chain_not_in_seqres", Integer, nullable=True),
    Column("pdbx_missing_num_end_of_chain_not_in_seqres", Integer, nullable=True),
    Column("pdbx_missing_num_begin_of_chain_in_seqres", Integer, nullable=True)
)


struct_biol = Table("struct_biol",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("pdbx_parent_biol_id", String(128), nullable=True),
    Column("pdbx_formula_weight", Float, nullable=True),
    Column("pdbx_formula_weight_method", String(128), nullable=True),
    Column("pdbx_aggregation_state", String(128), nullable=True),
    Column("pdbx_assembly_method", String(255), nullable=True)
)


struct_biol_gen = Table("struct_biol_gen",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("biol_id", String(128), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("symmetry", String(10), primary_key=True),
    Column("pdbx_full_symmetry_operation", String(20), nullable=True),
    Column("pdbx_PDB_order", Integer, nullable=True),
    Column("pdbx_new_asym_id", String(20)),
    Column("pdbx_new_pdb_asym_id", String(20)),
    Column("pdbx_color_red", Float, nullable=True),
    Column("pdbx_color_green", Float, nullable=True),
    Column("pdbx_color_blue", Float, nullable=True),
    Column("pdbx_after_begin_residue_no", String(20), nullable=True),
    Column("pdbx_after_end_residue_no", String(20), nullable=True),
    Column("pdbx_before_begin_residue_no", String(20), nullable=True),
    Column("pdbx_before_end_residue_no", String(20), nullable=True)
)


struct_biol_keywords = Table("struct_biol_keywords",
    metadata_obj,
    Column("biol_id", String(128), primary_key=True),
    Column("text", String(255), primary_key=True)
)


struct_biol_view = Table("struct_biol_view",
    metadata_obj,
    Column("biol_id", String(128), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("id", String(128), primary_key=True),
    Column("rot_matrix[1][1]", Float, nullable=True),
    Column("rot_matrix[1][2]", Float, nullable=True),
    Column("rot_matrix[1][3]", Float, nullable=True),
    Column("rot_matrix[2][1]", Float, nullable=True),
    Column("rot_matrix[2][2]", Float, nullable=True),
    Column("rot_matrix[2][3]", Float, nullable=True),
    Column("rot_matrix[3][1]", Float, nullable=True),
    Column("rot_matrix[3][2]", Float, nullable=True),
    Column("rot_matrix[3][3]", Float, nullable=True),
    Column("pdbx_vector[1]", Float, nullable=True, default=0.0),
    Column("pdbx_vector[2]", Float, nullable=True, default=0.0),
    Column("pdbx_vector[3]", Float, nullable=True, default=0.0)
)


struct_conf = Table("struct_conf",
    metadata_obj,
    Column("beg_label_asym_id", String(20)),
    Column("beg_label_comp_id", String(10)),
    Column("beg_label_seq_id", Integer),
    Column("beg_auth_asym_id", String(20), nullable=True),
    Column("beg_auth_comp_id", String(20), nullable=True),
    Column("beg_auth_seq_id", String(20), nullable=True),
    Column("conf_type_id", String(10)),
    Column("details", String(255), nullable=True),
    Column("end_label_asym_id", String(20)),
    Column("end_label_comp_id", String(10)),
    Column("end_label_seq_id", Integer),
    Column("end_auth_asym_id", String(20), nullable=True),
    Column("end_auth_comp_id", String(20), nullable=True),
    Column("end_auth_seq_id", String(20), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("pdbx_beg_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_end_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_PDB_helix_class", String(128), nullable=True),
    Column("pdbx_PDB_helix_length", Integer, nullable=True),
    Column("pdbx_PDB_helix_id", String(20), nullable=True)
)


struct_conf_type = Table("struct_conf_type",
    metadata_obj,
    Column("criteria", String(255), nullable=True),
    Column("reference", String(255), nullable=True)
)


struct_conn = Table("struct_conn",
    metadata_obj,
    Column("conn_type_id", String(10)),
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("ptnr1_label_alt_id", String(20), nullable=True),
    Column("ptnr1_label_asym_id", String(20)),
    Column("ptnr1_label_atom_id", String(6), nullable=True),
    Column("ptnr1_label_comp_id", String(10)),
    Column("ptnr1_label_seq_id", Integer),
    Column("ptnr1_auth_asym_id", String(20), nullable=True),
    Column("ptnr1_auth_atom_id", String(6), nullable=True),
    Column("ptnr1_auth_comp_id", String(20), nullable=True),
    Column("ptnr1_auth_seq_id", String(20), nullable=True),
    Column("ptnr1_role", String(50), nullable=True),
    Column("ptnr1_symmetry", String(10), nullable=True),
    Column("ptnr2_label_alt_id", String(20), nullable=True),
    Column("ptnr2_label_asym_id", String(20)),
    Column("ptnr2_label_atom_id", String(6), nullable=True),
    Column("ptnr2_label_comp_id", String(10)),
    Column("ptnr2_label_seq_id", Integer),
    Column("ptnr2_auth_asym_id", String(20), nullable=True),
    Column("ptnr2_auth_atom_id", String(6), nullable=True),
    Column("ptnr2_auth_comp_id", String(20), nullable=True),
    Column("ptnr2_auth_seq_id", String(20), nullable=True),
    Column("ptnr2_role", String(50), nullable=True),
    Column("ptnr2_symmetry", String(10), nullable=True),
    Column("pdbx_ptnr1_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_ptnr1_auth_alt_id", String(20), nullable=True),
    Column("pdbx_ptnr1_label_alt_id", String(20), nullable=True),
    Column("pdbx_ptnr1_standard_comp_id", String(20), nullable=True),
    Column("pdbx_ptnr2_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_ptnr2_auth_alt_id", String(20), nullable=True),
    Column("pdbx_ptnr2_label_alt_id", String(20), nullable=True),
    Column("pdbx_ptnr3_auth_alt_id", String(20), nullable=True),
    Column("pdbx_ptnr3_auth_asym_id", String(20), nullable=True),
    Column("pdbx_ptnr3_auth_atom_id", String(6), nullable=True),
    Column("pdbx_ptnr3_auth_comp_id", String(20), nullable=True),
    Column("pdbx_ptnr3_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_ptnr3_auth_seq_id", String(20), nullable=True),
    Column("pdbx_ptnr3_label_alt_id", String(20), nullable=True),
    Column("pdbx_ptnr3_label_asym_id", String(20), nullable=True),
    Column("pdbx_ptnr3_label_atom_id", String(6), nullable=True),
    Column("pdbx_ptnr3_label_comp_id", String(10), nullable=True),
    Column("pdbx_ptnr3_label_seq_id", Integer, nullable=True),
    Column("pdbx_PDB_id", String(20), nullable=True),
    Column("pdbx_dist_value", Float, nullable=True),
    Column("pdbx_value_order", String(10), nullable=True, default="sing"),
    Column("pdbx_leaving_atom_flag", String(20), nullable=True),
    Column("pdbx_ptnr1_mod_name", String(128), nullable=True),
    Column("pdbx_ptnr1_sugar_name", String(128), nullable=True),
    Column("pdbx_ptnr1_replaced_atom", String(20), nullable=True),
    Column("pdbx_ptnr3_auth_ins_code", String(20), nullable=True),
    Column("pdbx_ptnr1_atom_stereo_config", String(10), nullable=True, default="N"),
    Column("pdbx_ptnr1_leaving_atom_id", String(6), nullable=True),
    Column("pdbx_ptnr2_atom_stereo_config", String(10), nullable=True, default="N"),
    Column("pdbx_ptnr2_leaving_atom_id", String(6), nullable=True),
    Column("pdbx_role", String(50), nullable=True)
)


struct_conn_type = Table("struct_conn_type",
    metadata_obj,
    Column("criteria", String(255), nullable=True),
    Column("reference", String(255), nullable=True)
)


struct_keywords = Table("struct_keywords",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("text", String(255), nullable=True),
    Column("pdbx_keywords", String(128), nullable=True),
    Column("pdbx_details", String(255), nullable=True)
)


struct_mon_details = Table("struct_mon_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("prot_cis", Float, nullable=True),
    Column("RSCC", String(255), nullable=True),
    Column("RSR", String(255), nullable=True)
)


struct_mon_nucl = Table("struct_mon_nucl",
    metadata_obj,
    Column("alpha", Float, nullable=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("beta", Float, nullable=True),
    Column("chi1", Float, nullable=True),
    Column("chi2", Float, nullable=True),
    Column("delta", Float, nullable=True),
    Column("details", Float, nullable=True),
    Column("epsilon", Float, nullable=True),
    Column("gamma", Float, nullable=True),
    Column("label_alt_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_comp_id", String(10), primary_key=True),
    Column("label_seq_id", Integer, primary_key=True),
    Column("mean_B_all", Float, nullable=True),
    Column("mean_B_base", Float, nullable=True),
    Column("mean_B_phos", Float, nullable=True),
    Column("mean_B_sugar", Float, nullable=True),
    Column("nu0", Float, nullable=True),
    Column("nu1", Float, nullable=True),
    Column("nu2", Float, nullable=True),
    Column("nu3", Float, nullable=True),
    Column("nu4", Float, nullable=True),
    Column("P", Float, nullable=True),
    Column("RSCC_all", Float, nullable=True),
    Column("RSCC_base", Float, nullable=True),
    Column("RSCC_phos", Float, nullable=True),
    Column("RSCC_sugar", Float, nullable=True),
    Column("RSR_all", Float, nullable=True),
    Column("RSR_base", Float, nullable=True),
    Column("RSR_phos", Float, nullable=True),
    Column("RSR_sugar", Float, nullable=True),
    Column("tau0", Float, nullable=True),
    Column("tau1", Float, nullable=True),
    Column("tau2", Float, nullable=True),
    Column("tau3", Float, nullable=True),
    Column("tau4", Float, nullable=True),
    Column("taum", Float, nullable=True),
    Column("zeta", Float, nullable=True)
)


struct_mon_prot = Table("struct_mon_prot",
    metadata_obj,
    Column("chi1", Float, nullable=True),
    Column("chi2", Float, nullable=True),
    Column("chi3", Float, nullable=True),
    Column("chi4", Float, nullable=True),
    Column("chi5", Float, nullable=True),
    Column("details", Float, nullable=True),
    Column("label_alt_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_comp_id", String(10), primary_key=True),
    Column("label_seq_id", Integer, primary_key=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("RSCC_all", Float, nullable=True),
    Column("RSCC_main", Float, nullable=True),
    Column("RSCC_side", Float, nullable=True),
    Column("RSR_all", Float, nullable=True),
    Column("RSR_main", Float, nullable=True),
    Column("RSR_side", Float, nullable=True),
    Column("mean_B_all", Float, nullable=True),
    Column("mean_B_main", Float, nullable=True),
    Column("mean_B_side", Float, nullable=True),
    Column("omega", Float, nullable=True),
    Column("phi", Float, nullable=True),
    Column("psi", Float, nullable=True)
)


struct_mon_prot_cis = Table("struct_mon_prot_cis",
    metadata_obj,
    Column("label_alt_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("pdbx_auth_asym_id_2", String(20), nullable=True),
    Column("pdbx_auth_comp_id_2", String(20), nullable=True),
    Column("pdbx_auth_seq_id_2", String(20), nullable=True),
    Column("pdbx_label_asym_id_2", String(20), nullable=True),
    Column("pdbx_label_comp_id_2", String(10), nullable=True),
    Column("pdbx_label_seq_id_2", Integer, nullable=True),
    Column("pdbx_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_PDB_ins_code_2", String(20), nullable=True),
    Column("pdbx_PDB_model_num", Integer),
    Column("pdbx_omega_angle", String(20), nullable=True),
    Column("pdbx_id", String(20), primary_key=True),
    Column("pdbx_auth_ins_code", String(20), nullable=True),
    Column("pdbx_auth_ins_code_2", String(20), nullable=True)
)


struct_ncs_dom = Table("struct_ncs_dom",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("pdbx_ens_id", String(20), primary_key=True)
)


struct_ncs_dom_lim = Table("struct_ncs_dom_lim",
    metadata_obj,
    Column("beg_label_alt_id", String(20), nullable=True),
    Column("beg_label_asym_id", String(20), nullable=True),
    Column("beg_label_comp_id", String(20), nullable=True),
    Column("beg_label_seq_id", Integer, nullable=True),
    Column("beg_auth_asym_id", String(20), nullable=True),
    Column("beg_auth_comp_id", String(20), nullable=True),
    Column("beg_auth_seq_id", String(20), nullable=True),
    Column("dom_id", String(20), primary_key=True),
    Column("end_label_alt_id", String(20), nullable=True),
    Column("end_label_asym_id", String(20), nullable=True),
    Column("end_label_comp_id", String(20), nullable=True),
    Column("end_label_seq_id", Integer, nullable=True),
    Column("end_auth_asym_id", String(20), nullable=True),
    Column("end_auth_comp_id", String(20), nullable=True),
    Column("end_auth_seq_id", String(20), nullable=True),
    Column("selection_details", String(255), nullable=True),
    Column("pdbx_component_id", Integer, primary_key=True),
    Column("pdbx_refine_code", Float, nullable=True),
    Column("pdbx_ens_id", String(20), primary_key=True)
)


struct_ncs_ens = Table("struct_ncs_ens",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("point_group", String(128), nullable=True)
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
    Column("code", String(20)),
    Column("details", String(255), nullable=True),
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


struct_ref = Table("struct_ref",
    metadata_obj,
    Column("biol_id", String(128), nullable=True),
    Column("db_code", String(128)),
    Column("db_name", String(128)),
    Column("details", String(255), nullable=True),
    Column("entity_id", String(20)),
    Column("seq_align", String(10), nullable=True),
    Column("seq_dif", String(10), nullable=True),
    Column("pdbx_db_accession", String(20), nullable=True),
    Column("pdbx_db_isoform", String(20), nullable=True),
    Column("pdbx_seq_one_letter_code", String(255), nullable=True),
    Column("pdbx_align_begin", String(20), nullable=True),
    Column("pdbx_align_end", String(20), nullable=True)
)


struct_ref_seq = Table("struct_ref_seq",
    metadata_obj,
    Column("db_align_beg", Integer),
    Column("db_align_end", Integer),
    Column("details", String(255), nullable=True),
    Column("ref_id", String(20)),
    Column("seq_align_beg", Integer),
    Column("seq_align_end", Integer),
    Column("pdbx_strand_id", String(20), nullable=True),
    Column("pdbx_db_accession", String(20), nullable=True),
    Column("pdbx_db_align_beg_ins_code", String(20), nullable=True),
    Column("pdbx_db_align_end_ins_code", String(20), nullable=True),
    Column("pdbx_PDB_id_code", String(20), nullable=True),
    Column("pdbx_auth_seq_align_beg", String(20), nullable=True),
    Column("pdbx_auth_seq_align_end", String(20), nullable=True),
    Column("pdbx_seq_align_beg_ins_code", String(20), nullable=True),
    Column("pdbx_seq_align_end_ins_code", String(20), nullable=True)
)


struct_ref_seq_dif = Table("struct_ref_seq_dif",
    metadata_obj,
    Column("align_id", String(20)),
    Column("db_mon_id", String(10), nullable=True),
    Column("details", String(255), nullable=True),
    Column("mon_id", String(10), nullable=True),
    Column("seq_num", Integer, nullable=True),
    Column("pdbx_pdb_id_code", String(20), nullable=True),
    Column("pdbx_pdb_strand_id", String(20), nullable=True),
    Column("pdbx_pdb_ins_code", String(20), nullable=True),
    Column("pdbx_auth_seq_num", String(20), nullable=True),
    Column("pdbx_seq_db_name", String(20), nullable=True),
    Column("pdbx_seq_db_accession_code", String(20), nullable=True),
    Column("pdbx_seq_db_seq_num", String(20), nullable=True),
    Column("pdbx_ordinal", Integer, primary_key=True)
)


struct_sheet = Table("struct_sheet",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("number_strands", Integer, nullable=True),
    Column("type", String(255), nullable=True)
)


struct_sheet_hbond = Table("struct_sheet_hbond",
    metadata_obj,
    Column("range_1_beg_label_atom_id", String(6)),
    Column("range_1_beg_label_seq_id", Integer),
    Column("range_1_end_label_atom_id", String(6)),
    Column("range_1_end_label_seq_id", Integer),
    Column("range_2_beg_label_atom_id", String(6)),
    Column("range_2_beg_label_seq_id", Integer),
    Column("range_2_end_label_atom_id", String(6)),
    Column("range_2_end_label_seq_id", Integer),
    Column("range_1_beg_auth_atom_id", String(6), nullable=True),
    Column("range_1_beg_auth_seq_id", String(20), nullable=True),
    Column("range_1_end_auth_atom_id", String(6), nullable=True),
    Column("range_1_end_auth_seq_id", String(20), nullable=True),
    Column("range_2_beg_auth_atom_id", String(6), nullable=True),
    Column("range_2_beg_auth_seq_id", String(20), nullable=True),
    Column("range_2_end_auth_atom_id", String(6), nullable=True),
    Column("range_2_end_auth_seq_id", String(20), nullable=True),
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sheet_id", String(20), primary_key=True),
    Column("pdbx_range_1_beg_auth_comp_id", String(20), nullable=True),
    Column("pdbx_range_1_beg_auth_asym_id", String(20), nullable=True),
    Column("pdbx_range_1_end_auth_comp_id", String(20), nullable=True),
    Column("pdbx_range_1_end_auth_asym_id", String(20), nullable=True),
    Column("pdbx_range_1_beg_label_comp_id", String(10), nullable=True),
    Column("pdbx_range_1_beg_label_asym_id", String(20), nullable=True),
    Column("pdbx_range_1_beg_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_range_1_end_label_comp_id", String(10), nullable=True),
    Column("pdbx_range_1_end_label_asym_id", String(20), nullable=True),
    Column("pdbx_range_1_end_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_range_2_beg_label_comp_id", String(10), nullable=True),
    Column("pdbx_range_2_beg_label_asym_id", String(20), nullable=True),
    Column("pdbx_range_2_beg_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_range_2_end_label_comp_id", String(10), nullable=True),
    Column("pdbx_range_2_end_label_asym_id", String(20), nullable=True),
    Column("pdbx_range_2_end_label_ins_code", String(20), nullable=True)
)


struct_sheet_order = Table("struct_sheet_order",
    metadata_obj,
    Column("offset", Integer, nullable=True),
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sense", String(10), nullable=True),
    Column("sheet_id", String(20), primary_key=True)
)


struct_sheet_range = Table("struct_sheet_range",
    metadata_obj,
    Column("beg_label_asym_id", String(20)),
    Column("beg_label_comp_id", String(10)),
    Column("beg_label_seq_id", Integer),
    Column("end_label_asym_id", String(20)),
    Column("end_label_comp_id", String(10)),
    Column("end_label_seq_id", Integer),
    Column("beg_auth_asym_id", String(20), nullable=True),
    Column("beg_auth_comp_id", String(20), nullable=True),
    Column("beg_auth_seq_id", String(20), nullable=True),
    Column("end_auth_asym_id", String(20), nullable=True),
    Column("end_auth_comp_id", String(20), nullable=True),
    Column("end_auth_seq_id", String(20), nullable=True),
    Column("sheet_id", String(20), primary_key=True),
    Column("symmetry", String(10), nullable=True),
    Column("pdbx_beg_PDB_ins_code", String(20), nullable=True),
    Column("pdbx_end_PDB_ins_code", String(20), nullable=True)
)


struct_sheet_topology = Table("struct_sheet_topology",
    metadata_obj,
    Column("offset", Integer, nullable=True),
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sense", String(10), nullable=True),
    Column("sheet_id", String(20), primary_key=True)
)


struct_site = Table("struct_site",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("pdbx_num_residues", Integer, nullable=True),
    Column("pdbx_evidence_code", String(255), nullable=True),
    Column("pdbx_auth_asym_id", String(20), nullable=True),
    Column("pdbx_auth_comp_id", String(20), nullable=True),
    Column("pdbx_auth_seq_id", String(20), nullable=True),
    Column("pdbx_auth_ins_code", String(20), nullable=True)
)


struct_site_gen = Table("struct_site_gen",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(128), primary_key=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_asym_id", String(20)),
    Column("label_atom_id", String(6)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_atom_id", String(6), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("site_id", String(128), primary_key=True),
    Column("symmetry", String(10), nullable=True),
    Column("pdbx_auth_ins_code", String(20), nullable=True),
    Column("pdbx_num_res", Integer, nullable=True)
)


struct_site_keywords = Table("struct_site_keywords",
    metadata_obj,
    Column("site_id", String(128), primary_key=True),
    Column("text", String(255), primary_key=True)
)


struct_site_view = Table("struct_site_view",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(128), primary_key=True),
    Column("rot_matrix[1][1]", Float, nullable=True),
    Column("rot_matrix[1][2]", Float, nullable=True),
    Column("rot_matrix[1][3]", Float, nullable=True),
    Column("rot_matrix[2][1]", Float, nullable=True),
    Column("rot_matrix[2][2]", Float, nullable=True),
    Column("rot_matrix[2][3]", Float, nullable=True),
    Column("rot_matrix[3][1]", Float, nullable=True),
    Column("rot_matrix[3][2]", Float, nullable=True),
    Column("rot_matrix[3][3]", Float, nullable=True),
    Column("site_id", String(128))
)


symmetry = Table("symmetry",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cell_setting", String(10), nullable=True),
    Column("Int_Tables_number", Integer, nullable=True),
    Column("space_group_name_Hall", String(128), nullable=True),
    Column("space_group_name_H-M", String(128), nullable=True),
    Column("pdbx_full_space_group_name_H-M", String(128), nullable=True)
)


symmetry_equiv = Table("symmetry_equiv",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("pos_as_xyz", String(128), nullable=True)
)


audit_link = Table("audit_link",
    metadata_obj,
    Column("block_code", String(20), primary_key=True),
    Column("block_description", String(255), primary_key=True)
)


diffrn_reflns_class = Table("diffrn_reflns_class",
    metadata_obj,
    Column("av_R_eq", Float, nullable=True),
    Column("av_sgI/I", Float, nullable=True),
    Column("av_uI/I", Float, nullable=True),
    Column("code", String(20), primary_key=True),
    Column("description", String(255), nullable=True),
    Column("d_res_high", Float, nullable=True),
    Column("d_res_low", Float, nullable=True),
    Column("number", Integer, nullable=True)
)


refine_ls_class = Table("refine_ls_class",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("d_res_high", Float, nullable=True),
    Column("d_res_low", Float, nullable=True),
    Column("R_factor_gt", Float, nullable=True),
    Column("R_factor_all", Float, nullable=True),
    Column("R_Fsqd_factor", Float, nullable=True),
    Column("R_I_factor", Float, nullable=True),
    Column("wR_factor_all", Float, nullable=True)
)


reflns_class = Table("reflns_class",
    metadata_obj,
    Column("code", String(20), primary_key=True),
    Column("description", String(255), nullable=True),
    Column("d_res_high", Float, nullable=True),
    Column("d_res_low", Float, nullable=True),
    Column("number_gt", Integer, nullable=True),
    Column("number_total", Integer, nullable=True),
    Column("R_factor_all", Float, nullable=True),
    Column("R_factor_gt", Float, nullable=True),
    Column("R_Fsqd_factor", Float, nullable=True),
    Column("R_I_factor", Float, nullable=True),
    Column("wR_factor_all", Float, nullable=True)
)


space_group = Table("space_group",
    metadata_obj,
    Column("crystal_system", String(20), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("IT_number", Integer, nullable=True),
    Column("name_Hall", String(128), nullable=True),
    Column("name_H-M_alt", String(128), nullable=True)
)


space_group_symop = Table("space_group_symop",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("operation_xyz", String(128), nullable=True),
    Column("sg_id", String(20), nullable=True)
)


valence_param = Table("valence_param",
    metadata_obj,
    Column("atom_1", String(20), primary_key=True),
    Column("atom_1_valence", Integer, primary_key=True),
    Column("atom_2", String(20), primary_key=True),
    Column("atom_2_valence", Integer, primary_key=True),
    Column("B", Float, nullable=True),
    Column("details", String(255), nullable=True),
    Column("id", String(20), nullable=True),
    Column("ref_id", String(20), nullable=True),
    Column("Ro", Float, nullable=True)
)


valence_ref = Table("valence_ref",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("reference", String(255), nullable=True)
)


pdbx_audit = Table("pdbx_audit",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("current_version", String(20))
)


pdbx_version = Table("pdbx_version",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("revision_date", DateTime),
    Column("major_version", Integer, primary_key=True),
    Column("minor_version", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("revision_type", String(128), primary_key=True)
)


pdbx_audit_author = Table("pdbx_audit_author",
    metadata_obj,
    Column("address", String(255), nullable=True),
    Column("name", String(128)),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_database_message = Table("pdbx_database_message",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("message_id", String(255), primary_key=True),
    Column("date", Date),
    Column("content_type", String(20)),
    Column("message_type", String(20)),
    Column("sender", String(255), nullable=True),
    Column("sender_address_fax", String(25), nullable=True),
    Column("sender_address_phone", String(25), nullable=True),
    Column("sender_address_email", String(80), nullable=True),
    Column("sender_address_mail", String(255), nullable=True),
    Column("receiver", String(255), nullable=True),
    Column("receiver_address_fax", String(25), nullable=True),
    Column("receiver_address_phone", String(25), nullable=True),
    Column("receiver_address_email", String(80), nullable=True),
    Column("receiver_address_mail", String(255), nullable=True),
    Column("message", String(255), nullable=True)
)


pdbx_database_PDB_obs_spr = Table("pdbx_database_PDB_obs_spr",
    metadata_obj,
    Column("id", String(20)),
    Column("date", Date),
    Column("pdb_id", String(20), primary_key=True),
    Column("replace_pdb_id", String(255), primary_key=True),
    Column("details", String(255), nullable=True)
)


pdbx_database_proc = Table("pdbx_database_proc",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cycle_id", String(20), primary_key=True),
    Column("date_begin_cycle", Date),
    Column("date_end_cycle", Date),
    Column("details", String(255), nullable=True)
)


pdbx_database_remark = Table("pdbx_database_remark",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("text", String(255), nullable=True)
)


pdbx_database_status = Table("pdbx_database_status",
    metadata_obj,
    Column("status_code", String(20)),
    Column("author_release_status_code", String(20), nullable=True),
    Column("status_code_sf", String(20), nullable=True),
    Column("status_code_mr", String(20), nullable=True),
    Column("dep_release_code_coordinates", String(128), nullable=True, default="RELEASE NOW"),
    Column("dep_release_code_sequence", String(128), nullable=True, default="RELEASE NOW"),
    Column("dep_release_code_struct_fact", String(128), nullable=True, default="RELEASE NOW"),
    Column("dep_release_code_nmr_constraints", String(128), nullable=True, default="RELEASE NOW"),
    Column("entry_id", String(20), primary_key=True),
    Column("recvd_deposit_form", String(2), nullable=True),
    Column("date_deposition_form", Date, nullable=True),
    Column("date_begin_deposition", Date, nullable=True),
    Column("date_begin_processing", Date, nullable=True),
    Column("date_end_processing", Date, nullable=True),
    Column("date_begin_release_preparation", Date, nullable=True),
    Column("date_author_release_request", Date, nullable=True),
    Column("recvd_coordinates", String(2), nullable=True),
    Column("date_coordinates", Date, nullable=True),
    Column("recvd_struct_fact", String(2), nullable=True),
    Column("date_struct_fact", Date, nullable=True),
    Column("recvd_nmr_constraints", String(2), nullable=True),
    Column("date_nmr_constraints", Date, nullable=True),
    Column("recvd_internal_approval", String(2), nullable=True),
    Column("recvd_manuscript", String(2), nullable=True),
    Column("date_manuscript", Date, nullable=True),
    Column("name_depositor", String(255), nullable=True),
    Column("recvd_author_approval", String(2), nullable=True),
    Column("author_approval_type", String(20), nullable=True),
    Column("date_author_approval", Date, nullable=True),
    Column("recvd_initial_deposition_date", DateTime, nullable=True),
    Column("date_submitted", Date, nullable=True),
    Column("rcsb_annotator", String(20), nullable=True),
    Column("date_of_sf_release", DateTime, nullable=True),
    Column("date_of_mr_release", DateTime, nullable=True),
    Column("date_of_PDB_release", Date, nullable=True),
    Column("date_hold_coordinates", Date, nullable=True),
    Column("date_hold_struct_fact", Date, nullable=True),
    Column("date_hold_nmr_constraints", Date, nullable=True),
    Column("hold_for_publication", String(2), nullable=True),
    Column("SG_entry", String(2), nullable=True),
    Column("pdb_date_of_author_approval", Date, nullable=True),
    Column("deposit_site", String(20), nullable=True),
    Column("process_site", String(20), nullable=True),
    Column("dep_release_code_chemical_shifts", String(128), nullable=True, default="RELEASE NOW"),
    Column("recvd_chemical_shifts", String(2), nullable=True),
    Column("date_chemical_shifts", Date, nullable=True),
    Column("date_hold_chemical_shifts", Date, nullable=True),
    Column("status_code_cs", String(20), nullable=True),
    Column("date_of_cs_release", DateTime, nullable=True),
    Column("date_nmr_data", Date, nullable=True),
    Column("date_hold_nmr_data", Date, nullable=True),
    Column("date_of_nmr_data_release", DateTime, nullable=True),
    Column("dep_release_code_nmr_data", String(128), nullable=True, default="RELEASE NOW"),
    Column("recvd_nmr_data", String(2), nullable=True),
    Column("status_code_nmr_data", String(20), nullable=True),
    Column("methods_development_category", String(128), nullable=True),
    Column("pdb_format_compatible", String(2), nullable=True, default="Y"),
    Column("post_rel_status", String(20), nullable=True),
    Column("post_rel_recvd_coord", String(20), nullable=True),
    Column("post_rel_recvd_coord_date", DateTime, nullable=True),
    Column("auth_req_rel_date", DateTime, nullable=True),
    Column("ndb_tid", String(20), nullable=True),
    Column("status_coordinates_in_NDB", String(2), nullable=True),
    Column("date_revised", DateTime, nullable=True),
    Column("replaced_entry_id", String(20), nullable=True),
    Column("revision_id", String(20), nullable=True),
    Column("revision_description", String(255), nullable=True),
    Column("pdbx_annotator", String(20), nullable=True),
    Column("date_of_NDB_release", DateTime, nullable=True),
    Column("date_released_to_PDB", DateTime, nullable=True),
    Column("skip_PDB_REMARK_500", String(2), nullable=True, default="N"),
    Column("skip_PDB_REMARK", String(128), nullable=True),
    Column("title_suppression", String(2), nullable=True, default="N"),
    Column("date_accepted_terms_and_conditions", DateTime, nullable=True)
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
    Column("seq_one_letter_code", String(255), nullable=True)
)


pdbx_poly_seq_scheme = Table("pdbx_poly_seq_scheme",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("seq_id", Integer, primary_key=True),
    Column("hetero", String(10), nullable=True, default="no"),
    Column("mon_id", String(10), primary_key=True),
    Column("pdb_strand_id", String(20), nullable=True),
    Column("ndb_seq_num", Integer, nullable=True),
    Column("pdb_seq_num", String(20), nullable=True),
    Column("auth_seq_num", String(20), nullable=True),
    Column("pdb_mon_id", String(20), nullable=True),
    Column("auth_mon_id", String(20), nullable=True),
    Column("pdb_ins_code", String(20), nullable=True)
)


pdbx_nonpoly_scheme = Table("pdbx_nonpoly_scheme",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("entity_id", String(20), nullable=True),
    Column("mon_id", String(10), nullable=True),
    Column("pdb_strand_id", String(20), nullable=True),
    Column("ndb_seq_num", String(20), primary_key=True),
    Column("pdb_seq_num", String(20), nullable=True),
    Column("auth_seq_num", String(20), nullable=True),
    Column("pdb_mon_id", String(20), nullable=True),
    Column("auth_mon_id", String(20), nullable=True),
    Column("pdb_ins_code", String(20), nullable=True)
)


pdbx_refine = Table("pdbx_refine",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("R_factor_all_no_cutoff", Float, nullable=True),
    Column("R_factor_obs_no_cutoff", Float, nullable=True),
    Column("free_R_factor_4sig_cutoff", Float, nullable=True),
    Column("free_R_factor_no_cutoff", Float, nullable=True),
    Column("free_R_error_no_cutoff", Float, nullable=True),
    Column("free_R_val_test_set_size_perc_no_cutoff", Float, nullable=True),
    Column("free_R_val_test_set_ct_no_cutoff", Float, nullable=True),
    Column("number_reflns_obs_no_cutoff", Float, nullable=True),
    Column("R_factor_all_4sig_cutoff", Float, nullable=True),
    Column("R_factor_obs_4sig_cutoff", Float, nullable=True),
    Column("free_R_val_4sig_cutoff", Float, nullable=True),
    Column("free_R_val_test_set_size_perc_4sig_cutoff", Float, nullable=True),
    Column("free_R_val_test_set_ct_4sig_cutoff", Float, nullable=True),
    Column("number_reflns_obs_4sig_cutoff", Float, nullable=True),
    Column("free_R_val_no_cutoff", Float, nullable=True)
)


pdbx_struct_sheet_hbond = Table("pdbx_struct_sheet_hbond",
    metadata_obj,
    Column("range_id_1", String(20), primary_key=True),
    Column("range_id_2", String(20), primary_key=True),
    Column("sheet_id", String(20), primary_key=True),
    Column("range_1_label_atom_id", String(6)),
    Column("range_1_label_seq_id", Integer),
    Column("range_1_label_comp_id", String(10), nullable=True),
    Column("range_1_label_asym_id", String(20), nullable=True),
    Column("range_1_auth_atom_id", String(6), nullable=True),
    Column("range_1_auth_seq_id", String(20), nullable=True),
    Column("range_1_auth_comp_id", String(20), nullable=True),
    Column("range_1_auth_asym_id", String(20), nullable=True),
    Column("range_1_PDB_ins_code", String(20), nullable=True),
    Column("range_2_label_atom_id", String(6)),
    Column("range_2_label_seq_id", Integer),
    Column("range_2_label_comp_id", String(10), nullable=True),
    Column("range_2_label_asym_id", String(20), nullable=True),
    Column("range_2_auth_atom_id", String(6), nullable=True),
    Column("range_2_auth_seq_id", String(20), nullable=True),
    Column("range_2_auth_comp_id", String(20), nullable=True),
    Column("range_2_auth_asym_id", String(20), nullable=True),
    Column("range_2_PDB_ins_code", String(20), nullable=True)
)


pdbx_xplor_file = Table("pdbx_xplor_file",
    metadata_obj,
    Column("serial_no", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("param_file", String(128), nullable=True),
    Column("topol_file", String(128), nullable=True)
)


pdbx_refine_aux_file = Table("pdbx_refine_aux_file",
    metadata_obj,
    Column("serial_no", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128), primary_key=True),
    Column("file_name", String(128), nullable=True),
    Column("file_type", String(128), nullable=True)
)


pdbx_database_related = Table("pdbx_database_related",
    metadata_obj,
    Column("db_name", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("db_id", String(80), primary_key=True),
    Column("content_type", String(128), primary_key=True)
)


pdbx_entity_assembly = Table("pdbx_entity_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("biol_id", String(128)),
    Column("num_copies", Integer)
)


pdbx_exptl_crystal_grow_comp = Table("pdbx_exptl_crystal_grow_comp",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("comp_id", String(20), primary_key=True),
    Column("comp_name", String(128), nullable=True),
    Column("sol_id", String(128), nullable=True),
    Column("conc", Float, nullable=True),
    Column("conc_range", String(128), nullable=True),
    Column("conc_units", String(128), nullable=True)
)


pdbx_exptl_crystal_grow_sol = Table("pdbx_exptl_crystal_grow_sol",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("sol_id", String(128), primary_key=True),
    Column("volume", Float, nullable=True),
    Column("volume_units", String(128), nullable=True),
    Column("pH", Float, nullable=True)
)


pdbx_exptl_crystal_cryo_treatment = Table("pdbx_exptl_crystal_cryo_treatment",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("final_solution_details", String(255), nullable=True),
    Column("soaking_details", String(255), nullable=True),
    Column("cooling_details", String(255), nullable=True),
    Column("annealing_details", String(255), nullable=True)
)


pdbx_refine_tls = Table("pdbx_refine_tls",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128)),
    Column("details", String(255), nullable=True),
    Column("method", String(10), nullable=True),
    Column("origin_x", Float, nullable=True),
    Column("origin_y", Float, nullable=True),
    Column("origin_z", Float, nullable=True),
    Column("T[1][1]", Float, nullable=True),
    Column("T[1][1]_esd", Float, nullable=True, default=0.0),
    Column("T[1][2]", Float, nullable=True),
    Column("T[1][2]_esd", Float, nullable=True, default=0.0),
    Column("T[1][3]", Float, nullable=True),
    Column("T[1][3]_esd", Float, nullable=True, default=0.0),
    Column("T[2][2]", Float, nullable=True),
    Column("T[2][2]_esd", Float, nullable=True, default=0.0),
    Column("T[2][3]", Float, nullable=True),
    Column("T[2][3]_esd", Float, nullable=True, default=0.0),
    Column("T[3][3]", Float, nullable=True),
    Column("T[3][3]_esd", Float, nullable=True, default=0.0),
    Column("L[1][1]", Float, nullable=True),
    Column("L[1][1]_esd", Float, nullable=True, default=0.0),
    Column("L[1][2]", Float, nullable=True),
    Column("L[1][2]_esd", Float, nullable=True, default=0.0),
    Column("L[1][3]", Float, nullable=True),
    Column("L[1][3]_esd", Float, nullable=True, default=0.0),
    Column("L[2][2]", Float, nullable=True),
    Column("L[2][2]_esd", Float, nullable=True, default=0.0),
    Column("L[2][3]", Float, nullable=True),
    Column("L[2][3]_esd", Float, nullable=True, default=0.0),
    Column("L[3][3]", Float, nullable=True),
    Column("L[3][3]_esd", Float, nullable=True, default=0.0),
    Column("S[1][1]", Float, nullable=True),
    Column("S[1][1]_esd", Float, nullable=True, default=0.0),
    Column("S[1][2]", Float, nullable=True),
    Column("S[1][2]_esd", Float, nullable=True, default=0.0),
    Column("S[1][3]", Float, nullable=True),
    Column("S[1][3]_esd", Float, nullable=True, default=0.0),
    Column("S[2][1]", Float, nullable=True),
    Column("S[2][1]_esd", Float, nullable=True, default=0.0),
    Column("S[2][2]", Float, nullable=True),
    Column("S[2][2]_esd", Float, nullable=True, default=0.0),
    Column("S[2][3]", Float, nullable=True),
    Column("S[2][3]_esd", Float, nullable=True, default=0.0),
    Column("S[3][1]", Float, nullable=True),
    Column("S[3][1]_esd", Float, nullable=True, default=0.0),
    Column("S[3][2]", Float, nullable=True),
    Column("S[3][2]_esd", Float, nullable=True, default=0.0),
    Column("S[3][3]", Float, nullable=True),
    Column("S[3][3]_esd", Float, nullable=True, default=0.0)
)


pdbx_refine_tls_group = Table("pdbx_refine_tls_group",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("pdbx_refine_id", String(128)),
    Column("refine_tls_id", String(20)),
    Column("beg_label_asym_id", String(20), nullable=True),
    Column("beg_label_seq_id", Integer, nullable=True),
    Column("beg_auth_asym_id", String(20), nullable=True),
    Column("beg_auth_seq_id", String(20), nullable=True),
    Column("beg_PDB_ins_code", String(20), nullable=True),
    Column("end_label_asym_id", String(20), nullable=True),
    Column("end_label_seq_id", Integer, nullable=True),
    Column("end_auth_asym_id", String(20), nullable=True),
    Column("end_auth_seq_id", String(20), nullable=True),
    Column("end_PDB_ins_code", String(20), nullable=True),
    Column("selection", String(128), nullable=True),
    Column("selection_details", String(255), nullable=True)
)


pdbx_contact_author = Table("pdbx_contact_author",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("address_1", String(255), nullable=True),
    Column("address_2", String(255), nullable=True),
    Column("address_3", String(255), nullable=True),
    Column("legacy_address", String(255), nullable=True),
    Column("city", String(128), nullable=True),
    Column("state_province", String(128), nullable=True),
    Column("postal_code", String(128), nullable=True),
    Column("email", String(128)),
    Column("fax", String(128), nullable=True),
    Column("name_first", String(128)),
    Column("name_last", String(128)),
    Column("name_mi", String(128), nullable=True),
    Column("name_salutation", String(128), nullable=True),
    Column("country", String(128), nullable=True),
    Column("continent", String(128), nullable=True),
    Column("phone", String(128), nullable=True),
    Column("role", String(128), nullable=True),
    Column("organization_type", String(128), nullable=True),
    Column("identifier_ORCID", String(20), nullable=True)
)


pdbx_SG_project = Table("pdbx_SG_project",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("project_name", String(255), nullable=True),
    Column("full_name_of_center", String(255), nullable=True),
    Column("initial_of_center", String(255), nullable=True)
)


pdbx_atom_site_aniso_tls = Table("pdbx_atom_site_aniso_tls",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type_symbol", String(20)),
    Column("tls_group_id", String(20), primary_key=True),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("auth_atom_id", String(6)),
    Column("auth_asym_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_alt_id", String(20)),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_atom_id", String(6), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("U_tls[1][1]", Float),
    Column("U_tls[2][2]", Float),
    Column("U_tls[3][3]", Float),
    Column("U_tls[1][2]", Float),
    Column("U_tls[1][3]", Float),
    Column("U_tls[2][3]", Float)
)


pdbx_nmr_details = Table("pdbx_nmr_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("text", String(255), nullable=True)
)


pdbx_nmr_sample_details = Table("pdbx_nmr_sample_details",
    metadata_obj,
    Column("solution_id", String(20), primary_key=True),
    Column("contents", String(255), nullable=True),
    Column("solvent_system", String(255), nullable=True),
    Column("label", String(128), nullable=True, default="sample_1"),
    Column("type", String(128), nullable=True, default="solution"),
    Column("details", String(255), nullable=True)
)


pdbx_nmr_exptl_sample = Table("pdbx_nmr_exptl_sample",
    metadata_obj,
    Column("solution_id", String(20), primary_key=True),
    Column("component", String(128), primary_key=True),
    Column("concentration", Float, nullable=True),
    Column("concentration_range", String(30), nullable=True),
    Column("concentration_units", String(128), nullable=True),
    Column("isotopic_labeling", String(128), nullable=True),
    Column("concentration_err", Float, nullable=True)
)


pdbx_nmr_exptl_sample_conditions = Table("pdbx_nmr_exptl_sample_conditions",
    metadata_obj,
    Column("conditions_id", String(20), primary_key=True),
    Column("temperature", String(30), nullable=True),
    Column("pressure_units", String(20), nullable=True),
    Column("pressure", String(128), nullable=True),
    Column("pH", String(30), nullable=True),
    Column("ionic_strength", String(128), nullable=True),
    Column("details", String(255), nullable=True),
    Column("ionic_strength_err", Float, nullable=True),
    Column("ionic_strength_units", String(128), nullable=True),
    Column("label", String(128), nullable=True, default="sample_conditions_1"),
    Column("pH_err", Float, nullable=True),
    Column("pH_units", String(128), nullable=True),
    Column("pressure_err", Float, nullable=True),
    Column("temperature_err", Float, nullable=True),
    Column("temperature_units", String(128), nullable=True)
)


pdbx_nmr_spectrometer = Table("pdbx_nmr_spectrometer",
    metadata_obj,
    Column("spectrometer_id", String(20), primary_key=True),
    Column("model", String(128), nullable=True),
    Column("type", String(128), nullable=True),
    Column("manufacturer", String(128), nullable=True),
    Column("field_strength", Float, nullable=True),
    Column("details", String(255), nullable=True),
    Column("name", String(128), nullable=True)
)


pdbx_nmr_exptl = Table("pdbx_nmr_exptl",
    metadata_obj,
    Column("experiment_id", String(20), primary_key=True),
    Column("conditions_id", String(20), primary_key=True),
    Column("solution_id", String(20), primary_key=True),
    Column("type", String(128), nullable=True),
    Column("spectrometer_id", Integer, nullable=True),
    Column("sample_state", String(128), nullable=True, default="isotropic")
)


pdbx_nmr_software = Table("pdbx_nmr_software",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("classification", String(128)),
    Column("name", String(128)),
    Column("version", String(128), nullable=True),
    Column("authors", String(255), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_nmr_constraints = Table("pdbx_nmr_constraints",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("NOE_constraints_total", Integer, nullable=True),
    Column("NOE_intraresidue_total_count", Integer, nullable=True),
    Column("NOE_interentity_total_count", Integer, nullable=True),
    Column("NOE_sequential_total_count", Integer, nullable=True),
    Column("NOE_medium_range_total_count", Integer, nullable=True),
    Column("NOE_long_range_total_count", Integer, nullable=True),
    Column("protein_phi_angle_constraints_total_count", Integer, nullable=True),
    Column("protein_psi_angle_constraints_total_count", Integer, nullable=True),
    Column("protein_chi_angle_constraints_total_count", Integer, nullable=True),
    Column("protein_other_angle_constraints_total_count", Integer, nullable=True),
    Column("NOE_interproton_distance_evaluation", String(255), nullable=True),
    Column("NOE_pseudoatom_corrections", String(255), nullable=True),
    Column("NOE_motional_averaging_correction", String(255), nullable=True),
    Column("hydrogen_bond_constraints_total_count", Integer, nullable=True),
    Column("disulfide_bond_constraints_total_count", Integer, nullable=True),
    Column("NA_alpha-angle_constraints_total_count", Integer, nullable=True),
    Column("NA_beta-angle_constraints_total_count", Integer, nullable=True),
    Column("NA_gamma-angle_constraints_total_count", Integer, nullable=True),
    Column("NA_delta-angle_constraints_total_count", Integer, nullable=True),
    Column("NA_epsilon-angle_constraints_total_count", Integer, nullable=True),
    Column("NA_chi-angle_constraints_total_count", Integer, nullable=True),
    Column("NA_other-angle_constraints_total_count", Integer, nullable=True),
    Column("NA_sugar_pucker_constraints_total_count", Integer, nullable=True)
)


pdbx_nmr_ensemble = Table("pdbx_nmr_ensemble",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("conformers_calculated_total_number", Integer, nullable=True),
    Column("conformers_submitted_total_number", Integer, nullable=True),
    Column("conformer_selection_criteria", String(255), nullable=True),
    Column("representative_conformer", Integer, nullable=True),
    Column("average_constraints_per_residue", Integer, nullable=True),
    Column("average_constraint_violations_per_residue", Integer, nullable=True),
    Column("maximum_distance_constraint_violation", Float, nullable=True),
    Column("average_distance_constraint_violation", Float, nullable=True),
    Column("maximum_upper_distance_constraint_violation", Float, nullable=True),
    Column("maximum_lower_distance_constraint_violation", Float, nullable=True),
    Column("distance_constraint_violation_method", String(255), nullable=True),
    Column("maximum_torsion_angle_constraint_violation", Float, nullable=True),
    Column("average_torsion_angle_constraint_violation", Float, nullable=True),
    Column("torsion_angle_constraint_violation_method", String(255), nullable=True)
)


pdbx_nmr_ensemble_rms = Table("pdbx_nmr_ensemble_rms",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("residue_range_begin", Integer, nullable=True),
    Column("chain_range_begin", String(20), nullable=True),
    Column("residue_range_end", Integer, nullable=True),
    Column("chain_range_end", String(20), nullable=True),
    Column("atom_type", String(128), nullable=True),
    Column("distance_rms_dev", Float, nullable=True),
    Column("distance_rms_dev_error", Float, nullable=True),
    Column("covalent_bond_rms_dev", Float, nullable=True),
    Column("covalent_bond_rms_dev_error", Float, nullable=True),
    Column("bond_angle_rms_dev", Float, nullable=True),
    Column("bond_angle_rms_dev_error", Float, nullable=True),
    Column("improper_torsion_angle_rms_dev", Float, nullable=True),
    Column("improper_torsion_angle_rms_dev_error", Float, nullable=True),
    Column("peptide_planarity_rms_dev", Float, nullable=True),
    Column("peptide_planarity_rms_dev_error", Float, nullable=True),
    Column("dihedral_angles_rms_dev", Float, nullable=True),
    Column("dihedral_angles_rms_dev_error", Float, nullable=True),
    Column("coord_average_rmsd_method", String(255), nullable=True)
)


pdbx_nmr_representative = Table("pdbx_nmr_representative",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("conformer_id", String(128), nullable=True),
    Column("selection_criteria", String(128), nullable=True)
)


pdbx_nmr_refine = Table("pdbx_nmr_refine",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("software_ordinal", Integer, primary_key=True)
)


pdbx_nmr_force_constants = Table("pdbx_nmr_force_constants",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("exptl_distance_term", Float, nullable=True),
    Column("exptl_distance_term_units", String(20), nullable=True),
    Column("exptl_torsion_angles_term", Float, nullable=True),
    Column("exptl_torsion_angles_term_units", String(20), nullable=True),
    Column("exptl_J_coupling_term", Float, nullable=True),
    Column("exptl_J_coupling_term_units", String(20), nullable=True),
    Column("exptl_13C_shift_term", Float, nullable=True),
    Column("exptl_13C_shift_term_units", String(20), nullable=True),
    Column("exptl_1H_shift_term", Float, nullable=True),
    Column("exptl_1H_shift_term_units", String(20), nullable=True),
    Column("exptl_dipolar_coupling_term", Float, nullable=True),
    Column("exptl_dipolar_coupling_term_units", String(20), nullable=True),
    Column("exptl_D_isotope_shift_term", Float, nullable=True),
    Column("exptl_D_isotope_shift_term_units", String(20), nullable=True),
    Column("covalent_geom_bond_term", Float, nullable=True),
    Column("covalent_geom_bond_term_units", String(20), nullable=True),
    Column("covalent_geom_angles_term", Float, nullable=True),
    Column("covalent_geom_angles_term_units", String(20), nullable=True),
    Column("covalent_geom_impropers_term", Float, nullable=True),
    Column("covalent_geom_impropers_term_units", String(20), nullable=True),
    Column("non-bonded_inter_van_der_Waals_term_type", String(255), nullable=True),
    Column("non-bonded_inter_van_der_Waals_term", Float, nullable=True),
    Column("non-bonded_inter_van_der_Waals_term_units", String(20), nullable=True),
    Column("non-bonded_inter_conf_db_potential_term", Float, nullable=True),
    Column("non-bonded_inter_radius_of_gyration_term", Float, nullable=True),
    Column("non-bonded_inter_radius_of_gyration_term_units", String(20), nullable=True)
)


ndb_struct_conf_na = Table("ndb_struct_conf_na",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("feature", String(128), primary_key=True),
    Column("feature_count", Integer, nullable=True)
)


ndb_struct_feature_na = Table("ndb_struct_feature_na",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("feature", String(128), primary_key=True),
    Column("feature_count", Integer, nullable=True)
)


ndb_struct_na_base_pair = Table("ndb_struct_na_base_pair",
    metadata_obj,
    Column("model_number", Integer, primary_key=True),
    Column("pair_number", Integer),
    Column("pair_name", String(128)),
    Column("i_label_asym_id", String(20), primary_key=True),
    Column("i_label_comp_id", String(10), primary_key=True),
    Column("i_label_seq_id", Integer, primary_key=True),
    Column("i_symmetry", String(10), primary_key=True, default="1_555"),
    Column("j_label_asym_id", String(20), primary_key=True),
    Column("j_label_comp_id", String(10), primary_key=True),
    Column("j_label_seq_id", Integer, primary_key=True),
    Column("j_symmetry", String(10), primary_key=True, default="1_555"),
    Column("i_auth_asym_id", String(20)),
    Column("i_auth_seq_id", String(20)),
    Column("i_PDB_ins_code", String(20), nullable=True),
    Column("j_auth_asym_id", String(20)),
    Column("j_auth_seq_id", String(20)),
    Column("j_PDB_ins_code", String(20), nullable=True),
    Column("shear", Float, nullable=True),
    Column("stretch", Float, nullable=True),
    Column("stagger", Float, nullable=True),
    Column("buckle", Float, nullable=True),
    Column("propeller", Float, nullable=True),
    Column("opening", Float, nullable=True),
    Column("hbond_type_12", Integer, nullable=True),
    Column("hbond_type_28", Integer, nullable=True),
    Column("hbond_type_leontis_westhof", String(128), nullable=True)
)


ndb_struct_na_base_pair_step = Table("ndb_struct_na_base_pair_step",
    metadata_obj,
    Column("model_number", Integer, primary_key=True),
    Column("step_number", Integer),
    Column("step_name", String(128)),
    Column("i_label_asym_id_1", String(20), primary_key=True),
    Column("i_label_comp_id_1", String(10), primary_key=True),
    Column("i_label_seq_id_1", Integer, primary_key=True),
    Column("i_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("j_label_asym_id_1", String(20), primary_key=True),
    Column("j_label_comp_id_1", String(10), primary_key=True),
    Column("j_label_seq_id_1", Integer, primary_key=True),
    Column("j_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("i_label_asym_id_2", String(20), primary_key=True),
    Column("i_label_comp_id_2", String(10), primary_key=True),
    Column("i_label_seq_id_2", Integer, primary_key=True),
    Column("i_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("j_label_asym_id_2", String(20), primary_key=True),
    Column("j_label_comp_id_2", String(10), primary_key=True),
    Column("j_label_seq_id_2", Integer, primary_key=True),
    Column("j_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("i_auth_asym_id_1", String(20)),
    Column("i_auth_seq_id_1", String(20)),
    Column("i_PDB_ins_code_1", String(20), nullable=True),
    Column("j_auth_asym_id_1", String(20)),
    Column("j_auth_seq_id_1", String(20)),
    Column("j_PDB_ins_code_1", String(20), nullable=True),
    Column("i_auth_asym_id_2", String(20)),
    Column("i_auth_seq_id_2", String(20)),
    Column("i_PDB_ins_code_2", String(20), nullable=True),
    Column("j_auth_asym_id_2", String(20)),
    Column("j_auth_seq_id_2", String(20)),
    Column("j_PDB_ins_code_2", String(20), nullable=True),
    Column("shift", Float, nullable=True),
    Column("slide", Float, nullable=True),
    Column("rise", Float, nullable=True),
    Column("tilt", Float, nullable=True),
    Column("roll", Float, nullable=True),
    Column("twist", Float, nullable=True),
    Column("x_displacement", Float, nullable=True),
    Column("y_displacement", Float, nullable=True),
    Column("helical_rise", Float, nullable=True),
    Column("inclination", Float, nullable=True),
    Column("tip", Float, nullable=True),
    Column("helical_twist", Float, nullable=True)
)


ndb_original_ndb_coordinates = Table("ndb_original_ndb_coordinates",
    metadata_obj,
    Column("coord_section", String(255), primary_key=True)
)


pdbx_entity_nonpoly = Table("pdbx_entity_nonpoly",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("comp_id", String(10), nullable=True),
    Column("name", String(255), nullable=True)
)


pdbx_phasing_dm = Table("pdbx_phasing_dm",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(128), nullable=True),
    Column("mask_type", String(128), nullable=True),
    Column("fom_acentric", Float, nullable=True),
    Column("fom_centric", Float, nullable=True),
    Column("fom", Float, nullable=True),
    Column("reflns_acentric", Integer, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("delta_phi_initial", Float, nullable=True),
    Column("delta_phi_final", Float, nullable=True)
)


pdbx_phasing_dm_shell = Table("pdbx_phasing_dm_shell",
    metadata_obj,
    Column("d_res_high", Float, primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("fom_acentric", Float, nullable=True),
    Column("fom_centric", Float, nullable=True),
    Column("fom", Float, nullable=True),
    Column("reflns_acentric", Integer, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("delta_phi_initial", Float, nullable=True),
    Column("delta_phi_final", Float, nullable=True)
)


pdbx_phasing_MAD_shell = Table("pdbx_phasing_MAD_shell",
    metadata_obj,
    Column("d_res_low", Float, primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("reflns_acentric", Float, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("fom_acentric", Float, nullable=True),
    Column("fom_centric", Float, nullable=True),
    Column("fom", Float, nullable=True),
    Column("R_cullis_centric", Float, nullable=True),
    Column("R_cullis_acentric", Float, nullable=True),
    Column("R_cullis", Float, nullable=True),
    Column("R_kraut_centric", Float, nullable=True),
    Column("R_kraut_acentric", Float, nullable=True),
    Column("R_kraut", Float, nullable=True),
    Column("loc_centric", Float, nullable=True),
    Column("loc_acentric", Float, nullable=True),
    Column("loc", Float, nullable=True),
    Column("power_centric", Float, nullable=True),
    Column("power_acentric", Float, nullable=True),
    Column("power", Float, nullable=True)
)


pdbx_phasing_MAD_set = Table("pdbx_phasing_MAD_set",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("d_res_low", Float, nullable=True),
    Column("d_res_high", Float, nullable=True),
    Column("number_of_sites", Integer, nullable=True),
    Column("reflns_acentric", Integer, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("fom_acentric", Float, nullable=True),
    Column("fom_centric", Float, nullable=True),
    Column("fom", Float, nullable=True),
    Column("R_cullis_centric", Float, nullable=True),
    Column("R_cullis_acentric", Float, nullable=True),
    Column("R_cullis", Float, nullable=True),
    Column("R_kraut_centric", Float, nullable=True),
    Column("R_kraut_acentric", Float, nullable=True),
    Column("R_kraut", Float, nullable=True),
    Column("loc_centric", Float, nullable=True),
    Column("loc_acentric", Float, nullable=True),
    Column("loc", Float, nullable=True),
    Column("power_centric", Float, nullable=True),
    Column("power_acentric", Float, nullable=True),
    Column("power", Float, nullable=True)
)


pdbx_phasing_MAD_set_shell = Table("pdbx_phasing_MAD_set_shell",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("reflns_acentric", Integer, nullable=True),
    Column("reflns_centric", Integer, nullable=True),
    Column("reflns", Integer, nullable=True),
    Column("fom_acentric", Float, nullable=True),
    Column("fom_centric", Float, nullable=True),
    Column("fom", Float, nullable=True),
    Column("R_cullis_centric", Float, nullable=True),
    Column("R_cullis_acentric", Float, nullable=True),
    Column("R_cullis", Float, nullable=True),
    Column("R_kraut_centric", Float, nullable=True),
    Column("R_kraut_acentric", Float, nullable=True),
    Column("R_kraut", Float, nullable=True),
    Column("loc_centric", Float, nullable=True),
    Column("loc_acentric", Float, nullable=True),
    Column("loc", Float, nullable=True),
    Column("power_centric", Float, nullable=True),
    Column("power_acentric", Float, nullable=True),
    Column("power", Float, nullable=True)
)


pdbx_phasing_MAD_set_site = Table("pdbx_phasing_MAD_set_site",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("atom_type_symbol", String(20), nullable=True),
    Column("Cartn_x", Float, nullable=True),
    Column("Cartn_y", Float, nullable=True),
    Column("Cartn_z", Float, nullable=True),
    Column("Cartn_x_esd", Float, nullable=True),
    Column("Cartn_y_esd", Float, nullable=True),
    Column("Cartn_z_esd", Float, nullable=True),
    Column("fract_x", Float, nullable=True),
    Column("fract_y", Float, nullable=True),
    Column("fract_z", Float, nullable=True),
    Column("fract_x_esd", Float, nullable=True),
    Column("fract_y_esd", Float, nullable=True),
    Column("fract_z_esd", Float, nullable=True),
    Column("b_iso", Float, nullable=True),
    Column("b_iso_esd", Float, nullable=True),
    Column("occupancy", Float, nullable=True),
    Column("occupancy_esd", Float, nullable=True),
    Column("set_id", String(20), nullable=True),
    Column("occupancy_iso", Float, nullable=True)
)


pdbx_phasing_MR = Table("pdbx_phasing_MR",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("method_rotation", String(128), nullable=True),
    Column("d_res_high_rotation", Float, nullable=True),
    Column("d_res_low_rotation", Float, nullable=True),
    Column("sigma_F_rotation", Float, nullable=True),
    Column("sigma_I_rotation", Float, nullable=True),
    Column("reflns_percent_rotation", Float, nullable=True),
    Column("method_translation", String(128), nullable=True),
    Column("d_res_high_translation", Float, nullable=True),
    Column("d_res_low_translation", Float, nullable=True),
    Column("sigma_F_translation", Float, nullable=True),
    Column("sigma_I_translation", Float, nullable=True),
    Column("reflns_percent_translation", Float, nullable=True),
    Column("correlation_coeff_Io_to_Ic", Float, nullable=True),
    Column("correlation_coeff_Fo_to_Fc", Float, nullable=True),
    Column("R_factor", Float, nullable=True),
    Column("R_rigid_body", Float, nullable=True),
    Column("packing", Float, nullable=True),
    Column("model_details", String(255), nullable=True),
    Column("native_set_id", String(128), nullable=True),
    Column("d_res_high_fit", Float, nullable=True),
    Column("d_res_low_fit", Float, nullable=True),
    Column("zscore_rotation", Float, nullable=True),
    Column("LL_gain_rotation", Float, nullable=True),
    Column("zscore_translation", Float, nullable=True),
    Column("LL_gain_translation", Float, nullable=True)
)


pdbx_refine_component = Table("pdbx_refine_component",
    metadata_obj,
    Column("label_alt_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_comp_id", String(10), primary_key=True),
    Column("label_seq_id", Integer, primary_key=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("B_iso", Float, nullable=True),
    Column("B_iso_main_chain", Float, nullable=True),
    Column("B_iso_side_chain", Float, nullable=True),
    Column("shift", Float, nullable=True),
    Column("shift_side_chain", Float, nullable=True),
    Column("shift_main_chain", Float, nullable=True),
    Column("correlation", Float, nullable=True),
    Column("correlation_side_chain", Float, nullable=True),
    Column("correlation_main_chain", Float, nullable=True),
    Column("real_space_R", Float, nullable=True),
    Column("real_space_R_side_chain", Float, nullable=True),
    Column("real_space_R_main_chain", Float, nullable=True),
    Column("connect", Float, nullable=True),
    Column("density_index", Float, nullable=True),
    Column("density_index_main_chain", Float, nullable=True),
    Column("density_index_side_chain", Float, nullable=True),
    Column("density_ratio", Float, nullable=True),
    Column("density_ratio_main_chain", Float, nullable=True),
    Column("density_ratio_side_chain", Float, nullable=True)
)


pdbx_entity_prod_protocol = Table("pdbx_entity_prod_protocol",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("protocol", String(255)),
    Column("protocol_type", String(20), primary_key=True)
)


pdbx_entity_src_gen_prod_other = Table("pdbx_entity_src_gen_prod_other",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("process_name", String(255), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_entity_src_gen_prod_other_parameter = Table("pdbx_entity_src_gen_prod_other_parameter",
    metadata_obj,
    Column("step_id", Integer, primary_key=True),
    Column("parameter", String(128), primary_key=True),
    Column("value", String(255)),
    Column("details", String(255))
)


pdbx_entity_src_gen_prod_pcr = Table("pdbx_entity_src_gen_prod_pcr",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("forward_primer_id", String(20)),
    Column("reverse_primer_id", String(20)),
    Column("reaction_details", String(255), nullable=True),
    Column("purification_details", String(255), nullable=True),
    Column("summary", String(255), nullable=True)
)


pdbx_entity_src_gen_prod_digest = Table("pdbx_entity_src_gen_prod_digest",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("restriction_enzyme_1", String(255)),
    Column("restriction_enzyme_2", String(255), nullable=True),
    Column("purification_details", String(255), nullable=True),
    Column("summary", String(255), nullable=True)
)


pdbx_entity_src_gen_clone = Table("pdbx_entity_src_gen_clone",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("gene_insert_method", String(20)),
    Column("vector_name", String(255), nullable=True),
    Column("vector_details", String(255), nullable=True),
    Column("transformation_method", String(20), nullable=True),
    Column("marker", String(20), nullable=True),
    Column("verification_method", String(20), nullable=True),
    Column("purification_details", String(255), nullable=True),
    Column("summary", String(255), nullable=True)
)


pdbx_entity_src_gen_clone_ligation = Table("pdbx_entity_src_gen_clone_ligation",
    metadata_obj,
    Column("step_id", Integer, primary_key=True),
    Column("cleavage_enzymes", String(255)),
    Column("ligation_enzymes", String(255)),
    Column("temperature", Float),
    Column("time", Integer),
    Column("details", String(255), nullable=True)
)


pdbx_entity_src_gen_clone_recombination = Table("pdbx_entity_src_gen_clone_recombination",
    metadata_obj,
    Column("step_id", Integer, primary_key=True),
    Column("system", String(20)),
    Column("recombination_enzymes", String(20)),
    Column("details", String(255), nullable=True)
)


pdbx_entity_src_gen_express = Table("pdbx_entity_src_gen_express",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("promoter_type", String(255)),
    Column("plasmid_id", String(20)),
    Column("vector_type", String(20)),
    Column("N_terminal_seq_tag", String(255)),
    Column("C_terminal_seq_tag", String(255)),
    Column("host_org_scientific_name", String(128), nullable=True),
    Column("host_org_common_name", String(128), nullable=True),
    Column("host_org_variant", String(128), nullable=True),
    Column("host_org_strain", String(128), nullable=True),
    Column("host_org_tissue", String(128), nullable=True),
    Column("host_org_culture_collection", String(128), nullable=True),
    Column("host_org_cell_line", String(128), nullable=True),
    Column("host_org_tax_id", String(128), nullable=True),
    Column("host_org_details", String(255), nullable=True),
    Column("culture_base_media", String(255), nullable=True),
    Column("culture_additives", String(255), nullable=True),
    Column("culture_volume", Float),
    Column("culture_time", Float),
    Column("culture_temperature", Float),
    Column("inducer", String(128), nullable=True),
    Column("inducer_concentration", Float, nullable=True),
    Column("induction_details", String(255), nullable=True),
    Column("multiplicity_of_infection", Float, nullable=True),
    Column("induction_timepoint", Float, nullable=True),
    Column("induction_temperature", Float),
    Column("harvesting_details", String(255), nullable=True),
    Column("storage_details", String(255), nullable=True),
    Column("summary", String(255), nullable=True)
)


pdbx_entity_src_gen_express_timepoint = Table("pdbx_entity_src_gen_express_timepoint",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("serial", Integer, primary_key=True),
    Column("OD", Integer),
    Column("time", Integer)
)


pdbx_entity_src_gen_lysis = Table("pdbx_entity_src_gen_lysis",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("method", String(20)),
    Column("buffer_id", String(20)),
    Column("buffer_volume", Float),
    Column("temperature", Float),
    Column("time", Float),
    Column("details", String(255), nullable=True)
)


pdbx_entity_src_gen_refold = Table("pdbx_entity_src_gen_refold",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("denature_buffer_id", String(20)),
    Column("refold_buffer_id", String(20)),
    Column("temperature", Float),
    Column("time", Float),
    Column("storage_buffer_id", String(20)),
    Column("details", String(255), nullable=True)
)


pdbx_entity_src_gen_proteolysis = Table("pdbx_entity_src_gen_proteolysis",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("details", String(255), nullable=True),
    Column("protease", String(255)),
    Column("protein_protease_ratio", Float, nullable=True),
    Column("cleavage_buffer_id", String(20), nullable=True),
    Column("cleavage_temperature", Float, nullable=True),
    Column("cleavage_time", Float, nullable=True)
)


pdbx_entity_src_gen_chrom = Table("pdbx_entity_src_gen_chrom",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("column_type", String(255)),
    Column("column_volume", Float),
    Column("column_temperature", Float),
    Column("equilibration_buffer_id", String(20)),
    Column("flow_rate", Float, nullable=True),
    Column("elution_buffer_id", String(20)),
    Column("elution_protocol", String(255), nullable=True),
    Column("sample_prep_details", String(255), nullable=True),
    Column("sample_volume", Float),
    Column("sample_concentration", Float, nullable=True),
    Column("sample_conc_method", String(255), nullable=True),
    Column("volume_pooled_fractions", Float),
    Column("yield_pooled_fractions", Float),
    Column("yield_method", String(255)),
    Column("post_treatment", String(255), nullable=True)
)


pdbx_entity_src_gen_fract = Table("pdbx_entity_src_gen_fract",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("next_step_id", Integer),
    Column("end_construct_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("method", String(20)),
    Column("temperature", Float),
    Column("details", String(255), nullable=True),
    Column("protein_location", String(20)),
    Column("protein_volume", Float, nullable=True),
    Column("protein_yield", Float),
    Column("protein_yield_method", String(255))
)


pdbx_entity_src_gen_pure = Table("pdbx_entity_src_gen_pure",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("product_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("conc_device_id", String(20), nullable=True),
    Column("conc_details", String(255), nullable=True),
    Column("conc_assay_method", String(255)),
    Column("protein_concentration", Float),
    Column("protein_yield", Float, nullable=True),
    Column("protein_purity", Float, nullable=True),
    Column("protein_oligomeric_state", Integer, nullable=True),
    Column("storage_buffer_id", String(20)),
    Column("storage_temperature", Float, nullable=True),
    Column("summary", String(255), nullable=True)
)


pdbx_entity_src_gen_character = Table("pdbx_entity_src_gen_character",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("step_id", Integer, primary_key=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("method", String(255)),
    Column("result", String(255)),
    Column("details", String(255), nullable=True)
)


pdbx_construct = Table("pdbx_construct",
    metadata_obj,
    Column("entry_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("organisation", String(128)),
    Column("entity_id", String(20), nullable=True),
    Column("robot_id", String(20), nullable=True),
    Column("date", Date, nullable=True),
    Column("details", String(255), nullable=True),
    Column("class", String(20), nullable=True),
    Column("type", String(20)),
    Column("seq", String(255))
)


pdbx_construct_feature = Table("pdbx_construct_feature",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("construct_id", String(20), primary_key=True),
    Column("entry_id", String(20)),
    Column("start_seq", Integer, nullable=True),
    Column("end_seq", Integer, nullable=True),
    Column("type", String(128), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_robot_system = Table("pdbx_robot_system",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("model", String(128), nullable=True),
    Column("type", String(128), nullable=True),
    Column("manufacturer", String(128), nullable=True)
)


pdbx_buffer = Table("pdbx_buffer",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_buffer_components = Table("pdbx_buffer_components",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("buffer_id", String(20), primary_key=True),
    Column("name", String(128), nullable=True),
    Column("volume", String(20), nullable=True),
    Column("conc", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("conc_units", String(20), nullable=True),
    Column("isotopic_labeling", String(128), nullable=True)
)


pdbx_domain = Table("pdbx_domain",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True)
)


pdbx_domain_range = Table("pdbx_domain_range",
    metadata_obj,
    Column("beg_label_alt_id", String(20), primary_key=True),
    Column("beg_label_asym_id", String(20), primary_key=True),
    Column("beg_label_comp_id", String(10), primary_key=True),
    Column("beg_label_seq_id", Integer, primary_key=True),
    Column("beg_auth_asym_id", String(20), nullable=True),
    Column("beg_auth_comp_id", String(20), nullable=True),
    Column("beg_auth_seq_id", String(20), nullable=True),
    Column("domain_id", String(20), primary_key=True),
    Column("end_label_alt_id", String(20), primary_key=True),
    Column("end_label_asym_id", String(20), primary_key=True),
    Column("end_label_comp_id", String(10), primary_key=True),
    Column("end_label_seq_id", Integer, primary_key=True),
    Column("end_auth_asym_id", String(20), nullable=True),
    Column("end_auth_comp_id", String(20), nullable=True),
    Column("end_auth_seq_id", String(20), nullable=True)
)


pdbx_sequence_range = Table("pdbx_sequence_range",
    metadata_obj,
    Column("beg_label_alt_id", String(20), primary_key=True),
    Column("beg_label_asym_id", String(20), primary_key=True),
    Column("beg_label_comp_id", String(10), primary_key=True),
    Column("beg_label_seq_id", Integer, primary_key=True),
    Column("beg_auth_asym_id", String(20), nullable=True),
    Column("beg_auth_comp_id", String(20), nullable=True),
    Column("beg_auth_seq_id", String(20), nullable=True),
    Column("seq_range_id", String(20), primary_key=True),
    Column("end_label_alt_id", String(20), primary_key=True),
    Column("end_label_asym_id", String(20), primary_key=True),
    Column("end_label_comp_id", String(10), primary_key=True),
    Column("end_label_seq_id", Integer, primary_key=True),
    Column("end_auth_asym_id", String(20), nullable=True),
    Column("end_auth_comp_id", String(20), nullable=True),
    Column("end_auth_seq_id", String(20), nullable=True)
)


pdbx_feature_entry = Table("pdbx_feature_entry",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("feature_name", String(255)),
    Column("feature_type", String(255)),
    Column("feature", String(255)),
    Column("feature_identifier", String(255), nullable=True),
    Column("feature_assigned_by", String(255)),
    Column("feature_citation_id", String(20), nullable=True),
    Column("feature_software_id", String(255), nullable=True)
)


pdbx_feature_domain = Table("pdbx_feature_domain",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("domain_id", String(20)),
    Column("feature_name", String(255)),
    Column("feature_type", String(255)),
    Column("feature", String(255)),
    Column("feature_identifier", String(255), nullable=True),
    Column("feature_assigned_by", String(255)),
    Column("feature_citation_id", String(20), nullable=True),
    Column("feature_software_id", String(255), nullable=True)
)


pdbx_feature_sequence_range = Table("pdbx_feature_sequence_range",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("seq_range_id", String(20)),
    Column("feature_name", String(255)),
    Column("feature_type", String(255)),
    Column("feature", String(255)),
    Column("feature_identifier", String(255), nullable=True),
    Column("feature_assigned_by", String(255)),
    Column("feature_citation_id", String(20), nullable=True),
    Column("feature_software_id", String(255), nullable=True)
)


pdbx_feature_assembly = Table("pdbx_feature_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(128)),
    Column("feature_name", String(255)),
    Column("feature_type", String(255)),
    Column("feature", String(255)),
    Column("feature_identifier", String(255), nullable=True),
    Column("feature_assigned_by", String(255)),
    Column("feature_citation_id", String(20), nullable=True),
    Column("feature_software_id", String(255), nullable=True)
)


pdbx_feature_monomer = Table("pdbx_feature_monomer",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("feature_name", String(255)),
    Column("feature_type", String(255)),
    Column("feature", String(255)),
    Column("feature_identifier", String(255), nullable=True),
    Column("feature_assigned_by", String(255)),
    Column("feature_citation_id", String(20), nullable=True),
    Column("feature_software_id", String(255), nullable=True),
    Column("label_alt_id", String(20)),
    Column("label_asym_id", String(20)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True)
)


pdbx_exptl_pd = Table("pdbx_exptl_pd",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("spec_preparation_pH", Float, nullable=True),
    Column("spec_preparation_pH_range", String(128), nullable=True),
    Column("spec_preparation", String(255), nullable=True)
)


pdbx_reflns_twin = Table("pdbx_reflns_twin",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("crystal_id", String(20), primary_key=True),
    Column("domain_id", String(20), nullable=True),
    Column("type", String(128), nullable=True),
    Column("operator", String(128), primary_key=True),
    Column("fraction", Float),
    Column("mean_I2_over_mean_I_square", Float, nullable=True),
    Column("mean_F_square_over_mean_F2", Float, nullable=True)
)


pdbx_struct_info = Table("pdbx_struct_info",
    metadata_obj,
    Column("type", String(128), primary_key=True),
    Column("value", String(255), primary_key=True),
    Column("details", String(255), nullable=True)
)


pdbx_re_refinement = Table("pdbx_re_refinement",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("citation_id", String(20)),
    Column("details", String(20))
)


pdbx_struct_assembly_prop = Table("pdbx_struct_assembly_prop",
    metadata_obj,
    Column("biol_id", String(20), primary_key=True),
    Column("type", String(128), primary_key=True),
    Column("value", String(255)),
    Column("details", String(255), nullable=True)
)


pdbx_struct_ref_seq_feature = Table("pdbx_struct_ref_seq_feature",
    metadata_obj,
    Column("feature_id", Integer, primary_key=True),
    Column("align_id", String(20)),
    Column("type", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("pdb_strand_id", String(20), nullable=True),
    Column("asym_id", String(20), nullable=True),
    Column("beg_auth_seq_id", String(20), nullable=True),
    Column("end_auth_seq_id", String(20), nullable=True),
    Column("beg_seq_num", String(20), nullable=True),
    Column("end_seq_num", String(20), nullable=True),
    Column("beg_auth_mon_id", String(20), nullable=True),
    Column("end_auth_mon_id", String(20), nullable=True),
    Column("beg_pdb_ins_code", String(20), nullable=True),
    Column("end_pdb_ins_code", String(20), nullable=True)
)


pdbx_struct_ref_seq_feature_prop = Table("pdbx_struct_ref_seq_feature_prop",
    metadata_obj,
    Column("feature_id", Integer, primary_key=True),
    Column("property_id", Integer, primary_key=True),
    Column("type", String(255)),
    Column("value", String(255)),
    Column("details", String(255), nullable=True),
    Column("beg_db_mon_id", String(20), nullable=True),
    Column("end_db_mon_id", String(20), nullable=True),
    Column("beg_db_seq_id", Integer, nullable=True),
    Column("end_db_seq_id", Integer, nullable=True)
)


pdbx_struct_chem_comp_diagnostics = Table("pdbx_struct_chem_comp_diagnostics",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("type", String(128), nullable=True),
    Column("pdb_strand_id", String(20), nullable=True),
    Column("asym_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("seq_num", Integer, nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("pdb_ins_code", String(20), nullable=True),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_chem_comp_synonyms = Table("pdbx_chem_comp_synonyms",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("name", String(255)),
    Column("comp_id", String(10), primary_key=True),
    Column("provenance", String(128), nullable=True),
    Column("type", String(128), nullable=True)
)


pdbx_chem_comp_feature = Table("pdbx_chem_comp_feature",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("type", String(128), primary_key=True),
    Column("support", String(255), nullable=True),
    Column("value", String(255), primary_key=True),
    Column("source", String(128), primary_key=True)
)


pdbx_coordinate_model = Table("pdbx_coordinate_model",
    metadata_obj,
    Column("asym_id", String(20), primary_key=True),
    Column("type", String(128))
)


pdbx_struct_chem_comp_feature = Table("pdbx_struct_chem_comp_feature",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("type", String(128), nullable=True),
    Column("pdb_strand_id", String(20), nullable=True),
    Column("asym_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("seq_num", Integer, nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("pdb_ins_code", String(20), nullable=True),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_diffrn_reflns_shell = Table("pdbx_diffrn_reflns_shell",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("d_res_low", Float, primary_key=True),
    Column("d_res_high", Float, primary_key=True),
    Column("percent_possible_obs", Float, nullable=True),
    Column("Rmerge_I_obs", Float, nullable=True),
    Column("Rsym_value", Float, nullable=True),
    Column("chi_squared", Float, nullable=True),
    Column("redundancy", Float, nullable=True),
    Column("rejects", Integer, nullable=True),
    Column("number_obs", Integer, nullable=True)
)


pdbx_bond_distance_limits = Table("pdbx_bond_distance_limits",
    metadata_obj,
    Column("atom_type_1", String(20), primary_key=True),
    Column("atom_type_2", String(20), primary_key=True),
    Column("lower_limit", Float),
    Column("upper_limit", Float)
)


pdbx_soln_scatter = Table("pdbx_soln_scatter",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("type", String(20)),
    Column("source_beamline", String(255), nullable=True),
    Column("source_beamline_instrument", String(255), nullable=True),
    Column("detector_type", String(255), nullable=True),
    Column("detector_specific", String(255), nullable=True),
    Column("source_type", String(255), nullable=True),
    Column("source_class", String(255), nullable=True),
    Column("num_time_frames", Integer, nullable=True),
    Column("sample_pH", Float, nullable=True),
    Column("temperature", Float, nullable=True),
    Column("concentration_range", String(128), nullable=True),
    Column("buffer_name", String(128), nullable=True),
    Column("mean_guiner_radius", Float, nullable=True),
    Column("mean_guiner_radius_esd", Float, nullable=True),
    Column("min_mean_cross_sectional_radii_gyration", Float, nullable=True),
    Column("min_mean_cross_sectional_radii_gyration_esd", Float, nullable=True),
    Column("max_mean_cross_sectional_radii_gyration", Float, nullable=True),
    Column("max_mean_cross_sectional_radii_gyration_esd", Float, nullable=True),
    Column("protein_length", String(128), nullable=True),
    Column("data_reduction_software_list", String(255), nullable=True),
    Column("data_analysis_software_list", String(255), nullable=True)
)


pdbx_soln_scatter_model = Table("pdbx_soln_scatter_model",
    metadata_obj,
    Column("scatter_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("method", String(255), nullable=True),
    Column("software_list", String(255), nullable=True),
    Column("software_author_list", String(255), nullable=True),
    Column("entry_fitting_list", String(255), nullable=True),
    Column("num_conformers_calculated", Integer, nullable=True),
    Column("num_conformers_submitted", Integer, nullable=True),
    Column("representative_conformer", Integer, nullable=True),
    Column("conformer_selection_criteria", String(255), nullable=True)
)


pdbx_chem_comp_descriptor = Table("pdbx_chem_comp_descriptor",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("descriptor", String(255)),
    Column("type", String(50), primary_key=True),
    Column("program", String(128), primary_key=True),
    Column("program_version", String(128), primary_key=True),
    Column("ordinal", Integer, nullable=True)
)


pdbx_chem_comp_identifier = Table("pdbx_chem_comp_identifier",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("identifier", String(255)),
    Column("type", String(128), primary_key=True),
    Column("program", String(128), primary_key=True),
    Column("program_version", String(128), primary_key=True),
    Column("ordinal", Integer, nullable=True)
)


pdbx_chem_comp_import = Table("pdbx_chem_comp_import",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True)
)


pdbx_chem_comp_atom_edit = Table("pdbx_chem_comp_atom_edit",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("comp_id", String(10)),
    Column("edit_op", String(10)),
    Column("atom_id", String(6)),
    Column("edit_atom_id", String(6)),
    Column("edit_atom_value", String(128), nullable=True)
)


pdbx_chem_comp_bond_edit = Table("pdbx_chem_comp_bond_edit",
    metadata_obj,
    Column("ordinal", Integer),
    Column("comp_id", String(10), primary_key=True),
    Column("edit_op", String(10), primary_key=True),
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("edit_bond_value", String(128), nullable=True)
)


pdbx_chem_comp_audit = Table("pdbx_chem_comp_audit",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20), nullable=True),
    Column("processing_site", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("action_type", String(128), primary_key=True)
)


pdbx_validate_close_contact = Table("pdbx_validate_close_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("PDB_ins_code_1", String(20), nullable=True),
    Column("PDB_ins_code_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("symm_as_xyz_1", String(128), nullable=True, default="x,y,z"),
    Column("symm_as_xyz_2", String(128), nullable=True, default="x,y,z"),
    Column("dist", Float)
)


pdbx_validate_symm_contact = Table("pdbx_validate_symm_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("PDB_ins_code_1", String(20), nullable=True),
    Column("PDB_ins_code_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("site_symmetry_1", String(128), default="1555"),
    Column("site_symmetry_2", String(128), default="1555"),
    Column("dist", Float)
)


pdbx_validate_rmsd_bond = Table("pdbx_validate_rmsd_bond",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("PDB_ins_code_1", String(20), nullable=True),
    Column("PDB_ins_code_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("bond_deviation", Float),
    Column("bond_value", Float, nullable=True),
    Column("bond_target_value", Float, nullable=True),
    Column("bond_standard_deviation", Float, nullable=True),
    Column("linker_flag", String(50), nullable=True, default="N")
)


pdbx_validate_rmsd_angle = Table("pdbx_validate_rmsd_angle",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("auth_atom_id_3", String(6)),
    Column("auth_asym_id_3", String(20)),
    Column("auth_comp_id_3", String(20)),
    Column("auth_seq_id_3", String(20)),
    Column("PDB_ins_code_1", String(20), nullable=True),
    Column("PDB_ins_code_2", String(20), nullable=True),
    Column("PDB_ins_code_3", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("label_alt_id_3", String(20), nullable=True),
    Column("angle_deviation", Float),
    Column("angle_value", Float, nullable=True),
    Column("angle_target_value", Float, nullable=True),
    Column("angle_standard_deviation", Float, nullable=True),
    Column("linker_flag", String(50), nullable=True, default="N")
)


pdbx_validate_torsion = Table("pdbx_validate_torsion",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("phi", Float),
    Column("psi", Float)
)


pdbx_validate_peptide_omega = Table("pdbx_validate_peptide_omega",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("PDB_ins_code_1", String(20), nullable=True),
    Column("PDB_ins_code_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("omega", Float)
)


pdbx_validate_chiral = Table("pdbx_validate_chiral",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_atom_id", String(6), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("omega", Float),
    Column("details", String(128), nullable=True)
)


pdbx_validate_planes = Table("pdbx_validate_planes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("rmsd", Float),
    Column("type", String(50))
)


pdbx_validate_planes_atom = Table("pdbx_validate_planes_atom",
    metadata_obj,
    Column("plane_id", Integer),
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("auth_atom_id", String(6)),
    Column("atom_deviation", Float)
)


pdbx_validate_main_chain_plane = Table("pdbx_validate_main_chain_plane",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("improper_torsion_angle", Float)
)


pdbx_struct_conn_angle = Table("pdbx_struct_conn_angle",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("ptnr1_label_alt_id", String(20), nullable=True),
    Column("ptnr1_label_asym_id", String(20)),
    Column("ptnr1_label_atom_id", String(6)),
    Column("ptnr1_label_comp_id", String(10)),
    Column("ptnr1_label_seq_id", Integer, nullable=True),
    Column("ptnr1_auth_asym_id", String(20), nullable=True),
    Column("ptnr1_auth_atom_id", String(6), nullable=True),
    Column("ptnr1_auth_comp_id", String(20), nullable=True),
    Column("ptnr1_auth_seq_id", String(20), nullable=True),
    Column("ptnr1_symmetry", String(10), nullable=True),
    Column("ptnr2_label_alt_id", String(20), nullable=True),
    Column("ptnr2_label_asym_id", String(20)),
    Column("ptnr2_label_atom_id", String(6)),
    Column("ptnr2_label_comp_id", String(10)),
    Column("ptnr2_label_seq_id", Integer, nullable=True),
    Column("ptnr2_auth_asym_id", String(20), nullable=True),
    Column("ptnr2_auth_atom_id", String(6), nullable=True),
    Column("ptnr2_auth_comp_id", String(20), nullable=True),
    Column("ptnr2_auth_seq_id", String(20), nullable=True),
    Column("ptnr2_symmetry", String(10), nullable=True),
    Column("ptnr1_PDB_ins_code", String(20), nullable=True),
    Column("ptnr1_auth_alt_id", String(20), nullable=True),
    Column("ptnr2_PDB_ins_code", String(20), nullable=True),
    Column("ptnr2_auth_alt_id", String(20), nullable=True),
    Column("ptnr3_auth_alt_id", String(20), nullable=True),
    Column("ptnr3_auth_asym_id", String(20), nullable=True),
    Column("ptnr3_auth_atom_id", String(6), nullable=True),
    Column("ptnr3_auth_comp_id", String(20), nullable=True),
    Column("ptnr3_PDB_ins_code", String(20), nullable=True),
    Column("ptnr3_auth_seq_id", String(20), nullable=True),
    Column("ptnr3_label_alt_id", String(20), nullable=True),
    Column("ptnr3_label_asym_id", String(20), nullable=True),
    Column("ptnr3_label_atom_id", String(6), nullable=True),
    Column("ptnr3_label_comp_id", String(10), nullable=True),
    Column("ptnr3_label_seq_id", Integer, nullable=True),
    Column("ptnr3_symmetry", String(10), nullable=True),
    Column("value", Float, nullable=True),
    Column("value_esd", Float, nullable=True)
)


pdbx_unobs_or_zero_occ_residues = Table("pdbx_unobs_or_zero_occ_residues",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("polymer_flag", String(10)),
    Column("occupancy_flag", Integer),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(10)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True)
)


pdbx_unobs_or_zero_occ_atoms = Table("pdbx_unobs_or_zero_occ_atoms",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("polymer_flag", String(10)),
    Column("occupancy_flag", Integer),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_atom_id", String(6)),
    Column("auth_comp_id", String(10)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_atom_id", String(6), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True)
)


pdbx_entry_details = Table("pdbx_entry_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("nonpolymer_details", String(255), nullable=True),
    Column("sequence_details", String(255), nullable=True),
    Column("compound_details", String(255), nullable=True),
    Column("source_details", String(255), nullable=True),
    Column("has_ligand_of_interest", String(10), nullable=True),
    Column("has_protein_modification", String(20), nullable=True)
)


pdbx_struct_mod_residue = Table("pdbx_struct_mod_residue",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer, nullable=True),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("parent_comp_id", String(20), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_struct_ref_seq_insertion = Table("pdbx_struct_ref_seq_insertion",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("comp_id", String(10)),
    Column("asym_id", String(20)),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_seq_id", String(20)),
    Column("seq_id", Integer),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("db_code", String(128)),
    Column("db_name", String(128))
)


pdbx_struct_ref_seq_deletion = Table("pdbx_struct_ref_seq_deletion",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("asym_id", String(20)),
    Column("comp_id", String(10)),
    Column("db_seq_id", Integer),
    Column("db_code", String(128)),
    Column("db_name", String(128))
)


pdbx_remediation_atom_site_mapping = Table("pdbx_remediation_atom_site_mapping",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("group_PDB", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_asym_id", String(20)),
    Column("label_atom_id", String(6)),
    Column("label_comp_id", String(10)),
    Column("label_seq_id", Integer),
    Column("pdbx_align", Integer, nullable=True),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("pre_auth_asym_id", String(20), nullable=True),
    Column("pre_auth_atom_id", String(6), nullable=True),
    Column("pre_auth_comp_id", String(20), nullable=True),
    Column("pre_auth_seq_id", String(20), nullable=True),
    Column("pre_PDB_ins_code", String(20), nullable=True),
    Column("pre_group_PDB", String(20), nullable=True),
    Column("pre_auth_alt_id", String(20), nullable=True),
    Column("pre_pdbx_align", Integer, nullable=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_atom_id", String(6), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("auth_alt_id", String(20), nullable=True),
    Column("occupancy", Float, nullable=True),
    Column("pre_occupancy", Float, nullable=True)
)


pdbx_validate_polymer_linkage = Table("pdbx_validate_polymer_linkage",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("PDB_ins_code_1", String(20), nullable=True),
    Column("PDB_ins_code_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("dist", Float)
)


pdbx_helical_symmetry = Table("pdbx_helical_symmetry",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("number_of_operations", Integer),
    Column("rotation_per_n_subunits", Float),
    Column("rise_per_n_subunits", Float),
    Column("n_subunits_divisor", Integer),
    Column("dyad_axis", String(20)),
    Column("circular_symmetry", Integer)
)


pdbx_point_symmetry = Table("pdbx_point_symmetry",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("Schoenflies_symbol", String(20)),
    Column("circular_symmetry", Integer, nullable=True),
    Column("H-M_notation", String(20), nullable=True)
)


pdbx_struct_entity_inst = Table("pdbx_struct_entity_inst",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("entity_id", String(20), nullable=True),
    Column("id", String(20), primary_key=True)
)


pdbx_struct_oper_list = Table("pdbx_struct_oper_list",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(128)),
    Column("name", String(128), nullable=True),
    Column("symmetry_operation", String(128), nullable=True),
    Column("matrix[1][1]", Float, nullable=True),
    Column("matrix[1][2]", Float, nullable=True),
    Column("matrix[1][3]", Float, nullable=True),
    Column("matrix[2][1]", Float, nullable=True),
    Column("matrix[2][2]", Float, nullable=True),
    Column("matrix[2][3]", Float, nullable=True),
    Column("matrix[3][1]", Float, nullable=True),
    Column("matrix[3][2]", Float, nullable=True),
    Column("matrix[3][3]", Float, nullable=True),
    Column("vector[1]", Float, nullable=True),
    Column("vector[2]", Float, nullable=True),
    Column("vector[3]", Float, nullable=True),
    Column("full_matrix", String(255), nullable=True)
)


pdbx_struct_assembly = Table("pdbx_struct_assembly",
    metadata_obj,
    Column("method_details", String(255), nullable=True),
    Column("oligomeric_details", String(128), nullable=True),
    Column("oligomeric_count", Integer, nullable=True),
    Column("details", String(255))
)


pdbx_struct_assembly_gen = Table("pdbx_struct_assembly_gen",
    metadata_obj,
    Column("entity_inst_id", String(20), nullable=True),
    Column("asym_id_list", String(255), primary_key=True),
    Column("auth_asym_id_list", String(128), nullable=True),
    Column("assembly_id", String(128), primary_key=True),
    Column("oper_expression", String(511), primary_key=True)
)


pdbx_struct_asym_gen = Table("pdbx_struct_asym_gen",
    metadata_obj,
    Column("entity_inst_id", String(20), primary_key=True),
    Column("asym_id", String(20), nullable=True),
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
    Column("name", String(128), nullable=True),
    Column("matrix[1][1]", Float, nullable=True),
    Column("matrix[1][2]", Float, nullable=True),
    Column("matrix[1][3]", Float, nullable=True),
    Column("matrix[2][1]", Float, nullable=True),
    Column("matrix[2][2]", Float, nullable=True),
    Column("matrix[2][3]", Float, nullable=True),
    Column("matrix[3][1]", Float, nullable=True),
    Column("matrix[3][2]", Float, nullable=True),
    Column("matrix[3][3]", Float, nullable=True),
    Column("vector[1]", Float, nullable=True),
    Column("vector[2]", Float, nullable=True),
    Column("vector[3]", Float, nullable=True)
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
    Column("name", String(255), nullable=True),
    Column("release_status", String(50), nullable=True),
    Column("replaces", String(50), nullable=True),
    Column("replaced_by", String(50), nullable=True)
)


pdbx_reference_molecule_list = Table("pdbx_reference_molecule_list",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("family_prd_id", String(10), primary_key=True)
)


pdbx_reference_molecule = Table("pdbx_reference_molecule",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("formula_weight", Float, nullable=True),
    Column("formula", String(255), nullable=True),
    Column("type", String(50), nullable=True),
    Column("type_evidence_code", String(255), nullable=True),
    Column("class", String(50), nullable=True),
    Column("class_evidence_code", String(255), nullable=True),
    Column("name", String(255), nullable=True),
    Column("represent_as", String(50), nullable=True),
    Column("chem_comp_id", String(10), nullable=True),
    Column("compound_details", String(255), nullable=True),
    Column("description", String(255), nullable=True),
    Column("representative_PDB_id_code", String(10), nullable=True),
    Column("release_status", String(50), nullable=True),
    Column("replaces", String(50), nullable=True),
    Column("replaced_by", String(50), nullable=True)
)


pdbx_reference_entity_list = Table("pdbx_reference_entity_list",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("type", String(50), nullable=True),
    Column("details", String(255), nullable=True),
    Column("component_id", Integer, primary_key=True)
)


pdbx_reference_entity_nonpoly = Table("pdbx_reference_entity_nonpoly",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("name", String(255), nullable=True),
    Column("chem_comp_id", String(10), nullable=True)
)


pdbx_reference_entity_link = Table("pdbx_reference_entity_link",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("ref_entity_id_1", String(10)),
    Column("ref_entity_id_2", String(10)),
    Column("entity_seq_num_1", Integer, nullable=True),
    Column("entity_seq_num_2", Integer, nullable=True),
    Column("comp_id_1", String(20)),
    Column("comp_id_2", String(20)),
    Column("atom_id_1", String(6)),
    Column("atom_id_2", String(20)),
    Column("value_order", String(10), nullable=True, default="sing"),
    Column("component_1", Integer),
    Column("component_2", Integer),
    Column("nonpoly_res_num_1", String(20), nullable=True),
    Column("nonpoly_res_num_2", String(20), nullable=True),
    Column("link_class", String(20), nullable=True)
)


pdbx_reference_entity_poly_link = Table("pdbx_reference_entity_poly_link",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("component_id", Integer, primary_key=True),
    Column("entity_seq_num_1", Integer, nullable=True),
    Column("entity_seq_num_2", Integer, nullable=True),
    Column("comp_id_1", String(20)),
    Column("comp_id_2", String(20)),
    Column("atom_id_1", String(6)),
    Column("atom_id_2", String(20)),
    Column("insert_code_1", String(20), nullable=True),
    Column("insert_code_2", String(20), nullable=True),
    Column("value_order", String(10), nullable=True, default="sing")
)


pdbx_reference_entity_poly = Table("pdbx_reference_entity_poly",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("type", String(128), nullable=True),
    Column("db_code", String(255), nullable=True),
    Column("db_name", String(255), nullable=True)
)


pdbx_reference_entity_poly_seq = Table("pdbx_reference_entity_poly_seq",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("mon_id", String(20), primary_key=True),
    Column("parent_mon_id", String(20), nullable=True),
    Column("num", Integer, primary_key=True),
    Column("observed", String(10), nullable=True, default="Y"),
    Column("hetero", String(10), primary_key=True, default="N")
)


pdbx_reference_entity_sequence = Table("pdbx_reference_entity_sequence",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("type", String(128)),
    Column("NRP_flag", String(20)),
    Column("one_letter_codes", String(128), nullable=True)
)


pdbx_reference_entity_src_nat = Table("pdbx_reference_entity_src_nat",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("ref_entity_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("organism_scientific", String(255), nullable=True),
    Column("strain", String(255), nullable=True),
    Column("taxid", String(255), nullable=True),
    Column("atcc", String(255), nullable=True),
    Column("db_code", String(255), nullable=True),
    Column("db_name", String(255), nullable=True),
    Column("source", String(255), nullable=True),
    Column("source_id", String(255), nullable=True)
)


pdbx_reference_molecule_details = Table("pdbx_reference_molecule_details",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10), nullable=True),
    Column("ordinal", Integer, primary_key=True),
    Column("source", String(255), nullable=True),
    Column("source_id", String(255), nullable=True),
    Column("text", String(255))
)


pdbx_reference_molecule_synonyms = Table("pdbx_reference_molecule_synonyms",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("name", String(255)),
    Column("source", String(255)),
    Column("chem_comp_id", String(10), nullable=True)
)


pdbx_reference_entity_subcomponents = Table("pdbx_reference_entity_subcomponents",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("seq", String(255), primary_key=True),
    Column("chem_comp_id", String(10), nullable=True)
)


pdbx_reference_molecule_annotation = Table("pdbx_reference_molecule_annotation",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10), nullable=True),
    Column("ordinal", Integer, primary_key=True),
    Column("text", String(255)),
    Column("type", String(128)),
    Column("support", String(255), nullable=True),
    Column("source", String(255)),
    Column("chem_comp_id", String(10), nullable=True)
)


pdbx_reference_molecule_features = Table("pdbx_reference_molecule_features",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("prd_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("source_ordinal", Integer, nullable=True),
    Column("type", String(128)),
    Column("value", String(255)),
    Column("source", String(128)),
    Column("chem_comp_id", String(10), nullable=True)
)


pdbx_reference_molecule_related_structures = Table("pdbx_reference_molecule_related_structures",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("db_name", String(255), nullable=True),
    Column("db_code", String(255), nullable=True),
    Column("db_accession", String(255), nullable=True),
    Column("name", String(255), nullable=True),
    Column("formula", String(255), nullable=True),
    Column("citation_id", String(20), nullable=True)
)


pdbx_struct_group_list = Table("pdbx_struct_group_list",
    metadata_obj,
    Column("struct_group_id", String(10), primary_key=True),
    Column("name", String(128)),
    Column("type", String(128)),
    Column("group_enumeration_type", String(25)),
    Column("description", String(255)),
    Column("selection", String(128), nullable=True),
    Column("selection_details", String(255), nullable=True)
)


pdbx_struct_group_components = Table("pdbx_struct_group_components",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("struct_group_id", String(10)),
    Column("PDB_model_num", Integer, nullable=True),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("label_alt_id", String(20), nullable=True)
)


pdbx_struct_group_component_range = Table("pdbx_struct_group_component_range",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("struct_group_id", String(10)),
    Column("PDB_model_num", Integer, nullable=True),
    Column("beg_auth_asym_id", String(20)),
    Column("beg_auth_comp_id", String(20)),
    Column("beg_auth_seq_id", String(20)),
    Column("beg_PDB_ins_code", String(20), nullable=True),
    Column("beg_label_asym_id", String(20), nullable=True),
    Column("beg_label_comp_id", String(10), nullable=True),
    Column("beg_label_seq_id", Integer, nullable=True),
    Column("beg_label_alt_id", String(20), nullable=True),
    Column("end_auth_asym_id", String(20)),
    Column("end_auth_comp_id", String(20)),
    Column("end_auth_seq_id", String(20)),
    Column("end_PDB_ins_code", String(20), nullable=True),
    Column("end_label_asym_id", String(20), nullable=True),
    Column("end_label_comp_id", String(10), nullable=True),
    Column("end_label_seq_id", Integer, nullable=True),
    Column("end_label_alt_id", String(20), nullable=True)
)


pdbx_prd_audit = Table("pdbx_prd_audit",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20), nullable=True),
    Column("processing_site", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("action_type", String(128), primary_key=True)
)


pdbx_family_prd_audit = Table("pdbx_family_prd_audit",
    metadata_obj,
    Column("family_prd_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20), nullable=True),
    Column("processing_site", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("action_type", String(128), primary_key=True)
)


pdbx_molecule = Table("pdbx_molecule",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("instance_id", Integer, primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("linked_entity_id", String(20), nullable=True)
)


pdbx_molecule_features = Table("pdbx_molecule_features",
    metadata_obj,
    Column("prd_id", String(10), primary_key=True),
    Column("class", String(50), nullable=True),
    Column("type", String(50), nullable=True),
    Column("name", String(255), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_family_group_index = Table("pdbx_family_group_index",
    metadata_obj,
    Column("id", String(10), primary_key=True),
    Column("family_prd_id", String(10), primary_key=True)
)


pdbx_distant_solvent_atoms = Table("pdbx_distant_solvent_atoms",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_atom_id", String(6)),
    Column("auth_comp_id", String(10)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_atom_id", String(6), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("neighbor_macromolecule_distance", Float, nullable=True),
    Column("neighbor_ligand_distance", Float, nullable=True)
)


pdbx_struct_special_symmetry = Table("pdbx_struct_special_symmetry",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("PDB_model_num", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(10)),
    Column("auth_seq_id", String(20)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True)
)


pdbx_reference_publication_list = Table("pdbx_reference_publication_list",
    metadata_obj,
    Column("publication_abbrev", String(128), primary_key=True),
    Column("ASTM_code_type", String(128), nullable=True),
    Column("ASTM_code_value", String(128), nullable=True),
    Column("ISSN_code_type", String(128), nullable=True),
    Column("ISSN_code_value", String(128), nullable=True),
    Column("country", String(128), nullable=True),
    Column("start_year", String(128), nullable=True),
    Column("end_year", String(128), nullable=True)
)


pdbx_nmr_assigned_chem_shift_list = Table("pdbx_nmr_assigned_chem_shift_list",
    metadata_obj,
    Column("chem_shift_13C_err", Float, nullable=True),
    Column("chem_shift_15N_err", Float, nullable=True),
    Column("chem_shift_19F_err", Float, nullable=True),
    Column("chem_shift_1H_err", Float, nullable=True),
    Column("chem_shift_2H_err", Float, nullable=True),
    Column("chem_shift_31P_err", Float, nullable=True),
    Column("chem_shift_reference_id", Integer),
    Column("conditions_id", Integer),
    Column("data_file_name", String(128)),
    Column("details", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("error_derivation_method", String(255), nullable=True),
    Column("label", String(128), nullable=True),
    Column("conditions_label", String(128), nullable=True)
)


pdbx_nmr_chem_shift_experiment = Table("pdbx_nmr_chem_shift_experiment",
    metadata_obj,
    Column("assigned_chem_shift_list_id", Integer, primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("experiment_id", Integer, primary_key=True),
    Column("experiment_name", String(128), nullable=True),
    Column("sample_state", String(128), nullable=True),
    Column("solution_id", Integer, nullable=True)
)


pdbx_nmr_chem_shift_ref = Table("pdbx_nmr_chem_shift_ref",
    metadata_obj,
    Column("atom_group", String(128)),
    Column("atom_isotope_number", Integer, primary_key=True),
    Column("atom_type", String(20), primary_key=True),
    Column("chem_shift_reference_id", Integer, primary_key=True),
    Column("chem_shift_units", String(128)),
    Column("chem_shift_val", Float),
    Column("correction_val", Float, nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("external_ref_axis", String(128), nullable=True),
    Column("external_ref_loc", String(128), nullable=True),
    Column("external_ref_sample_geometry", String(128), nullable=True),
    Column("indirect_shift_ratio", Float, nullable=True, default=1.0),
    Column("mol_common_name", String(128), primary_key=True),
    Column("rank", String(20), nullable=True),
    Column("ref_correction_type", String(128), nullable=True),
    Column("ref_method", String(128), nullable=True),
    Column("ref_type", String(128), nullable=True),
    Column("solvent", String(128), nullable=True)
)


pdbx_nmr_chem_shift_reference = Table("pdbx_nmr_chem_shift_reference",
    metadata_obj,
    Column("carbon_shifts_flag", String(128), nullable=True),
    Column("details", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("id", Integer, primary_key=True),
    Column("label", String(128), default="chemical_shift_reference_1"),
    Column("nitrogen_shifts_flag", String(128), nullable=True),
    Column("other_shifts_flag", String(128), nullable=True, default="no"),
    Column("phosphorus_shifts_flag", String(128), nullable=True, default="no"),
    Column("proton_shifts_flag", String(128), nullable=True)
)


pdbx_nmr_chem_shift_software = Table("pdbx_nmr_chem_shift_software",
    metadata_obj,
    Column("assigned_chem_shift_list_id", Integer, primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("software_id", Integer, primary_key=True),
    Column("software_label", String(20), nullable=True)
)


pdbx_nmr_constraint_file = Table("pdbx_nmr_constraint_file",
    metadata_obj,
    Column("constraint_filename", String(128), primary_key=True),
    Column("constraint_number", Integer, nullable=True),
    Column("constraint_subtype", String(128), primary_key=True),
    Column("constraint_type", String(128), primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("id", Integer, nullable=True),
    Column("software_name", String(128), nullable=True),
    Column("software_ordinal", Integer, nullable=True)
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
    Column("atom_isotope_number", Integer),
    Column("spectral_region", String(20), primary_key=True),
    Column("magnetization_linkage_id", Integer, nullable=True),
    Column("sweep_width", Float, nullable=True),
    Column("encoding_code", String(128), nullable=True),
    Column("encoded_source_dimension_id", Integer, nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("spectral_peak_list_id", Integer, primary_key=True),
    Column("sweep_width_units", String(20)),
    Column("center_frequency_offset", Float),
    Column("under_sampling_type", String(128))
)


pdbx_nmr_spectral_peak_list = Table("pdbx_nmr_spectral_peak_list",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("data_file_name", String(128), nullable=True),
    Column("solution_id", Integer),
    Column("conditions_id", Integer),
    Column("experiment_id", Integer),
    Column("number_of_spectral_dimensions", Integer),
    Column("details", String(255), nullable=True),
    Column("text_data_format", String(128), nullable=True),
    Column("label", String(128), nullable=True),
    Column("conditions_label", String(128), nullable=True)
)


pdbx_nmr_spectral_peak_software = Table("pdbx_nmr_spectral_peak_software",
    metadata_obj,
    Column("software_id", Integer, primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("spectral_peak_list_id", Integer, primary_key=True)
)


pdbx_nmr_systematic_chem_shift_offset = Table("pdbx_nmr_systematic_chem_shift_offset",
    metadata_obj,
    Column("type", String(128), nullable=True),
    Column("atom_type", String(128), nullable=True),
    Column("atom_isotope_number", Integer, nullable=True),
    Column("val", Float, nullable=True),
    Column("val_err", Float, nullable=True),
    Column("entry_id", String(20)),
    Column("assigned_chem_shift_list_id", Integer),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_nmr_upload = Table("pdbx_nmr_upload",
    metadata_obj,
    Column("data_file_id", Integer, primary_key=True),
    Column("data_file_name", String(128)),
    Column("data_file_category", String(128)),
    Column("data_file_syntax", String(128), nullable=True),
    Column("entry_id", String(20), primary_key=True)
)


pdbx_chem_comp_subcomponent_struct_conn = Table("pdbx_chem_comp_subcomponent_struct_conn",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("type", String(10)),
    Column("entity_id_1", Integer),
    Column("entity_id_2", Integer),
    Column("atom_id_1", String(6)),
    Column("atom_id_2", String(6)),
    Column("comp_id_1", String(10)),
    Column("comp_id_2", String(10)),
    Column("seq_id_1", Integer),
    Column("seq_id_2", Integer)
)


pdbx_chem_comp_subcomponent_entity_list = Table("pdbx_chem_comp_subcomponent_entity_list",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("parent_comp_id", String(10)),
    Column("type", String(50)),
    Column("class", String(10))
)


entity_src_nat = Table("entity_src_nat",
    metadata_obj,
    Column("common_name", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("entity_id", String(20), primary_key=True),
    Column("genus", String(255), nullable=True),
    Column("species", String(255), nullable=True),
    Column("strain", String(255), nullable=True),
    Column("tissue", String(255), nullable=True),
    Column("tissue_fraction", String(255), nullable=True),
    Column("pdbx_organism_scientific", String(255), nullable=True),
    Column("pdbx_secretion", String(255), nullable=True),
    Column("pdbx_fragment", String(255), nullable=True),
    Column("pdbx_variant", String(255), nullable=True),
    Column("pdbx_cell_line", String(255), nullable=True),
    Column("pdbx_atcc", String(255), nullable=True),
    Column("pdbx_cellular_location", String(255), nullable=True),
    Column("pdbx_organ", String(255), nullable=True),
    Column("pdbx_organelle", String(255), nullable=True),
    Column("pdbx_cell", String(255), nullable=True),
    Column("pdbx_plasmid_name", String(255), nullable=True),
    Column("pdbx_plasmid_details", String(255), nullable=True),
    Column("pdbx_ncbi_taxonomy_id", String(128), nullable=True),
    Column("pdbx_src_id", Integer, primary_key=True, default=1),
    Column("pdbx_alt_source_flag", String(20), nullable=True, default="sample"),
    Column("pdbx_beg_seq_num", Integer, nullable=True),
    Column("pdbx_end_seq_num", Integer, nullable=True),
    Column("pdbx_culture_collection", String(255), nullable=True)
)


entity_src_gen = Table("entity_src_gen",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("gene_src_common_name", String(255), nullable=True),
    Column("gene_src_details", String(255), nullable=True),
    Column("gene_src_genus", String(255), nullable=True),
    Column("gene_src_species", String(255), nullable=True),
    Column("gene_src_strain", String(255), nullable=True),
    Column("gene_src_tissue", String(255), nullable=True),
    Column("gene_src_tissue_fraction", String(255), nullable=True),
    Column("host_org_genus", String(255), nullable=True),
    Column("host_org_species", String(255), nullable=True),
    Column("pdbx_gene_src_fragment", String(255), nullable=True),
    Column("pdbx_gene_src_gene", String(255), nullable=True),
    Column("pdbx_gene_src_scientific_name", String(255), nullable=True),
    Column("pdbx_gene_src_variant", String(255), nullable=True),
    Column("pdbx_gene_src_cell_line", String(255), nullable=True),
    Column("pdbx_gene_src_atcc", String(255), nullable=True),
    Column("pdbx_gene_src_organ", String(255), nullable=True),
    Column("pdbx_gene_src_organelle", String(255), nullable=True),
    Column("pdbx_gene_src_plasmid", String(255), nullable=True),
    Column("pdbx_gene_src_plasmid_name", String(255), nullable=True),
    Column("pdbx_gene_src_cell", String(255), nullable=True),
    Column("pdbx_gene_src_cellular_location", String(255), nullable=True),
    Column("pdbx_host_org_gene", String(255), nullable=True),
    Column("pdbx_host_org_organ", String(255), nullable=True),
    Column("pdbx_host_org_organelle", String(255), nullable=True),
    Column("pdbx_host_org_cellular_location", String(255), nullable=True),
    Column("pdbx_host_org_strain", String(255), nullable=True),
    Column("pdbx_host_org_tissue_fraction", String(255), nullable=True),
    Column("pdbx_description", String(255), nullable=True),
    Column("host_org_common_name", String(255), nullable=True),
    Column("host_org_details", String(255), nullable=True),
    Column("host_org_strain", String(255), nullable=True),
    Column("plasmid_details", String(255), nullable=True),
    Column("plasmid_name", String(255), nullable=True),
    Column("pdbx_host_org_variant", String(255), nullable=True),
    Column("pdbx_host_org_cell_line", String(255), nullable=True),
    Column("pdbx_host_org_atcc", String(255), nullable=True),
    Column("pdbx_host_org_culture_collection", String(255), nullable=True),
    Column("pdbx_host_org_cell", String(255), nullable=True),
    Column("pdbx_host_org_scientific_name", String(255), nullable=True),
    Column("pdbx_host_org_tissue", String(255), nullable=True),
    Column("pdbx_host_org_vector", String(255), nullable=True),
    Column("pdbx_host_org_vector_type", String(255), nullable=True),
    Column("expression_system_id", String(50), nullable=True),
    Column("gene_src_dev_stage", String(255), nullable=True),
    Column("start_construct_id", String(20), nullable=True),
    Column("pdbx_gene_src_ncbi_taxonomy_id", String(128), nullable=True),
    Column("pdbx_host_org_ncbi_taxonomy_id", String(128), nullable=True),
    Column("pdbx_src_id", Integer, primary_key=True, default=1),
    Column("pdbx_alt_source_flag", String(20), nullable=True, default="sample"),
    Column("pdbx_seq_type", String(128), nullable=True),
    Column("pdbx_beg_seq_num", Integer, nullable=True),
    Column("pdbx_end_seq_num", Integer, nullable=True),
    Column("pdbx_gene_src_culture_collection", String(255), nullable=True)
)


pdbx_entity_src_syn = Table("pdbx_entity_src_syn",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("organism_scientific", String(255), nullable=True),
    Column("organism_common_name", String(255), nullable=True),
    Column("strain", String(255), nullable=True),
    Column("ncbi_taxonomy_id", String(128), nullable=True),
    Column("entity_id", String(20), primary_key=True),
    Column("pdbx_src_id", Integer, primary_key=True, default=1),
    Column("pdbx_alt_source_flag", String(20), nullable=True, default="sample"),
    Column("pdbx_beg_seq_num", Integer, nullable=True),
    Column("pdbx_end_seq_num", Integer, nullable=True)
)


pdbx_entity_poly_comp_link_list = Table("pdbx_entity_poly_comp_link_list",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("details", String(255), nullable=True),
    Column("entity_id", String(20)),
    Column("entity_comp_num_1", Integer),
    Column("entity_comp_num_2", Integer),
    Column("comp_id_1", String(10)),
    Column("comp_id_2", String(10)),
    Column("atom_id_1", String(6)),
    Column("leaving_atom_id_1", String(6)),
    Column("atom_stereo_config_1", String(10), nullable=True, default="N"),
    Column("atom_id_2", String(6)),
    Column("leaving_atom_id_2", String(6)),
    Column("atom_stereo_config_2", String(10), nullable=True, default="N"),
    Column("value_order", String(10), nullable=True, default="sing")
)


pdbx_linked_entity = Table("pdbx_linked_entity",
    metadata_obj,
    Column("linked_entity_id", String(10), primary_key=True),
    Column("type", String(50), nullable=True),
    Column("class", String(255), nullable=True),
    Column("name", String(255), nullable=True),
    Column("description", String(255), nullable=True),
    Column("prd_id", String(10), nullable=True)
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
    Column("details", String(255), nullable=True)
)


pdbx_linked_entity_link_list = Table("pdbx_linked_entity_link_list",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("linked_entity_id", String(10), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("entity_id_1", String(20)),
    Column("entity_id_2", String(20)),
    Column("entity_seq_num_1", Integer, nullable=True),
    Column("entity_seq_num_2", Integer, nullable=True),
    Column("comp_id_1", String(20)),
    Column("comp_id_2", String(20)),
    Column("atom_id_1", String(6)),
    Column("atom_id_2", String(6)),
    Column("value_order", String(10), nullable=True, default="sing"),
    Column("component_1", Integer),
    Column("component_2", Integer),
    Column("link_class", String(20), nullable=True)
)


pdbx_entity_branch_descriptor = Table("pdbx_entity_branch_descriptor",
    metadata_obj,
    Column("entity_id", String(20)),
    Column("descriptor", String(255)),
    Column("type", String(50)),
    Column("program", String(128), nullable=True),
    Column("program_version", String(128), nullable=True),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_reference_linked_entity = Table("pdbx_reference_linked_entity",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("class", String(255), nullable=True),
    Column("name", String(255), nullable=True),
    Column("taxonomy_id", String(255), nullable=True),
    Column("taxonomy_class", String(255), nullable=True),
    Column("link_to_entity_type", String(128), nullable=True),
    Column("link_to_comp_id", String(10), nullable=True),
    Column("link_from_entity_type", String(128), nullable=True)
)


pdbx_reference_linked_entity_comp_list = Table("pdbx_reference_linked_entity_comp_list",
    metadata_obj,
    Column("linked_entity_id", Integer, primary_key=True),
    Column("list_id", Integer, primary_key=True),
    Column("name", String(255), nullable=True),
    Column("comp_id", String(10), nullable=True)
)


pdbx_reference_linked_entity_comp_link = Table("pdbx_reference_linked_entity_comp_link",
    metadata_obj,
    Column("linked_entity_id", Integer, primary_key=True),
    Column("link_id", Integer, primary_key=True),
    Column("list_id_1", Integer),
    Column("list_id_2", Integer),
    Column("details", String(255), nullable=True),
    Column("comp_id_1", String(20)),
    Column("comp_id_2", String(20)),
    Column("atom_id_1", String(6)),
    Column("atom_id_2", String(6)),
    Column("leaving_atom_id_1", String(6)),
    Column("atom_stereo_config_1", String(10), nullable=True, default="N"),
    Column("leaving_atom_id_2", String(6)),
    Column("atom_stereo_config_2", String(10), nullable=True, default="N"),
    Column("value_order", String(10), nullable=True, default="sing")
)


pdbx_reference_linked_entity_link = Table("pdbx_reference_linked_entity_link",
    metadata_obj,
    Column("linked_entity_id", Integer, primary_key=True),
    Column("link_id", Integer, primary_key=True),
    Column("from_list_id", Integer),
    Column("details", String(255), nullable=True),
    Column("to_comp_id", String(20)),
    Column("from_comp_id", String(20)),
    Column("to_atom_id", String(6)),
    Column("from_atom_id", String(6)),
    Column("from_leaving_atom_id", String(6)),
    Column("from_atom_stereo_config", String(10), nullable=True, default="N"),
    Column("value_order", String(10), nullable=True, default="sing")
)


pdbx_related_exp_data_set = Table("pdbx_related_exp_data_set",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("data_reference", String(80)),
    Column("metadata_reference", String(80), nullable=True),
    Column("data_set_type", String(128)),
    Column("details", String(255), nullable=True)
)


pdbx_database_status_history = Table("pdbx_database_status_history",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("ordinal", String(20), primary_key=True),
    Column("date_begin", Date),
    Column("date_end", Date, nullable=True),
    Column("status_code", String(20)),
    Column("details", String(255), nullable=True)
)


em_assembly = Table("em_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("name", String(255), nullable=True),
    Column("aggregation_state", String(128), nullable=True),
    Column("composition", String(255), nullable=True),
    Column("num_components", Integer, nullable=True),
    Column("mol_wt_exp", Float, nullable=True),
    Column("mol_wt_theo", Float, nullable=True),
    Column("mol_wt_method", String(255), nullable=True),
    Column("details", String(255), nullable=True)
)


em_entity_assembly = Table("em_entity_assembly",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(20), nullable=True),
    Column("parent_id", Integer),
    Column("source", String(128), nullable=True),
    Column("type", String(128), nullable=True),
    Column("name", String(255)),
    Column("details", String(255), nullable=True),
    Column("go_id", String(128), nullable=True),
    Column("ipr_id", String(128), nullable=True),
    Column("synonym", String(128), nullable=True),
    Column("number_of_copies", Integer, nullable=True),
    Column("oligomeric_details", String(255), nullable=True),
    Column("entity_id_list", String(128), nullable=True),
    Column("ebi_organism_scientific", String(128), nullable=True),
    Column("ebi_organism_common", String(255), nullable=True),
    Column("ebi_strain", String(255), nullable=True),
    Column("ebi_tissue", String(255), nullable=True),
    Column("ebi_cell", String(255), nullable=True),
    Column("ebi_organelle", String(255), nullable=True),
    Column("ebi_cellular_location", String(255), nullable=True),
    Column("ebi_engineered", String(128), nullable=True),
    Column("ebi_expression_system", String(128), nullable=True),
    Column("ebi_expression_system_plasmid", String(128), nullable=True),
    Column("mutant_flag", String(128), nullable=True),
    Column("chimera", String(128), nullable=True)
)


em_virus_entity = Table("em_virus_entity",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("virus_host_category", String(128), nullable=True),
    Column("virus_host_species", String(128), nullable=True),
    Column("virus_host_growth_cell", String(128), nullable=True),
    Column("virus_type", String(128), nullable=True),
    Column("virus_isolate", String(128), nullable=True),
    Column("ictvdb_id", String(128), nullable=True),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("enveloped", String(20), nullable=True),
    Column("empty", String(20), nullable=True),
    Column("details", String(255), nullable=True)
)


em_sample_preparation = Table("em_sample_preparation",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ph", Float, nullable=True),
    Column("buffer_id", String(20), nullable=True),
    Column("sample_concentration", Float, nullable=True),
    Column("2d_crystal_grow_id", String(20), nullable=True),
    Column("support_id", String(20), nullable=True),
    Column("entity_assembly_id", String(20), nullable=True),
    Column("details", String(255), nullable=True)
)


em_sample_support = Table("em_sample_support",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("film_material", String(128), nullable=True),
    Column("method", String(255), nullable=True),
    Column("grid_material", String(128), nullable=True),
    Column("grid_mesh_size", Integer, nullable=True),
    Column("grid_type", String(128), nullable=True),
    Column("pretreatment", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("specimen_id", String(20), primary_key=True),
    Column("citation_id", String(20), nullable=True)
)


em_buffer = Table("em_buffer",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("specimen_id", String(20), primary_key=True),
    Column("name", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("pH", Float, nullable=True)
)


em_vitrification = Table("em_vitrification",
    metadata_obj,
    Column("entry_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("sample_preparation_id", String(20), nullable=True),
    Column("specimen_id", String(20), primary_key=True),
    Column("cryogen_name", String(128), nullable=True),
    Column("humidity", Float, nullable=True),
    Column("temp", Float, nullable=True),
    Column("chamber_temperature", Float, nullable=True),
    Column("instrument", String(128), nullable=True),
    Column("method", String(255), nullable=True),
    Column("time_resolved_state", String(255), nullable=True),
    Column("citation_id", String(20), nullable=True),
    Column("details", String(255), nullable=True)
)


em_imaging = Table("em_imaging",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("astigmatism", String(255), nullable=True),
    Column("electron_beam_tilt_params", String(255), nullable=True),
    Column("residual_tilt", Float, nullable=True),
    Column("sample_support_id", String(20), nullable=True),
    Column("detector_id", String(20), nullable=True),
    Column("scans_id", String(20), nullable=True),
    Column("microscope_id", String(20), nullable=True),
    Column("microscope_model", String(128)),
    Column("specimen_holder_type", String(255), nullable=True),
    Column("specimen_holder_model", String(128), nullable=True),
    Column("details", String(255), nullable=True),
    Column("date", DateTime, nullable=True),
    Column("accelerating_voltage", Integer, nullable=True),
    Column("illumination_mode", String(128)),
    Column("mode", String(128)),
    Column("nominal_cs", Float, nullable=True),
    Column("nominal_defocus_min", Float, nullable=True),
    Column("nominal_defocus_max", Float, nullable=True),
    Column("calibrated_defocus_min", Float, nullable=True),
    Column("calibrated_defocus_max", Float, nullable=True),
    Column("tilt_angle_min", Float, nullable=True),
    Column("tilt_angle_max", Float, nullable=True),
    Column("nominal_magnification", Integer, nullable=True),
    Column("calibrated_magnification", Integer, nullable=True),
    Column("electron_source", String(128), nullable=True),
    Column("electron_dose", Float, nullable=True),
    Column("energy_filter", String(128), nullable=True),
    Column("energy_window", String(128), nullable=True),
    Column("citation_id", String(20), nullable=True),
    Column("temperature", Float, nullable=True),
    Column("detector_distance", Float, nullable=True),
    Column("recording_temperature_minimum", Float, nullable=True),
    Column("recording_temperature_maximum", Float, nullable=True),
    Column("alignment_procedure", String(128), nullable=True),
    Column("c2_aperture_diameter", Float, nullable=True),
    Column("specimen_id", String(20)),
    Column("cryogen", String(255), nullable=True)
)


em_detector = Table("em_detector",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("type", String(128), nullable=True),
    Column("detective_quantum_efficiency", Float, nullable=True),
    Column("mode", String(128), nullable=True)
)


em_image_scans = Table("em_image_scans",
    metadata_obj,
    Column("entry_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("number_digital_images", Integer, nullable=True),
    Column("details", String(255), nullable=True),
    Column("scanner_model", String(128), nullable=True),
    Column("sampling_size", Float, nullable=True),
    Column("od_range", Float, nullable=True),
    Column("quant_bit_size", Integer, nullable=True),
    Column("citation_id", String(20), nullable=True),
    Column("dimension_height", Integer, nullable=True),
    Column("dimension_width", Integer, nullable=True),
    Column("frames_per_image", Integer, nullable=True),
    Column("image_recording_id", String(20), primary_key=True),
    Column("used_frames_per_image", String(20), nullable=True)
)


em_2d_projection_selection = Table("em_2d_projection_selection",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20)),
    Column("num_particles", Integer, nullable=True),
    Column("software_name", String(128), nullable=True),
    Column("method", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("citation_id", String(20), nullable=True)
)


em_3d_reconstruction = Table("em_3d_reconstruction",
    metadata_obj,
    Column("entry_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("method", String(255), nullable=True),
    Column("algorithm", String(255), nullable=True),
    Column("citation_id", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("resolution", Float, nullable=True),
    Column("resolution_method", String(255), nullable=True),
    Column("magnification_calibration", String(255), nullable=True),
    Column("ctf_correction_method", String(255), nullable=True),
    Column("nominal_pixel_size", Float, nullable=True),
    Column("actual_pixel_size", Float, nullable=True),
    Column("num_particles", Integer, nullable=True),
    Column("euler_angles_details", String(255), nullable=True),
    Column("num_class_averages", Integer, nullable=True),
    Column("software", String(255), nullable=True),
    Column("fsc_type", String(255), nullable=True),
    Column("refinement_type", String(255), nullable=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("symmetry_type", String(128), nullable=True)
)


em_3d_fitting = Table("em_3d_fitting",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entry_id", String(20), primary_key=True),
    Column("method", String(128), nullable=True),
    Column("target_criteria", String(255), nullable=True),
    Column("software_name", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("overall_b_value", Float, nullable=True),
    Column("ref_space", String(128), nullable=True),
    Column("ref_protocol", String(128), nullable=True),
    Column("initial_refinement_model_id", Integer, nullable=True)
)


em_3d_fitting_list = Table("em_3d_fitting_list",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("3d_fitting_id", String(20), primary_key=True),
    Column("pdb_entry_id", String(20), nullable=True),
    Column("pdb_chain_id", String(80), nullable=True),
    Column("pdb_chain_residue_range", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("chain_id", String(80), nullable=True),
    Column("chain_residue_range", String(20), nullable=True),
    Column("source_name", String(20), nullable=True),
    Column("type", String(128), nullable=True),
    Column("accession_code", String(128), nullable=True),
    Column("initial_refinement_model_id", Integer, nullable=True)
)


em_helical_entity = Table("em_helical_entity",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entity_assembly_id", String(20), nullable=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True),
    Column("dyad", String(128), nullable=True),
    Column("axial_symmetry", String(5)),
    Column("angular_rotation_per_subunit", Float, nullable=True),
    Column("axial_rise_per_subunit", Float, nullable=True),
    Column("hand", String(255), nullable=True)
)


em_experiment = Table("em_experiment",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("id", String(20)),
    Column("reconstruction_method", String(128)),
    Column("aggregation_state", String(128)),
    Column("specimen_type", String(255), nullable=True),
    Column("entity_assembly_id", String(20))
)


em_single_particle_entity = Table("em_single_particle_entity",
    metadata_obj,
    Column("entry_id", String(20)),
    Column("id", Integer, primary_key=True),
    Column("symmetry_type", String(128), nullable=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("point_symmetry", String(20), nullable=True)
)


em_admin = Table("em_admin",
    metadata_obj,
    Column("current_status", String(20)),
    Column("deposition_date", DateTime),
    Column("deposition_site", String(20)),
    Column("details", String(255), nullable=True),
    Column("entry_id", String(20), primary_key=True),
    Column("last_update", DateTime),
    Column("map_release_date", DateTime, nullable=True),
    Column("map_hold_date", DateTime, nullable=True),
    Column("header_release_date", DateTime, nullable=True),
    Column("obsoleted_date", DateTime, nullable=True),
    Column("replace_existing_entry_flag", String(20), nullable=True),
    Column("title", String(128)),
    Column("process_site", String(20), nullable=True),
    Column("composite_map", String(128), nullable=True)
)


em_author_list = Table("em_author_list",
    metadata_obj,
    Column("author", String(150)),
    Column("identifier_ORCID", String(20), nullable=True),
    Column("ordinal", Integer, primary_key=True)
)


em_db_reference = Table("em_db_reference",
    metadata_obj,
    Column("access_code", String(20)),
    Column("db_name", String(20)),
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("relationship", String(128), nullable=True)
)


em_db_reference_auxiliary = Table("em_db_reference_auxiliary",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("link", String(20)),
    Column("link_type", String(255))
)


em_depui = Table("em_depui",
    metadata_obj,
    Column("composite_map_deposition", String(128), nullable=True),
    Column("depositor_hold_instructions", String(128)),
    Column("entry_id", String(20), primary_key=True),
    Column("macromolecule_description", String(10)),
    Column("obsolete_instructions", String(255), nullable=True),
    Column("same_authors_as_pdb", String(10)),
    Column("same_title_as_pdb", String(10))
)


em_obsolete = Table("em_obsolete",
    metadata_obj,
    Column("date", DateTime),
    Column("details", String(255), nullable=True),
    Column("entry", String(15)),
    Column("id", String(20), primary_key=True)
)


em_supersede = Table("em_supersede",
    metadata_obj,
    Column("date", DateTime),
    Column("details", String(255), nullable=True),
    Column("entry", String(15)),
    Column("id", String(20), primary_key=True)
)


em_entity_assembly_molwt = Table("em_entity_assembly_molwt",
    metadata_obj,
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("experimental_flag", String(20), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("units", String(20), nullable=True),
    Column("value", Float, nullable=True),
    Column("method", String(255), nullable=True)
)


em_entity_assembly_naturalsource = Table("em_entity_assembly_naturalsource",
    metadata_obj,
    Column("cell", String(255), nullable=True),
    Column("cellular_location", String(255), nullable=True),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer),
    Column("organism", String(128)),
    Column("organelle", String(255), nullable=True),
    Column("organ", String(128), nullable=True),
    Column("strain", String(255), nullable=True),
    Column("tissue", String(255), nullable=True),
    Column("details", String(255), nullable=True)
)


em_entity_assembly_synthetic = Table("em_entity_assembly_synthetic",
    metadata_obj,
    Column("cell", String(255), nullable=True),
    Column("cellular_location", String(255), nullable=True),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer),
    Column("organism", String(128)),
    Column("organelle", String(255), nullable=True),
    Column("organ", String(128), nullable=True),
    Column("strain", String(255), nullable=True),
    Column("tissue", String(255), nullable=True)
)


em_entity_assembly_recombinant = Table("em_entity_assembly_recombinant",
    metadata_obj,
    Column("cell", String(128), nullable=True),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer),
    Column("organism", String(128)),
    Column("plasmid", String(128), nullable=True),
    Column("strain", String(128), nullable=True)
)


em_virus_natural_host = Table("em_virus_natural_host",
    metadata_obj,
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("ncbi_tax_id", Integer, nullable=True),
    Column("organism", String(128), nullable=True),
    Column("strain", String(255), nullable=True)
)


em_virus_synthetic = Table("em_virus_synthetic",
    metadata_obj,
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("organism", String(128), nullable=True),
    Column("ncbi_tax_id", Integer, nullable=True),
    Column("strain", String(255), nullable=True)
)


em_virus_shell = Table("em_virus_shell",
    metadata_obj,
    Column("diameter", Float, nullable=True),
    Column("entity_assembly_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=True),
    Column("triangulation", Integer, nullable=True)
)


em_specimen = Table("em_specimen",
    metadata_obj,
    Column("concentration", Float, nullable=True),
    Column("details", String(255), nullable=True),
    Column("embedding_applied", String(80)),
    Column("experiment_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("shadowing_applied", String(80)),
    Column("staining_applied", String(80)),
    Column("vitrification_applied", String(80))
)


em_embedding = Table("em_embedding",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("material", String(128)),
    Column("specimen_id", String(20))
)


em_fiducial_markers = Table("em_fiducial_markers",
    metadata_obj,
    Column("diameter", Float),
    Column("em_tomography_specimen_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("manufacturer", String(128))
)


em_focused_ion_beam = Table("em_focused_ion_beam",
    metadata_obj,
    Column("current", Float),
    Column("details", String(255), nullable=True),
    Column("dose_rate", Integer, nullable=True),
    Column("duration", Float),
    Column("em_tomography_specimen_id", String(20)),
    Column("final_thickness", Integer),
    Column("id", String(20), primary_key=True),
    Column("initial_thickness", Integer),
    Column("instrument", String(128)),
    Column("ion", String(128)),
    Column("temperature", Integer),
    Column("voltage", Integer)
)


em_grid_pretreatment = Table("em_grid_pretreatment",
    metadata_obj,
    Column("atmosphere", String(128), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("pressure", Float, nullable=True),
    Column("sample_support_id", String(20)),
    Column("time", Integer, nullable=True),
    Column("type", String(128), nullable=True)
)


em_ultramicrotomy = Table("em_ultramicrotomy",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("em_tomography_specimen_id", String(20)),
    Column("final_thickness", Integer),
    Column("id", String(20), primary_key=True),
    Column("instrument", String(128)),
    Column("temperature", Integer)
)


em_high_pressure_freezing = Table("em_high_pressure_freezing",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("em_tomography_specimen_id", String(20)),
    Column("id", String(20), primary_key=True),
    Column("instrument", String(128))
)


em_shadowing = Table("em_shadowing",
    metadata_obj,
    Column("angle", Float),
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("material", String(128)),
    Column("specimen_id", String(20), primary_key=True),
    Column("thickness", Float)
)


em_tomography_specimen = Table("em_tomography_specimen",
    metadata_obj,
    Column("cryo_protectant", String(128), nullable=True),
    Column("details", String(255), nullable=True),
    Column("fiducial_markers", String(20), nullable=True),
    Column("high_pressure_freezing", String(20), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("sectioning", String(128), nullable=True),
    Column("specimen_id", String(20))
)


em_crystal_formation = Table("em_crystal_formation",
    metadata_obj,
    Column("atmosphere", String(255), nullable=True),
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("instrument", String(128), nullable=True),
    Column("lipid_mixture", String(255), nullable=True),
    Column("lipid_protein_ratio", Float, nullable=True),
    Column("specimen_id", String(20)),
    Column("temperature", Integer, nullable=True),
    Column("time", Integer, nullable=True),
    Column("time_unit", String(20), nullable=True)
)


em_staining = Table("em_staining",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("material", String(128)),
    Column("specimen_id", String(20)),
    Column("type", String(20))
)


em_support_film = Table("em_support_film",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("material", String(128), nullable=True),
    Column("sample_support_id", String(20)),
    Column("thickness", Float, nullable=True),
    Column("topology", String(128), nullable=True)
)


em_buffer_component = Table("em_buffer_component",
    metadata_obj,
    Column("buffer_id", String(20), primary_key=True),
    Column("concentration", Float, nullable=True),
    Column("concentration_units", String(128), nullable=True),
    Column("formula", String(20), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("name", String(128), nullable=True)
)


em_diffraction = Table("em_diffraction",
    metadata_obj,
    Column("camera_length", Float),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20)),
    Column("tilt_angle_list", String(128), nullable=True)
)


em_diffraction_shell = Table("em_diffraction_shell",
    metadata_obj,
    Column("em_diffraction_stats_id", String(20), nullable=True),
    Column("fourier_space_coverage", Float),
    Column("high_resolution", Float),
    Column("id", String(20), primary_key=True),
    Column("low_resolution", Float),
    Column("multiplicity", Float),
    Column("num_structure_factors", Integer),
    Column("phase_residual", Float)
)


em_diffraction_stats = Table("em_diffraction_stats",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("fourier_space_coverage", Float),
    Column("high_resolution", Float),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), nullable=True),
    Column("num_intensities_measured", Integer),
    Column("num_structure_factors", Integer),
    Column("overall_phase_error", Float, nullable=True),
    Column("overall_phase_residual", Float, nullable=True),
    Column("phase_error_rejection_criteria", String(128)),
    Column("r_merge", Float),
    Column("r_sym", Float, nullable=True)
)


em_tomography = Table("em_tomography",
    metadata_obj,
    Column("axis1_angle_increment", Float, nullable=True),
    Column("axis1_max_angle", Float, nullable=True),
    Column("axis1_min_angle", Float, nullable=True),
    Column("axis2_angle_increment", Float, nullable=True),
    Column("axis2_max_angle", Float, nullable=True),
    Column("axis2_min_angle", Float, nullable=True),
    Column("dual_tilt_axis_rotation", Float, nullable=True),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20), primary_key=True)
)


em_image_recording = Table("em_image_recording",
    metadata_obj,
    Column("average_exposure_time", Float, nullable=True),
    Column("avg_electron_dose_per_subtomogram", Float, nullable=True),
    Column("avg_electron_dose_per_image", Float, nullable=True),
    Column("details", String(255), nullable=True),
    Column("detector_mode", String(128), nullable=True),
    Column("film_or_detector_model", String(128), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20), primary_key=True),
    Column("num_diffraction_images", Integer, nullable=True),
    Column("num_grids_imaged", Integer, nullable=True),
    Column("num_real_images", Integer, nullable=True)
)


em_imaging_optics = Table("em_imaging_optics",
    metadata_obj,
    Column("chr_aberration_corrector", String(255), nullable=True),
    Column("energyfilter_lower", String(128), nullable=True),
    Column("energyfilter_slit_width", Float, nullable=True),
    Column("energyfilter_name", String(128), nullable=True),
    Column("energyfilter_upper", String(128), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("imaging_id", String(20), primary_key=True),
    Column("phase_plate", String(255), nullable=True),
    Column("sph_aberration_corrector", String(255), nullable=True),
    Column("details", String(128), nullable=True)
)


em_final_classification = Table("em_final_classification",
    metadata_obj,
    Column("avg_num_images_per_class", Integer, nullable=True),
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20)),
    Column("num_classes", Integer, nullable=True),
    Column("type", String(20), nullable=True)
)


em_start_model = Table("em_start_model",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("emdb_id", String(15), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("insilico_model", String(255), nullable=True),
    Column("orthogonal_tilt_angle1", Float, nullable=True),
    Column("orthogonal_tilt_angle2", Float, nullable=True),
    Column("orthogonal_tilt_num_images", Integer, nullable=True),
    Column("other", String(255), nullable=True),
    Column("pdb_id", String(20), nullable=True),
    Column("random_conical_tilt_angle", Float, nullable=True),
    Column("random_conical_tilt_num_images", Integer, nullable=True),
    Column("type", String(128))
)


em_software = Table("em_software",
    metadata_obj,
    Column("category", String(128), nullable=True),
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), nullable=True),
    Column("fitting_id", String(20), nullable=True),
    Column("imaging_id", String(20), nullable=True),
    Column("name", String(128), nullable=True),
    Column("version", String(128), nullable=True)
)


em_euler_angle_assignment = Table("em_euler_angle_assignment",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20)),
    Column("order", String(20)),
    Column("proj_matching_angular_sampling", Float, nullable=True),
    Column("proj_matching_merit_function", String(128), nullable=True),
    Column("proj_matching_num_projections", Integer, nullable=True),
    Column("type", String(128))
)


em_ctf_correction = Table("em_ctf_correction",
    metadata_obj,
    Column("amplitude_correction", String(20), nullable=True),
    Column("amplitude_correction_factor", Float, nullable=True),
    Column("amplitude_correction_space", String(20), nullable=True),
    Column("correction_operation", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("em_image_processing_id", String(20), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("phase_reversal", String(20), nullable=True),
    Column("phase_reversal_anisotropic", String(20), nullable=True),
    Column("phase_reversal_correction_space", String(20), nullable=True),
    Column("type", String(128), nullable=True)
)


em_volume_selection = Table("em_volume_selection",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("method", String(255), nullable=True),
    Column("num_tomograms", Integer),
    Column("num_volumes_extracted", Integer),
    Column("reference_model", String(255), nullable=True)
)


em_3d_crystal_entity = Table("em_3d_crystal_entity",
    metadata_obj,
    Column("angle_alpha", Float, default=90.0),
    Column("angle_beta", Float, default=90.0),
    Column("angle_gamma", Float, default=90.0),
    Column("image_processing_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("length_a", Float),
    Column("length_b", Float),
    Column("length_c", Float),
    Column("space_group_name", String(128)),
    Column("space_group_num", Integer)
)


em_2d_crystal_entity = Table("em_2d_crystal_entity",
    metadata_obj,
    Column("angle_gamma", Float, default=90.0),
    Column("c_sampling_length", Float, nullable=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("id", String(20), primary_key=True),
    Column("entity_assembly_id", String(20), nullable=True),
    Column("length_a", Float),
    Column("length_b", Float),
    Column("length_c", Float),
    Column("space_group_name_H-M", String(128))
)


em_image_processing = Table("em_image_processing",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("image_recording_id", String(20), primary_key=True)
)


em_particle_selection = Table("em_particle_selection",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("image_processing_id", String(20), primary_key=True),
    Column("method", String(255), nullable=True),
    Column("num_particles_selected", Integer, nullable=True),
    Column("reference_model", String(255), nullable=True)
)


em_map = Table("em_map",
    metadata_obj,
    Column("annotation_details", String(255), nullable=True),
    Column("axis_order_fast", String(20)),
    Column("axis_order_medium", String(20)),
    Column("axis_order_slow", String(20)),
    Column("cell_a", Float),
    Column("cell_b", Float),
    Column("cell_c", Float),
    Column("cell_alpha", Float),
    Column("cell_beta", Float),
    Column("cell_gamma", Float),
    Column("contour_level", Float, nullable=True),
    Column("contour_level_source", String(128), nullable=True),
    Column("data_type", String(128)),
    Column("dimensions_col", Integer),
    Column("dimensions_row", Integer),
    Column("dimensions_sec", Integer),
    Column("endian_type", String(20)),
    Column("file", String(128), nullable=True),
    Column("original_file", String(128), nullable=True),
    Column("format", String(20)),
    Column("id", Integer, primary_key=True),
    Column("partition", Integer),
    Column("entry_id", String(20), primary_key=True),
    Column("label", String(255), nullable=True),
    Column("limit_col", Integer, nullable=True),
    Column("limit_row", Integer, nullable=True),
    Column("limit_sec", Integer, nullable=True),
    Column("origin_col", Integer),
    Column("origin_row", Integer),
    Column("origin_sec", Integer),
    Column("pixel_spacing_x", Float),
    Column("pixel_spacing_y", Float),
    Column("pixel_spacing_z", Float),
    Column("size_kb", Integer),
    Column("spacing_x", Integer),
    Column("spacing_y", Integer),
    Column("spacing_z", Integer),
    Column("statistics_average", Float, nullable=True),
    Column("statistics_maximum", Float, nullable=True),
    Column("statistics_minimum", Float, nullable=True),
    Column("statistics_std", Float, nullable=True),
    Column("symmetry_space_group", Integer),
    Column("type", String(128))
)


em_fsc_curve = Table("em_fsc_curve",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("file", String(128), nullable=True),
    Column("id", String(20), primary_key=True)
)


em_interpret_figure = Table("em_interpret_figure",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("file", String(128)),
    Column("id", String(20), primary_key=True)
)


em_layer_lines = Table("em_layer_lines",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("experiment_id", String(20), primary_key=True),
    Column("file", String(128)),
    Column("id", String(20), primary_key=True)
)


em_structure_factors = Table("em_structure_factors",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("experiment_id", String(20), primary_key=True),
    Column("file", String(128)),
    Column("id", String(20), primary_key=True)
)


em_depositor_info = Table("em_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("em_method_selection", String(128)),
    Column("molecular_description_flag", String(20), nullable=True)
)


em_map_depositor_info = Table("em_map_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("experiment_id", String(20), nullable=True),
    Column("id", String(20), primary_key=True),
    Column("map_type", String(20)),
    Column("upload_file_name", String(128)),
    Column("upload_format", String(20)),
    Column("contour_level", Float, nullable=True),
    Column("annotation_details", String(255), nullable=True),
    Column("pixel_spacing_x", Float),
    Column("pixel_spacing_y", Float),
    Column("pixel_spacing_z", Float)
)


em_mask_depositor_info = Table("em_mask_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("upload_file_name", String(128)),
    Column("upload_format", String(20)),
    Column("contour_level", Float, nullable=True),
    Column("annotation_details", String(255), nullable=True),
    Column("pixel_spacing_x", Float),
    Column("pixel_spacing_y", Float),
    Column("pixel_spacing_z", Float)
)


em_figure_depositor_info = Table("em_figure_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("experiment_id", String(20), nullable=True),
    Column("upload_file_name", String(128)),
    Column("details", String(255), nullable=True)
)


em_layer_lines_depositor_info = Table("em_layer_lines_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("experiment_id", String(20), nullable=True),
    Column("upload_file_name", String(128)),
    Column("details", String(255), nullable=True)
)


em_structure_factors_depositor_info = Table("em_structure_factors_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("experiment_id", String(20), nullable=True),
    Column("upload_file_name", String(128)),
    Column("details", String(255), nullable=True)
)


pdbx_seq_map_depositor_info = Table("pdbx_seq_map_depositor_info",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("auth_asym_id", String(20), primary_key=True),
    Column("one_letter_code", String(255)),
    Column("one_letter_code_mod", String(255), nullable=True)
)


pdbx_chem_comp_depositor_info = Table("pdbx_chem_comp_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("comp_id", String(10)),
    Column("alt_comp_id", String(10), nullable=True),
    Column("name", String(255), nullable=True),
    Column("formula", String(255), nullable=True),
    Column("type", String(128), nullable=True),
    Column("descriptor", String(255), nullable=True),
    Column("descriptor_type", String(50), nullable=True),
    Column("in_dictionary_flag", String(20), nullable=True),
    Column("details", String(255), nullable=True),
    Column("upload_file_name", String(128), nullable=True),
    Column("upload_file_type", String(20), nullable=True)
)


pdbx_struct_ref_seq_depositor_info = Table("pdbx_struct_ref_seq_depositor_info",
    metadata_obj,
    Column("ref_id", String(20), primary_key=True),
    Column("entity_id", String(20)),
    Column("db_align_beg", Integer, nullable=True),
    Column("db_align_end", Integer, nullable=True),
    Column("details", String(255), nullable=True),
    Column("db_accession", String(20), nullable=True),
    Column("db_code", String(128), nullable=True),
    Column("db_name", String(128), nullable=True),
    Column("db_seq_one_letter_code", String(255), nullable=True),
    Column("seq_align_begin", String(20), nullable=True),
    Column("seq_align_end", String(20), nullable=True)
)


pdbx_struct_ref_seq_dif_depositor_info = Table("pdbx_struct_ref_seq_dif_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("ref_id", String(20)),
    Column("entity_id", String(20)),
    Column("db_mon_id", String(10), nullable=True),
    Column("db_seq_id", Integer, nullable=True),
    Column("details", String(255), nullable=True),
    Column("auth_mon_id", String(10), nullable=True),
    Column("auth_seq_id", Integer, nullable=True),
    Column("db_accession", String(20), nullable=True),
    Column("db_code", String(128), nullable=True),
    Column("db_name", String(128), nullable=True),
    Column("annotation", String(50), nullable=True)
)


pdbx_struct_assembly_prop_depositor_info = Table("pdbx_struct_assembly_prop_depositor_info",
    metadata_obj,
    Column("biol_id", String(20), primary_key=True),
    Column("type", String(128), primary_key=True),
    Column("value", String(255)),
    Column("details", String(255), nullable=True)
)


pdbx_struct_assembly_depositor_info = Table("pdbx_struct_assembly_depositor_info",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("id", String(128), primary_key=True),
    Column("method_details", String(255), nullable=True),
    Column("oligomeric_details", String(128), nullable=True),
    Column("oligomeric_count", String(128), nullable=True),
    Column("matrix_flag", String(20), nullable=True),
    Column("upload_file_name", String(255), nullable=True)
)


pdbx_struct_assembly_gen_depositor_info = Table("pdbx_struct_assembly_gen_depositor_info",
    metadata_obj,
    Column("id", String(128), primary_key=True),
    Column("asym_id_list", String(128)),
    Column("assembly_id", String(128)),
    Column("oper_expression", String(511)),
    Column("full_matrices", String(10), nullable=True),
    Column("symmetry_operation", String(80), nullable=True),
    Column("at_unit_matrix", String(2), nullable=True),
    Column("chain_id_list", String(200), nullable=True),
    Column("all_chains", String(2), nullable=True),
    Column("helical_rotation", Float, nullable=True),
    Column("helical_rise", Float, nullable=True)
)


pdbx_struct_oper_list_depositor_info = Table("pdbx_struct_oper_list_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(128)),
    Column("name", String(128), nullable=True),
    Column("symmetry_operation", String(128), nullable=True),
    Column("matrix[1][1]", Float, nullable=True),
    Column("matrix[1][2]", Float, nullable=True),
    Column("matrix[1][3]", Float, nullable=True),
    Column("matrix[2][1]", Float, nullable=True),
    Column("matrix[2][2]", Float, nullable=True),
    Column("matrix[2][3]", Float, nullable=True),
    Column("matrix[3][1]", Float, nullable=True),
    Column("matrix[3][2]", Float, nullable=True),
    Column("matrix[3][3]", Float, nullable=True),
    Column("vector[1]", Float, nullable=True),
    Column("vector[2]", Float, nullable=True),
    Column("vector[3]", Float, nullable=True)
)


pdbx_point_symmetry_depositor_info = Table("pdbx_point_symmetry_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("Schoenflies_symbol", String(20)),
    Column("circular_symmetry", Integer, nullable=True),
    Column("H-M_notation", String(20), nullable=True),
    Column("status_flag", String(20), nullable=True)
)


pdbx_helical_symmetry_depositor_info = Table("pdbx_helical_symmetry_depositor_info",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("number_of_operations", Integer, nullable=True),
    Column("rotation_per_n_subunits", Float, nullable=True),
    Column("rise_per_n_subunits", Float, nullable=True),
    Column("n_subunits_divisor", Integer, nullable=True),
    Column("dyad_axis", String(20), nullable=True),
    Column("circular_symmetry", Integer, nullable=True),
    Column("status_flag", String(20), nullable=True)
)


pdbx_struct_assembly_auth_evidence_depositor_info = Table("pdbx_struct_assembly_auth_evidence_depositor_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(128), primary_key=True),
    Column("experimental_support", String(128)),
    Column("details", String(255), nullable=True)
)


pdbx_solvent_atom_site_mapping = Table("pdbx_solvent_atom_site_mapping",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_atom_id", String(6), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("pre_auth_asym_id", String(20), nullable=True),
    Column("pre_auth_atom_id", String(6), nullable=True),
    Column("pre_auth_comp_id", String(20), nullable=True),
    Column("pre_auth_seq_id", String(20), nullable=True),
    Column("pre_PDB_ins_code", String(20), nullable=True),
    Column("pre_auth_alt_id", String(20), nullable=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_atom_id", String(6), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("auth_alt_id", String(20), nullable=True),
    Column("occupancy", Float, nullable=True),
    Column("Cartn_x", Float, nullable=True),
    Column("Cartn_y", Float, nullable=True),
    Column("Cartn_z", Float, nullable=True),
    Column("pre_Cartn_x", Float, nullable=True),
    Column("pre_Cartn_y", Float, nullable=True),
    Column("pre_Cartn_z", Float, nullable=True),
    Column("symmetry", String(10), nullable=True),
    Column("symmetry_as_xyz", String(128), nullable=True, default="x,y,z")
)


pdbx_molecule_features_depositor_info = Table("pdbx_molecule_features_depositor_info",
    metadata_obj,
    Column("entity_id", String(10), primary_key=True),
    Column("class", String(50), nullable=True),
    Column("type", String(50), nullable=True),
    Column("name", String(255), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_chem_comp_instance_depositor_info = Table("pdbx_chem_comp_instance_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("comp_id", String(10)),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("auth_asym_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("in_polymer_flag", String(20), nullable=True),
    Column("author_provided_flag", String(20), nullable=True),
    Column("formula", String(255), nullable=True)
)


pdbx_depui_status_flags = Table("pdbx_depui_status_flags",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("primary_citation_status", String(20), nullable=True),
    Column("corresponding_author_status", String(20), nullable=True),
    Column("reference_citation_status", String(20), nullable=True),
    Column("is_grant_funded", String(20), nullable=True),
    Column("has_ncs_data", String(20), nullable=True),
    Column("prediction_target", String(20), nullable=True),
    Column("has_helical_symmetry", String(20), nullable=True),
    Column("has_point_symmetry", String(20), nullable=True),
    Column("has_cyclic_symmetry", String(20), nullable=True),
    Column("has_accepted_terms_and_conditions", String(20)),
    Column("has_viewed_validation_report", String(20), nullable=True),
    Column("validated_model_file_name", String(128), nullable=True),
    Column("merge_prior_model_file_name", String(128), nullable=True),
    Column("merge_replace_model_file_name", String(128), nullable=True),
    Column("merge_output_model_file_name", String(128), nullable=True),
    Column("is_ligand_processing_complete", String(255)),
    Column("sample_xyz_sequence_alignments_valid", String(255)),
    Column("has_sas_data", String(20), nullable=True),
    Column("is_sas_deposited", String(20), nullable=True),
    Column("use_sas_refine", String(20), nullable=True),
    Column("merged_fail", String(20), nullable=True),
    Column("post_rel_replacement_reason", String(128), nullable=True),
    Column("post_rel_replacement_reason_details", String(255), nullable=True),
    Column("has_accepted_assemblies", String(20), nullable=True)
)


pdbx_depui_upload = Table("pdbx_depui_upload",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("file_content_type", String(128), nullable=True),
    Column("file_type", String(128), nullable=True),
    Column("file_name", String(128), nullable=True),
    Column("file_size", Integer, nullable=True),
    Column("valid_flag", String(20), nullable=True),
    Column("diagnostic_message", String(255), nullable=True),
    Column("sequence_align", String(255), nullable=True)
)


pdbx_depui_validation_status_flags = Table("pdbx_depui_validation_status_flags",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("residual_B_factors_flag", String(20), nullable=True),
    Column("occupancy_outliers_low", Integer, nullable=True),
    Column("occupancy_outliers_high", Integer, nullable=True),
    Column("adp_outliers_low", Integer, nullable=True),
    Column("solvent_outliers", Integer, nullable=True),
    Column("tls_no_aniso", String(20), nullable=True),
    Column("adp_outliers_zero", String(255), nullable=True)
)


pdbx_chem_comp_upload_depositor_info = Table("pdbx_chem_comp_upload_depositor_info",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("comp_id", String(10)),
    Column("upload_file_type", String(50)),
    Column("upload_file_name", String(128))
)


pdbx_depui_entity_status_flags = Table("pdbx_depui_entity_status_flags",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("has_mutation", String(20), nullable=True),
    Column("sample_xyz_sequence_alignments_valid", String(255))
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
    Column("deposition_data_set_id", String(20)),
    Column("message_id", String(20)),
    Column("timestamp", String(128)),
    Column("sender", String(128)),
    Column("content_type", String(128)),
    Column("content_value", String(128)),
    Column("parent_message_id", String(20)),
    Column("message_subject", String(255)),
    Column("message_text", String(255)),
    Column("message_type", String(20)),
    Column("send_status", String(20))
)


pdbx_deposition_message_file_reference = Table("pdbx_deposition_message_file_reference",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("deposition_data_set_id", String(20)),
    Column("message_id", String(20)),
    Column("content_type", String(20)),
    Column("content_format", String(128)),
    Column("partition_number", String(20)),
    Column("version_id", String(20)),
    Column("storage_type", String(20))
)


pdbx_depui_entry_details = Table("pdbx_depui_entry_details",
    metadata_obj,
    Column("dep_dataset_id", String(20), primary_key=True),
    Column("wwpdb_site_id", String(20), nullable=True),
    Column("experimental_methods", String(255)),
    Column("requested_accession_types", String(128)),
    Column("validated_contact_email", String(128)),
    Column("validated_identifier_ORCID", String(20), nullable=True),
    Column("country", String(128)),
    Column("structural_genomics_flag", String(20), nullable=True),
    Column("related_database_name", String(128), nullable=True),
    Column("related_database_code", String(128), nullable=True),
    Column("replace_pdb_id", String(255), nullable=True)
)


pdbx_data_processing_status = Table("pdbx_data_processing_status",
    metadata_obj,
    Column("task_name", String(128), primary_key=True),
    Column("status", String(128), primary_key=True)
)


pdbx_entity_instance_feature = Table("pdbx_entity_instance_feature",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("feature_type", String(128), nullable=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("asym_id", String(20), nullable=True),
    Column("auth_seq_num", String(20), nullable=True),
    Column("seq_num", Integer, nullable=True),
    Column("comp_id", String(10), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_entity_src_gen_depositor_info = Table("pdbx_entity_src_gen_depositor_info",
    metadata_obj,
    Column("src_id", Integer, primary_key=True),
    Column("entity_id", String(20)),
    Column("seq_type", String(128), nullable=True),
    Column("beg_seq_num", Integer),
    Column("end_seq_num", Integer),
    Column("gene_src_gene", String(255), nullable=True),
    Column("gene_src_scientific_name", String(255), nullable=True),
    Column("host_org_gene", String(255), nullable=True),
    Column("host_org_scientific_name", String(255), nullable=True),
    Column("host_org_strain", String(255), nullable=True),
    Column("gene_src_ncbi_taxonomy_id", Integer, nullable=True),
    Column("host_org_ncbi_taxonomy_id", Integer, nullable=True),
    Column("host_org_vector_type", String(255), nullable=True),
    Column("plasmid_name", String(255), nullable=True)
)


pdbx_chem_comp_model = Table("pdbx_chem_comp_model",
    metadata_obj,
    Column("id", String(10), primary_key=True),
    Column("comp_id", String(10))
)


pdbx_chem_comp_model_atom = Table("pdbx_chem_comp_model_atom",
    metadata_obj,
    Column("atom_id", String(6), primary_key=True),
    Column("ordinal_id", Integer),
    Column("model_id", String(10), primary_key=True),
    Column("charge", Integer, nullable=True, default=0),
    Column("model_Cartn_x", Float, nullable=True),
    Column("model_Cartn_y", Float, nullable=True),
    Column("model_Cartn_z", Float, nullable=True),
    Column("type_symbol", String(20))
)


pdbx_chem_comp_model_bond = Table("pdbx_chem_comp_model_bond",
    metadata_obj,
    Column("atom_id_1", String(6), primary_key=True),
    Column("atom_id_2", String(6), primary_key=True),
    Column("model_id", String(10), primary_key=True),
    Column("value_order", String(10), nullable=True, default="sing"),
    Column("ordinal_id", Integer)
)


pdbx_chem_comp_model_feature = Table("pdbx_chem_comp_model_feature",
    metadata_obj,
    Column("model_id", String(10), primary_key=True),
    Column("feature_name", String(128), primary_key=True),
    Column("feature_value", String(255))
)


pdbx_chem_comp_model_descriptor = Table("pdbx_chem_comp_model_descriptor",
    metadata_obj,
    Column("model_id", String(10), primary_key=True),
    Column("descriptor", String(255)),
    Column("type", String(50), primary_key=True)
)


pdbx_chem_comp_model_audit = Table("pdbx_chem_comp_model_audit",
    metadata_obj,
    Column("model_id", String(10), primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("annotator", String(20), nullable=True),
    Column("processing_site", String(20), nullable=True),
    Column("details", String(255), nullable=True),
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
    Column("description", String(255))
)


pdbx_view_category = Table("pdbx_view_category",
    metadata_obj,
    Column("view_group_id", String(20)),
    Column("category_view_name", String(128))
)


pdbx_view_item = Table("pdbx_view_item",
    metadata_obj,
    Column("item_name", String(80), primary_key=True),
    Column("category_id", String(20)),
    Column("item_view_name", String(128)),
    Column("item_view_mandatory_code", String(20)),
    Column("item_view_allow_alternate_value", String(20), nullable=True, default="N")
)


pdbx_coord = Table("pdbx_coord",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("chain_atoms_Y_P", String(20)),
    Column("hydrogen_atoms_Y_N", String(20)),
    Column("solvent_atoms_Y_N", String(20)),
    Column("structure_factors_Y_N", String(20))
)


pdbx_connect = Table("pdbx_connect",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("hetgroup_name", String(128), nullable=True),
    Column("formul", String(128), nullable=True),
    Column("hetgroup_chemical_name", String(255), nullable=True),
    Column("parent_residue", String(20), nullable=True),
    Column("formal_charge", Integer, nullable=True),
    Column("class_1", String(255), nullable=True),
    Column("class_2", String(255), nullable=True),
    Column("type", String(255), nullable=True),
    Column("status", String(20), nullable=True),
    Column("date", DateTime, nullable=True),
    Column("modified_date", DateTime, nullable=True)
)


pdbx_connect_type = Table("pdbx_connect_type",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("ndbTokenType", String(20), nullable=True),
    Column("modified", String(20), nullable=True)
)


pdbx_connect_modification = Table("pdbx_connect_modification",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("modification", String(128))
)


pdbx_connect_atom = Table("pdbx_connect_atom",
    metadata_obj,
    Column("res_name", String(20), primary_key=True),
    Column("atom_name", String(20), primary_key=True),
    Column("connect_to", String(20), primary_key=True),
    Column("type_symbol", String(20)),
    Column("charge", Integer),
    Column("bond_type", String(20), nullable=True),
    Column("align_pos", Integer, nullable=True)
)


pdbx_database_PDB_master = Table("pdbx_database_PDB_master",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("num_remark", Integer, nullable=True),
    Column("num_ftnote", Integer, nullable=True),
    Column("num_het", Integer, nullable=True),
    Column("num_helix", Integer, nullable=True),
    Column("num_sheet", Integer, nullable=True),
    Column("num_turn", Integer, nullable=True),
    Column("num_site", Integer, nullable=True),
    Column("num_trans", Integer, nullable=True),
    Column("num_coord", Integer, nullable=True),
    Column("num_ter", Integer, nullable=True),
    Column("num_conect", Integer, nullable=True),
    Column("num_seqres", Integer, nullable=True)
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
    Column("begin_ins_code", String(20), nullable=True),
    Column("end_res_number", String(20), primary_key=True),
    Column("end_ins_code", String(20), nullable=True),
    Column("database_name", String(20), primary_key=True),
    Column("database_accession", String(20), nullable=True),
    Column("database_id_code", String(20), nullable=True),
    Column("database_begin_res_number", String(20), nullable=True),
    Column("database_begin_ins_code", String(20), nullable=True),
    Column("database_end_res_number", String(20), nullable=True),
    Column("database_end_ins_code", String(20), nullable=True)
)


pdbx_drug_info = Table("pdbx_drug_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128), primary_key=True),
    Column("num_per_asym_unit", Integer),
    Column("num_of_whole_molecule", Integer, nullable=True),
    Column("size_of_molecule_per_asym_unit", String(20), nullable=True)
)


pdbx_inhibitor_info = Table("pdbx_inhibitor_info",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(128)),
    Column("num_per_asym_unit", Integer)
)


pdbx_ion_info = Table("pdbx_ion_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("numb_per_asym_unit", Integer)
)


pdbx_hybrid = Table("pdbx_hybrid",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("sugar_name", String(128)),
    Column("strand_id", String(20)),
    Column("residue_names", String(128))
)


pdbx_na_strand_info = Table("pdbx_na_strand_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("num_of_NA_strands_per_asym_unit", Integer),
    Column("num_of_NA_strands_per_biol_unit", Integer, nullable=True),
    Column("fract_NA_strand_per_asym_unit", String(20), nullable=True)
)


pdbx_nonstandard_list = Table("pdbx_nonstandard_list",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("label_seq_num", String(20), nullable=True),
    Column("label_seq_id", Integer, primary_key=True),
    Column("ins_code", String(20), nullable=True),
    Column("number_atoms_nh", Integer, nullable=True)
)


pdbx_pdb_compnd = Table("pdbx_pdb_compnd",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("text", String(255), nullable=True)
)


pdbx_pdb_source = Table("pdbx_pdb_source",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("text", String(255), nullable=True)
)


pdbx_protein_info = Table("pdbx_protein_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("num_per_asym_unit", Integer)
)


pdbx_solvent_info = Table("pdbx_solvent_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("numb_per_asym_unit", Integer)
)


pdbx_source = Table("pdbx_source",
    metadata_obj,
    Column("src_method", String(255), primary_key=True)
)


pdbx_struct_biol_func = Table("pdbx_struct_biol_func",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("biol_id", String(128), primary_key=True),
    Column("function", String(255))
)


pdbx_struct_pack_gen = Table("pdbx_struct_pack_gen",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("symmetry", String(10), primary_key=True, default="1_555"),
    Column("color_red", Float, nullable=True),
    Column("color_green", Float, nullable=True),
    Column("color_blue", Float, nullable=True),
    Column("crystal_type", Integer, nullable=True),
    Column("packing_type", Integer, nullable=True)
)


pdbx_trna_info = Table("pdbx_trna_info",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("name", String(128)),
    Column("num_per_asym_unit", Integer)
)


pdbx_unpair = Table("pdbx_unpair",
    metadata_obj,
    Column("chain_id", String(20), primary_key=True),
    Column("residue_name", String(20), nullable=True),
    Column("residue_number", String(20), nullable=True)
)


pdbx_refine_ls_restr_ncs = Table("pdbx_refine_ls_restr_ncs",
    metadata_obj,
    Column("dom_id", String(128), primary_key=True),
    Column("type", String(128), nullable=True),
    Column("number", Integer, nullable=True),
    Column("rms_dev", Float, nullable=True),
    Column("weight", Float, nullable=True)
)


pdbx_struct_ncs_virus_gen = Table("pdbx_struct_ncs_virus_gen",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("oper_id", Integer),
    Column("asym_id", String(20)),
    Column("pdb_chain_id", String(20))
)


pdbx_sequence_annotation = Table("pdbx_sequence_annotation",
    metadata_obj,
    Column("pdb_chain_id", String(20), primary_key=True),
    Column("ncbi_taxid", String(20))
)


pdbx_post_process_details = Table("pdbx_post_process_details",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("text", String(255), nullable=True),
    Column("seq_details", String(255), nullable=True)
)


pdbx_post_process_status = Table("pdbx_post_process_status",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("cycle_id", String(20), primary_key=True),
    Column("date_begin", Date),
    Column("date_end", Date),
    Column("details", String(255)),
    Column("annotator", String(128))
)


pdbx_struct_link = Table("pdbx_struct_link",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(10), nullable=True),
    Column("ptnr1_label_alt_id", String(20), nullable=True),
    Column("ptnr1_label_asym_id", String(20)),
    Column("ptnr1_label_atom_id", String(6)),
    Column("ptnr1_label_comp_id", String(10)),
    Column("ptnr1_label_seq_id", Integer),
    Column("ptnr1_label_ins_code", String(20), nullable=True),
    Column("ptnr1_symmetry", String(10), nullable=True, default="1_555"),
    Column("ptnr2_label_alt_id", String(20), nullable=True),
    Column("ptnr2_label_asym_id", String(20)),
    Column("ptnr2_label_atom_id", String(6)),
    Column("ptnr2_label_comp_id", String(10)),
    Column("ptnr2_label_seq_id", Integer),
    Column("ptnr2_label_ins_code", String(20), nullable=True),
    Column("ptnr2_symmetry", String(10), nullable=True, default="1_555"),
    Column("details", String(128), nullable=True),
    Column("pdbx_dist_value", Float, nullable=True)
)


pdbx_missing_residue_list = Table("pdbx_missing_residue_list",
    metadata_obj,
    Column("pdb_model_id", Integer, nullable=True),
    Column("pdb_chain_id", String(20), primary_key=True),
    Column("pdb_residue_name", String(20), primary_key=True),
    Column("pdb_residue_number", String(20), primary_key=True),
    Column("pdb_insertion_code", String(20), nullable=True),
    Column("label_seq_id", Integer, nullable=True)
)


pdbx_data_processing_cell = Table("pdbx_data_processing_cell",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("a", Float, nullable=True),
    Column("a_tolerance", Float, nullable=True),
    Column("b", Float, nullable=True),
    Column("b_tolerance", Float, nullable=True),
    Column("c", Float, nullable=True),
    Column("c_tolerance", Float, nullable=True),
    Column("alpha", Float, nullable=True),
    Column("alpha_tolerance", Float, nullable=True),
    Column("beta", Float, nullable=True),
    Column("beta_tolerance", Float, nullable=True),
    Column("gamma", Float, nullable=True),
    Column("gamma_tolerance", Float, nullable=True),
    Column("volume", Float, nullable=True),
    Column("mosaicity", Float, nullable=True),
    Column("resolution_range", String(128), nullable=True),
    Column("space_group", String(128), nullable=True)
)


pdbx_data_processing_reflns = Table("pdbx_data_processing_reflns",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("number_all", Integer, nullable=True),
    Column("number_marked_reject", Integer, nullable=True),
    Column("percent_marked_reject", Float, nullable=True),
    Column("percent_rejected", Float, nullable=True),
    Column("R_factor_all_linear", Float, nullable=True)
)


pdbx_data_processing_detector = Table("pdbx_data_processing_detector",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("name", String(128), nullable=True),
    Column("wavelength", Float, nullable=True),
    Column("polarization", Float, nullable=True),
    Column("beam_position_x", Float, nullable=True),
    Column("beam_position_y", Float, nullable=True),
    Column("cassette_rot_x", Float, nullable=True),
    Column("cassette_rot_y", Float, nullable=True),
    Column("cassette_rot_z", Float, nullable=True),
    Column("scale_y", Float, nullable=True),
    Column("skew", Float, nullable=True),
    Column("crossfire_x", Float, nullable=True),
    Column("crossfire_y", Float, nullable=True),
    Column("crossfire_xy", Float, nullable=True),
    Column("date", String(128), nullable=True),
    Column("experimentor", String(255), nullable=True),
    Column("crystal_data_id", String(255), nullable=True),
    Column("processing_path", String(255), nullable=True),
    Column("processing_files", String(255), nullable=True)
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
    Column("name_type", String(128))
)


pdbx_entity_name_instance = Table("pdbx_entity_name_instance",
    metadata_obj,
    Column("name", String(255), primary_key=True),
    Column("pdb_id", String(20), primary_key=True),
    Column("rcsb_id", String(20)),
    Column("entity_id", String(20), primary_key=True),
    Column("pdb_chain_id", String(20)),
    Column("pdb_mol_id", String(20))
)


pdbx_val_angle = Table("pdbx_val_angle",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("auth_atom_id_3", String(6)),
    Column("auth_asym_id_3", String(20)),
    Column("auth_comp_id_3", String(20)),
    Column("auth_seq_id_3", String(20)),
    Column("auth_PDB_insert_id_1", String(20), nullable=True),
    Column("auth_PDB_insert_id_2", String(20), nullable=True),
    Column("auth_PDB_insert_id_3", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_asym_id_1", String(20), nullable=True),
    Column("label_atom_id_1", String(6), nullable=True),
    Column("label_comp_id_1", String(10), nullable=True),
    Column("label_seq_id_1", Integer, nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("label_asym_id_2", String(20), nullable=True),
    Column("label_atom_id_2", String(6), nullable=True),
    Column("label_comp_id_2", String(10), nullable=True),
    Column("label_seq_id_2", Integer, nullable=True),
    Column("label_alt_id_3", String(20), nullable=True),
    Column("label_asym_id_3", String(20), nullable=True),
    Column("label_atom_id_3", String(6), nullable=True),
    Column("label_comp_id_3", String(10), nullable=True),
    Column("label_seq_id_3", Integer, nullable=True),
    Column("angle", Float),
    Column("angle_deviation", Float)
)


pdbx_val_bond = Table("pdbx_val_bond",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("auth_PDB_insert_id_1", String(20), nullable=True),
    Column("auth_PDB_insert_id_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_asym_id_1", String(20), nullable=True),
    Column("label_atom_id_1", String(6), nullable=True),
    Column("label_comp_id_1", String(10), nullable=True),
    Column("label_seq_id_1", Integer, nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("label_asym_id_2", String(20), nullable=True),
    Column("label_atom_id_2", String(6), nullable=True),
    Column("label_comp_id_2", String(10), nullable=True),
    Column("label_seq_id_2", Integer, nullable=True),
    Column("bond", Float),
    Column("bond_deviation", Float)
)


pdbx_val_contact = Table("pdbx_val_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("auth_PDB_insert_id_1", String(20), nullable=True),
    Column("auth_PDB_insert_id_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_asym_id_1", String(20), nullable=True),
    Column("label_atom_id_1", String(6), nullable=True),
    Column("label_comp_id_1", String(10), nullable=True),
    Column("label_seq_id_1", Integer, nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("label_asym_id_2", String(20), nullable=True),
    Column("label_atom_id_2", String(6), nullable=True),
    Column("label_comp_id_2", String(10), nullable=True),
    Column("label_seq_id_2", Integer, nullable=True),
    Column("dist", Float)
)


pdbx_val_sym_contact = Table("pdbx_val_sym_contact",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id_1", String(20)),
    Column("auth_atom_id_1", String(6)),
    Column("auth_comp_id_1", String(20)),
    Column("auth_seq_id_1", String(20)),
    Column("auth_atom_id_2", String(6)),
    Column("auth_asym_id_2", String(20)),
    Column("auth_comp_id_2", String(20)),
    Column("auth_seq_id_2", String(20)),
    Column("auth_PDB_insert_id_1", String(20), nullable=True),
    Column("auth_PDB_insert_id_2", String(20), nullable=True),
    Column("label_alt_id_1", String(20), nullable=True),
    Column("label_asym_id_1", String(20), nullable=True),
    Column("label_atom_id_1", String(6), nullable=True),
    Column("label_comp_id_1", String(10), nullable=True),
    Column("label_seq_id_1", Integer, nullable=True),
    Column("label_alt_id_2", String(20), nullable=True),
    Column("label_asym_id_2", String(20), nullable=True),
    Column("label_atom_id_2", String(6), nullable=True),
    Column("label_comp_id_2", String(10), nullable=True),
    Column("label_seq_id_2", Integer, nullable=True),
    Column("site_symmetry_1", String(20), nullable=True, default="1_555"),
    Column("site_symmetry_2", String(20), nullable=True, default="1_555"),
    Column("dist", Float)
)


pdbx_rmch_outlier = Table("pdbx_rmch_outlier",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("auth_PDB_insert_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("phi", Float),
    Column("psi", Float)
)


pdbx_missing_atom_poly = Table("pdbx_missing_atom_poly",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("auth_PDB_insert_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("atom_name", String(20))
)


pdbx_missing_atom_nonpoly = Table("pdbx_missing_atom_nonpoly",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("auth_PDB_insert_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("atom_name", String(20))
)


pdbx_val_chiral = Table("pdbx_val_chiral",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id", String(20)),
    Column("auth_comp_id", String(20)),
    Column("auth_seq_id", String(20)),
    Column("auth_PDB_insert_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10), nullable=True),
    Column("label_seq_id", Integer, nullable=True),
    Column("chiral_center_atom_name", String(20)),
    Column("chiral_neighbor_atom_name", String(20)),
    Column("chiral_center_atom_alt_id", String(20), nullable=True),
    Column("chiral_neighbor_atom_alt_id", String(20), nullable=True)
)


pdbx_atlas = Table("pdbx_atlas",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("page_id", Integer, primary_key=True),
    Column("page_name", String(255))
)


pdbx_summary_flags = Table("pdbx_summary_flags",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("flag_id", String(128), primary_key=True),
    Column("flag_value", String(20))
)


pdbx_entity_func_bind_mode = Table("pdbx_entity_func_bind_mode",
    metadata_obj,
    Column("domain_id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("protein_binds_to", String(20)),
    Column("type", String(10))
)


pdbx_entity_func_enzyme = Table("pdbx_entity_func_enzyme",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50))
)


pdbx_entity_func_regulatory = Table("pdbx_entity_func_regulatory",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50))
)


pdbx_entity_func_structural = Table("pdbx_entity_func_structural",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50))
)


pdbx_entity_func_other = Table("pdbx_entity_func_other",
    metadata_obj,
    Column("bind_mode_id", String(20), primary_key=True),
    Column("type", String(50))
)


pdbx_entity_poly_domain = Table("pdbx_entity_poly_domain",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("entity_id", String(20), primary_key=True),
    Column("begin_mon_id", String(10)),
    Column("begin_seq_num", Integer),
    Column("end_mon_id", String(10)),
    Column("end_seq_num", Integer)
)


pdbx_na_struct_keywds = Table("pdbx_na_struct_keywds",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("conformation_type", String(128), nullable=True),
    Column("strand_description", String(128), nullable=True),
    Column("special_feature", String(128), nullable=True)
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
    Column("atom_site_label_alt_id_1", String(20), nullable=True),
    Column("atom_site_label_atom_id_1", String(6), nullable=True),
    Column("atom_site_label_comp_id_1", String(10), nullable=True),
    Column("atom_site_label_seq_id_1", Integer, nullable=True),
    Column("atom_site_label_asym_id_1", String(20), nullable=True),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20), nullable=True),
    Column("atom_site_label_atom_id_2", String(6), nullable=True),
    Column("atom_site_label_comp_id_2", String(10), nullable=True),
    Column("atom_site_label_seq_id_2", Integer, nullable=True),
    Column("atom_site_label_asym_id_2", String(20), nullable=True),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20), nullable=True),
    Column("atom_site_label_atom_id_3", String(6), nullable=True),
    Column("atom_site_label_comp_id_3", String(10), nullable=True),
    Column("atom_site_label_seq_id_3", Integer, nullable=True),
    Column("atom_site_label_asym_id_3", String(20), nullable=True),
    Column("atom_site_auth_asym_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_1", String(6), nullable=True),
    Column("atom_site_auth_comp_id_1", String(20), nullable=True),
    Column("atom_site_auth_seq_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_2", String(6), nullable=True),
    Column("atom_site_auth_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_comp_id_2", String(20), nullable=True),
    Column("atom_site_auth_seq_id_2", String(20), nullable=True),
    Column("atom_site_auth_atom_id_3", String(6), nullable=True),
    Column("atom_site_auth_asym_id_3", String(20), nullable=True),
    Column("atom_site_auth_comp_id_3", String(20), nullable=True),
    Column("atom_site_auth_seq_id_3", String(20), nullable=True),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("value", Float, nullable=True),
    Column("value_esd", Float, nullable=True, default=0.0)
)


pdbx_virtual_bond = Table("pdbx_virtual_bond",
    metadata_obj,
    Column("model_id", Integer, primary_key=True),
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20), nullable=True),
    Column("atom_site_label_atom_id_1", String(6), nullable=True),
    Column("atom_site_label_comp_id_1", String(10), nullable=True),
    Column("atom_site_label_seq_id_1", Integer, nullable=True),
    Column("atom_site_label_asym_id_1", String(20), nullable=True),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20), nullable=True),
    Column("atom_site_label_atom_id_2", String(6), nullable=True),
    Column("atom_site_label_comp_id_2", String(10), nullable=True),
    Column("atom_site_label_seq_id_2", Integer, nullable=True),
    Column("atom_site_label_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_atom_id_1", String(6), nullable=True),
    Column("atom_site_auth_asym_id_1", String(20), nullable=True),
    Column("atom_site_auth_comp_id_1", String(20), nullable=True),
    Column("atom_site_auth_seq_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_2", String(6), nullable=True),
    Column("atom_site_auth_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_comp_id_2", String(20), nullable=True),
    Column("atom_site_auth_seq_id_2", Integer, nullable=True),
    Column("dist", Float, nullable=True),
    Column("dist_esd", Float, nullable=True, default=0.0),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555")
)


pdbx_virtual_torsion = Table("pdbx_virtual_torsion",
    metadata_obj,
    Column("model_id", Integer, primary_key=True),
    Column("atom_site_id_1", String(20), primary_key=True),
    Column("atom_site_label_alt_id_1", String(20), nullable=True),
    Column("atom_site_label_atom_id_1", String(6), nullable=True),
    Column("atom_site_label_comp_id_1", String(10), nullable=True),
    Column("atom_site_label_seq_id_1", Integer, nullable=True),
    Column("atom_site_label_asym_id_1", String(20), nullable=True),
    Column("atom_site_id_2", String(20), primary_key=True),
    Column("atom_site_label_alt_id_2", String(20), nullable=True),
    Column("atom_site_label_atom_id_2", String(6), nullable=True),
    Column("atom_site_label_comp_id_2", String(10), nullable=True),
    Column("atom_site_label_seq_id_2", Integer, nullable=True),
    Column("atom_site_label_asym_id_2", String(20), nullable=True),
    Column("atom_site_id_3", String(20), primary_key=True),
    Column("atom_site_label_alt_id_3", String(20), nullable=True),
    Column("atom_site_label_atom_id_3", String(6), nullable=True),
    Column("atom_site_label_comp_id_3", String(10), nullable=True),
    Column("atom_site_label_seq_id_3", Integer, nullable=True),
    Column("atom_site_label_asym_id_3", String(20), nullable=True),
    Column("atom_site_id_4", String(20), primary_key=True),
    Column("atom_site_label_alt_id_4", String(20), nullable=True),
    Column("atom_site_label_atom_id_4", String(6), nullable=True),
    Column("atom_site_label_comp_id_4", String(10), nullable=True),
    Column("atom_site_label_seq_id_4", Integer, nullable=True),
    Column("atom_site_label_asym_id_4", String(20), nullable=True),
    Column("atom_site_auth_atom_id_1", String(6), nullable=True),
    Column("atom_site_auth_asym_id_1", String(20), nullable=True),
    Column("atom_site_auth_comp_id_1", String(20), nullable=True),
    Column("atom_site_auth_seq_id_1", String(20), nullable=True),
    Column("atom_site_auth_atom_id_2", String(6), nullable=True),
    Column("atom_site_auth_asym_id_2", String(20), nullable=True),
    Column("atom_site_auth_comp_id_2", String(20), nullable=True),
    Column("atom_site_auth_seq_id_2", String(20), nullable=True),
    Column("atom_site_auth_atom_id_3", String(6), nullable=True),
    Column("atom_site_auth_asym_id_3", String(20), nullable=True),
    Column("atom_site_auth_comp_id_3", String(20), nullable=True),
    Column("atom_site_auth_seq_id_3", String(20), nullable=True),
    Column("atom_site_auth_atom_id_4", String(6), nullable=True),
    Column("atom_site_auth_asym_id_4", String(20), nullable=True),
    Column("atom_site_auth_comp_id_4", String(20), nullable=True),
    Column("atom_site_auth_seq_id_4", String(20), nullable=True),
    Column("site_symmetry_1", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_2", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_3", String(10), primary_key=True, default="1_555"),
    Column("site_symmetry_4", String(10), primary_key=True, default="1_555"),
    Column("value", Float, nullable=True),
    Column("value_esd", Float, nullable=True, default=0.0)
)


pdbx_sequence_pattern = Table("pdbx_sequence_pattern",
    metadata_obj,
    Column("label_asym_id", String(20), primary_key=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("pattern_count", Integer),
    Column("sequence_pattern", String(20), primary_key=True)
)


pdbx_stereochemistry = Table("pdbx_stereochemistry",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10)),
    Column("auth_seq_id", String(20)),
    Column("label_seq_id", Integer),
    Column("label_atom_id", String(6)),
    Column("label_alt_id", String(20)),
    Column("label_atom_id_u", String(6)),
    Column("label_alt_id_u", String(20)),
    Column("label_atom_id_v", String(6)),
    Column("label_alt_id_v", String(20)),
    Column("label_atom_id_w", String(6)),
    Column("label_alt_id_w", String(20)),
    Column("volume3", Float),
    Column("angle_out_of_plane", Float)
)


pdbx_rms_devs_covalent = Table("pdbx_rms_devs_covalent",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("rms_bonds", Float),
    Column("num_bonds", Integer),
    Column("rms_bonds_base", Float),
    Column("num_bonds_base", Integer),
    Column("rms_bonds_sugar", Float),
    Column("num_bonds_sugar", Integer),
    Column("rms_bonds_phosphate", Float),
    Column("num_bonds_phosphate", Integer),
    Column("rms_angles", Float),
    Column("num_angles", Integer),
    Column("rms_angles_base", Float),
    Column("num_angles_base", Integer),
    Column("rms_angles_sugar", Float),
    Column("num_angles_sugar", Integer),
    Column("rms_angles_phosphate", Float),
    Column("num_angles_phosphate", Integer)
)


pdbx_rms_devs_cov_by_monomer = Table("pdbx_rms_devs_cov_by_monomer",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10)),
    Column("auth_seq_id", String(20)),
    Column("label_seq_id", Integer),
    Column("rms_bonds", Float),
    Column("num_bonds", Integer),
    Column("rms_angles", Float),
    Column("num_angles", Integer)
)


pdbx_sugar_phosphate_geometry = Table("pdbx_sugar_phosphate_geometry",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", Integer),
    Column("auth_asym_id", String(20), nullable=True),
    Column("label_asym_id", String(20), nullable=True),
    Column("label_comp_id", String(10)),
    Column("auth_seq_id", String(20), nullable=True),
    Column("label_seq_id", Integer),
    Column("neighbor_comp_id_5prime", String(10), nullable=True),
    Column("neighbor_comp_id_3prime", String(10), nullable=True),
    Column("o3_p_o5_c5", Float, nullable=True),
    Column("p_o5_c5_c4", Float, nullable=True),
    Column("o5_c5_c4_c3", Float, nullable=True),
    Column("c5_c4_c3_o3", Float, nullable=True),
    Column("c4_c3_o3_p", Float, nullable=True),
    Column("c3_o3_p_o5", Float, nullable=True),
    Column("c4_o4_c1_n1_9", Float, nullable=True),
    Column("o4_c1_n1_9_c2_4", Float, nullable=True),
    Column("o4_c1_n1_9_c6_8", Float, nullable=True),
    Column("c4_o4_c1_c2", Float, nullable=True),
    Column("o4_c1_c2_c3", Float, nullable=True),
    Column("c1_c2_c3_c4", Float, nullable=True),
    Column("c2_c3_c4_o4", Float, nullable=True),
    Column("c3_c4_o4_c1", Float, nullable=True),
    Column("c5_c4_c3_c2", Float, nullable=True),
    Column("o4_c4_c3_o3", Float, nullable=True),
    Column("o3_c3_c2_o2", Float, nullable=True),
    Column("o5_c5_c4_o4", Float, nullable=True),
    Column("pseudorot", Float, nullable=True),
    Column("maxtorsion", Float, nullable=True),
    Column("next_label_comp_id", String(10), nullable=True),
    Column("next_label_seq_id", Integer, nullable=True),
    Column("next_o3_p_o5_c5", Float, nullable=True),
    Column("next_p_o5_c5_c4", Float, nullable=True),
    Column("next_o5_c5_c4_c3", Float, nullable=True),
    Column("next_c5_c4_c3_o3", Float, nullable=True),
    Column("next_c4_c3_o3_p", Float, nullable=True),
    Column("next_c3_o3_p_o5", Float, nullable=True),
    Column("next_c4_o4_c1_n1_9", Float, nullable=True),
    Column("next_o4_c1_n1_9_c2_4", Float, nullable=True),
    Column("c1_c2", Float, nullable=True),
    Column("c2_c3", Float, nullable=True),
    Column("c3_c4", Float, nullable=True),
    Column("c4_o4", Float, nullable=True),
    Column("o4_c1", Float, nullable=True),
    Column("p_o5", Float, nullable=True),
    Column("o5_c5", Float, nullable=True),
    Column("c5_c4", Float, nullable=True),
    Column("c3_o3", Float, nullable=True),
    Column("o3_p", Float, nullable=True),
    Column("p_o1p", Float, nullable=True),
    Column("p_o2p", Float, nullable=True),
    Column("c1_n9_1", Float, nullable=True),
    Column("n1_c2", Float, nullable=True),
    Column("n1_c6", Float, nullable=True),
    Column("n9_c4", Float, nullable=True),
    Column("n9_c8", Float, nullable=True),
    Column("c1_c2_c3", Float, nullable=True),
    Column("c2_c3_c4", Float, nullable=True),
    Column("c3_c4_o4", Float, nullable=True),
    Column("c4_o4_c1", Float, nullable=True),
    Column("o4_c1_c2", Float, nullable=True),
    Column("p_o5_c5", Float, nullable=True),
    Column("o5_c5_c4", Float, nullable=True),
    Column("c5_c4_c3", Float, nullable=True),
    Column("c4_c3_o3", Float, nullable=True),
    Column("c3_o3_p", Float, nullable=True),
    Column("o3_p_o5", Float, nullable=True),
    Column("o4_c1_n1_9", Float, nullable=True),
    Column("c1_n1_9_c2_4", Float, nullable=True),
    Column("c5_c4_o4", Float, nullable=True),
    Column("c2_c3_o3", Float, nullable=True),
    Column("o1p_p_o2p", Float, nullable=True),
    Column("c2_c1_n1_9", Float, nullable=True),
    Column("c1_n1_9_c6_8", Float, nullable=True)
)


pdbx_nmr_computing = Table("pdbx_nmr_computing",
    metadata_obj,
    Column("entry_id", String(20), primary_key=True),
    Column("collection", String(128), nullable=True),
    Column("collection_version", String(20), nullable=True),
    Column("processing", String(128), nullable=True),
    Column("processing_version", String(20), nullable=True),
    Column("data_analysis", String(128), nullable=True),
    Column("data_analysis_version", String(20), nullable=True),
    Column("structure_solution", String(128), nullable=True),
    Column("structure_solution_version", String(20), nullable=True),
    Column("refinement", String(128), nullable=True),
    Column("refinement_version", String(20), nullable=True),
    Column("iterative_relaxation_matrix", String(128), nullable=True),
    Column("iterative_relaxation_matrix_version", String(20), nullable=True)
)


pdbx_audit_conform_extension = Table("pdbx_audit_conform_extension",
    metadata_obj,
    Column("extension_dict_location", String(255), nullable=True),
    Column("extension_dict_name", String(128), primary_key=True),
    Column("extension_dict_version", String(128), primary_key=True)
)


pdbx_dcc_mapman = Table("pdbx_dcc_mapman",
    metadata_obj,
    Column("pdbid", String(20), primary_key=True),
    Column("details", String(255), nullable=True)
)


pdbx_dcc_rscc_mapman = Table("pdbx_dcc_rscc_mapman",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", String(20), nullable=True),
    Column("pdb_id", String(20), nullable=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_ins_code", String(20), nullable=True),
    Column("correlation", Float, nullable=True),
    Column("real_space_R", Float, nullable=True),
    Column("weighted_real_space_R", Float, nullable=True),
    Column("real_space_Zscore", Float, nullable=True),
    Column("Biso_mean", Float, nullable=True),
    Column("occupancy_mean", Float, nullable=True),
    Column("flag", String(128), nullable=True)
)


pdbx_dcc_rscc_mapman_overall = Table("pdbx_dcc_rscc_mapman_overall",
    metadata_obj,
    Column("pdbid", String(20), primary_key=True),
    Column("correlation", Float, nullable=True),
    Column("correlation_sigma", Float, nullable=True),
    Column("real_space_R", Float, nullable=True),
    Column("real_space_R_sigma", Float, nullable=True)
)


pdbx_dcc_density = Table("pdbx_dcc_density",
    metadata_obj,
    Column("DCC_version", String(128), nullable=True),
    Column("pdbid", String(20), primary_key=True),
    Column("pdbtype", String(128), nullable=True),
    Column("unit_cell", String(128), nullable=True),
    Column("space_group_name_H-M", String(128), nullable=True),
    Column("space_group_pointless", String(128), nullable=True),
    Column("ls_d_res_high", Float, nullable=True),
    Column("ls_d_res_high_sf", Float, nullable=True),
    Column("ls_d_res_low_sf", Float, nullable=True),
    Column("R_value_R_work", Float, nullable=True),
    Column("R_value_R_free", Float, nullable=True),
    Column("working_set_count", Integer, nullable=True),
    Column("free_set_count", Integer, nullable=True),
    Column("occupancy_min", Float, nullable=True),
    Column("occupancy_max", Float, nullable=True),
    Column("occupancy_mean", Float, nullable=True),
    Column("Biso_min", Float, nullable=True),
    Column("Biso_max", Float, nullable=True),
    Column("Biso_mean", Float, nullable=True),
    Column("B_wilson", Float, nullable=True),
    Column("B_wilson_scale", Float, nullable=True),
    Column("mean_I2_over_mean_I_square", Float, nullable=True),
    Column("mean_F_square_over_mean_F2", Float, nullable=True),
    Column("mean_E2_1_abs", Float, nullable=True),
    Column("Padilla-Yeates_L_mean", Float, nullable=True),
    Column("Padilla-Yeates_L2_mean", Float, nullable=True),
    Column("Padilla-Yeates_L2_mean_pointless", Float, nullable=True),
    Column("Z_score_L_test", Float, nullable=True),
    Column("twin_type", String(128), nullable=True),
    Column("twin_operator_xtriage", String(255), nullable=True),
    Column("twin_fraction_xtriage", Float, nullable=True),
    Column("twin_Rfactor", Float, nullable=True),
    Column("I_over_sigI_resh", Float, nullable=True),
    Column("I_over_sigI_diff", Float, nullable=True),
    Column("I_over_sigI_mean", Float, nullable=True),
    Column("ice_ring", String(128), nullable=True),
    Column("anisotropy", Float, nullable=True),
    Column("Z-score", Float, nullable=True),
    Column("prob_peak_value", Float, nullable=True),
    Column("translational_pseudo_symmetry", String(128), nullable=True),
    Column("wavelength", Float, nullable=True),
    Column("B_solvent", Float, nullable=True),
    Column("K_solvent", Float, nullable=True),
    Column("TLS_refinement_reported", String(128), nullable=True),
    Column("partial_B_value_correction_attempted", String(128), nullable=True),
    Column("partial_B_value_correction_success", String(128), nullable=True),
    Column("reflection_status_archived", String(128), nullable=True),
    Column("reflection_status_used", String(128), nullable=True),
    Column("iso_B_value_type", String(128), nullable=True),
    Column("reflns_twin", String(128), nullable=True),
    Column("twin_by_xtriage", String(128), nullable=True),
    Column("twin_operator", String(128), nullable=True),
    Column("twin_fraction", String(128), nullable=True),
    Column("tls_group_number", Integer, nullable=True),
    Column("ncs_group_number", Integer, nullable=True),
    Column("mtrix_number", Integer, nullable=True),
    Column("Matthew_coeff", Float, nullable=True),
    Column("solvent_content", Float, nullable=True),
    Column("Cruickshank_dpi_xyz", Float, nullable=True),
    Column("dpi_free_R", Float, nullable=True),
    Column("fom", Float, nullable=True),
    Column("correlation_overall", Float, nullable=True),
    Column("real_space_R_overall", Float, nullable=True),
    Column("mFo-DFc-3sigma_positive", Integer, nullable=True),
    Column("mFo-DFc-6sigma_positive", Integer, nullable=True),
    Column("mFo-DFc-3sigma_negative", Integer, nullable=True),
    Column("mFo-DFc-6sigma_negative", Integer, nullable=True),
    Column("Bmean-Bwilson", Float, nullable=True),
    Column("Rfree-Rwork", Float, nullable=True),
    Column("error", String(255), nullable=True)
)


pdbx_dcc_geometry = Table("pdbx_dcc_geometry",
    metadata_obj,
    Column("pdbid", String(20), primary_key=True),
    Column("Ramachandran_outlier_percent", Float, nullable=True),
    Column("Ramachandran_outlier_number", Integer, nullable=True),
    Column("Ramachandran_allowed_percent", Float, nullable=True),
    Column("Ramachandran_allowed_number", Integer, nullable=True),
    Column("Ramachandran_favored_percent", Float, nullable=True),
    Column("Ramachandran_favored_number", Integer, nullable=True),
    Column("rotamer_outliers_percent", Float, nullable=True),
    Column("rotamer_outliers_number", Integer, nullable=True),
    Column("cbeta_deviations", Integer, nullable=True),
    Column("all_atom_clashscore", Float, nullable=True),
    Column("overall_score", Float, nullable=True),
    Column("bond_overall_rms", Float, nullable=True),
    Column("bond_overall_max", Float, nullable=True),
    Column("bond_ligand_rms", Float, nullable=True),
    Column("bond_ligand_max", Float, nullable=True),
    Column("angle_overall_rms", Float, nullable=True),
    Column("angle_overall_max", Float, nullable=True),
    Column("angle_ligand_rms", Float, nullable=True),
    Column("angle_ligand_max", Float, nullable=True),
    Column("dihedral_overall_rms", Float, nullable=True),
    Column("dihedral_overall_max", Float, nullable=True),
    Column("chirality_overall_rms", Float, nullable=True),
    Column("chirality_overall_max", Float, nullable=True),
    Column("planarity_overall_rms", Float, nullable=True),
    Column("planarity_overall_max", Float, nullable=True),
    Column("non-bonded_rms", Float, nullable=True)
)


pdbx_dcc_density_corr = Table("pdbx_dcc_density_corr",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("program", String(128), nullable=True),
    Column("ls_d_res_high", Float, nullable=True),
    Column("ls_d_res_low", Float, nullable=True),
    Column("ls_R_factor_R_all", Float, nullable=True),
    Column("ls_R_factor_R_work", Float, nullable=True),
    Column("ls_R_factor_R_free", Float, nullable=True),
    Column("ls_number_reflns_obs", Integer, nullable=True),
    Column("ls_percent_reflns_obs", Float, nullable=True),
    Column("ls_number_reflns_R_free", Integer, nullable=True),
    Column("correlation_coeff_Fo_to_Fc", Float, nullable=True),
    Column("real_space_R", Float, nullable=True),
    Column("correlation", Float, nullable=True),
    Column("details", String(128), nullable=True)
)


pdbx_dcc_map = Table("pdbx_dcc_map",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("model_id", String(20), nullable=True),
    Column("pdb_id", String(20), nullable=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("label_ins_code", String(20), nullable=True),
    Column("RSCC", Float, nullable=True),
    Column("RSR", Float, nullable=True),
    Column("weighted_RSR", Float, nullable=True),
    Column("RSRZ", Float, nullable=True),
    Column("weighted_RSRZ", Float, nullable=True),
    Column("Biso_mean", Float, nullable=True),
    Column("occupancy_mean", Float, nullable=True),
    Column("RSCC_main_chain", Float, nullable=True),
    Column("RSR_main_chain", Float, nullable=True),
    Column("wRSR_main_chain", Float, nullable=True),
    Column("RSRZ_main_chain", Float, nullable=True),
    Column("wRSRZ_main_chain", Float, nullable=True),
    Column("Biso_mean_main_chain", Float, nullable=True),
    Column("occupancy_mean_main_chain", Float, nullable=True),
    Column("RSCC_side_chain", Float, nullable=True),
    Column("RSR_side_chain", Float, nullable=True),
    Column("wRSR_side_chain", Float, nullable=True),
    Column("RSRZ_side_chain", Float, nullable=True),
    Column("wRSRZ_side_chain", Float, nullable=True),
    Column("Biso_mean_side_chain", Float, nullable=True),
    Column("occupancy_mean_side_chain", Float, nullable=True),
    Column("RSCC_phosphate_group", Float, nullable=True),
    Column("RSR_phosphate_group", Float, nullable=True),
    Column("wRSR_phosphate_group", Float, nullable=True),
    Column("RSRZ_phosphate_group", Float, nullable=True),
    Column("wRSRZ_phosphate_group", Float, nullable=True),
    Column("Biso_mean_phosphate_group", Float, nullable=True),
    Column("occupancy_mean_phosphate_group", Float, nullable=True),
    Column("shift", Float, nullable=True),
    Column("shift_main_chain", Float, nullable=True),
    Column("shift_side_chain", Float, nullable=True),
    Column("density_connectivity", Float, nullable=True),
    Column("density_index_main_chain", Float, nullable=True),
    Column("density_index_side_chain", Float, nullable=True),
    Column("RSZD", Float, nullable=True),
    Column("RSZO", Float, nullable=True),
    Column("RSZO_Zscore", Float, nullable=True),
    Column("LLDF", Float, nullable=True),
    Column("RSZD_main_chain", Float, nullable=True),
    Column("RSZO_main_chain", Float, nullable=True),
    Column("RSZD_side_chain", Float, nullable=True),
    Column("RSZO_side_chain", Float, nullable=True),
    Column("RSZD_phosphate_group", Float, nullable=True),
    Column("RSZO_phosphate_group", Float, nullable=True),
    Column("quality_indicator", String(128), nullable=True)
)


pdbx_deposit_group = Table("pdbx_deposit_group",
    metadata_obj,
    Column("group_id", String(20), primary_key=True),
    Column("group_title", String(255), nullable=True),
    Column("group_description", String(255), nullable=True),
    Column("group_type", String(255), nullable=True)
)


pdbx_deposit_group_index = Table("pdbx_deposit_group_index",
    metadata_obj,
    Column("group_id", String(20), primary_key=True),
    Column("ordinal_id", Integer, primary_key=True),
    Column("dep_set_id", String(20), nullable=True),
    Column("pdb_id_code", String(20), nullable=True),
    Column("group_file_name", String(20), nullable=True),
    Column("group_file_timestamp", Date, nullable=True),
    Column("auth_file_label", String(128), nullable=True),
    Column("auth_file_content_type", String(128), nullable=True),
    Column("auth_file_format_type", String(20), nullable=True),
    Column("auth_file_name", String(128), nullable=True),
    Column("auth_file_size", Integer, nullable=True)
)


pdbx_struct_assembly_auth_evidence = Table("pdbx_struct_assembly_auth_evidence",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("assembly_id", String(128), primary_key=True),
    Column("experimental_support", String(128)),
    Column("details", String(255), nullable=True)
)


pdbx_struct_assembly_auth_classification = Table("pdbx_struct_assembly_auth_classification",
    metadata_obj,
    Column("assembly_id", String(128), primary_key=True),
    Column("reason_for_interest", String(128))
)


pdbx_crystal_alignment = Table("pdbx_crystal_alignment",
    metadata_obj,
    Column("crystal_id", String(20), primary_key=True),
    Column("oscillation_range", Float, nullable=True),
    Column("oscillation_start", Float, nullable=True),
    Column("oscillation_end", Float, nullable=True),
    Column("xbeam", Float, nullable=True),
    Column("xbeam_esd", Float, nullable=True),
    Column("ybeam", Float, nullable=True),
    Column("ybeam_esd", Float, nullable=True),
    Column("crysx_spindle", Float, nullable=True),
    Column("crysx_spindle_esd", Float, nullable=True),
    Column("crysy_vertical", Float, nullable=True),
    Column("crysy_vertical_esd", Float, nullable=True),
    Column("crysz_beam", Float, nullable=True),
    Column("crysz_beam_esd", Float, nullable=True),
    Column("crystal_to_detector_distance", Float, nullable=True),
    Column("crystal_to_detector_distance_esd", Float, nullable=True),
    Column("crossfire_x", Float, nullable=True),
    Column("crossfire_x_esd", Float, nullable=True),
    Column("crossfire_y", Float, nullable=True),
    Column("crossfire_y_esd", Float, nullable=True),
    Column("crossfire_xy", Float, nullable=True),
    Column("crossfire_xy_esd", Float, nullable=True),
    Column("overall_beam_divergence", Float, nullable=True),
    Column("overall_beam_divergence_esd", Float, nullable=True)
)


pdbx_audit_revision_history = Table("pdbx_audit_revision_history",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("major_revision", Integer),
    Column("minor_revision", Integer),
    Column("revision_date", DateTime),
    Column("internal_version", Integer, nullable=True),
    Column("internal_deposition_id", String(20), nullable=True)
)


pdbx_audit_revision_group = Table("pdbx_audit_revision_group",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("group", String(128))
)


pdbx_audit_revision_category = Table("pdbx_audit_revision_category",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("category", String(20))
)


pdbx_audit_revision_details = Table("pdbx_audit_revision_details",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("provider", String(128), nullable=True),
    Column("type", String(128), nullable=True),
    Column("description", String(255), nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_audit_revision_item = Table("pdbx_audit_revision_item",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("revision_ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128), primary_key=True),
    Column("item", String(20))
)


pdbx_supporting_exp_data_set = Table("pdbx_supporting_exp_data_set",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("data_content_type", String(128)),
    Column("data_version_major", Integer, nullable=True),
    Column("data_version_minor", Integer, nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_database_doi = Table("pdbx_database_doi",
    metadata_obj,
    Column("db_name", String(10), primary_key=True),
    Column("db_DOI", String(10))
)


pdbx_audit_conform = Table("pdbx_audit_conform",
    metadata_obj,
    Column("dict_location", String(255), nullable=True),
    Column("dict_name", String(255), primary_key=True),
    Column("dict_version", String(255), primary_key=True)
)


pdbx_serial_crystallography_measurement = Table("pdbx_serial_crystallography_measurement",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("pulse_energy", Float, nullable=True),
    Column("pulse_duration", Float, nullable=True),
    Column("xfel_pulse_repetition_rate", Float, nullable=True),
    Column("pulse_photon_energy", Float, nullable=True),
    Column("photons_per_pulse", Float, nullable=True),
    Column("source_size", Float, nullable=True),
    Column("source_distance", Float, nullable=True),
    Column("focal_spot_size", Float, nullable=True),
    Column("collimation", String(255), nullable=True),
    Column("collection_time_total", Float, nullable=True)
)


pdbx_serial_crystallography_sample_delivery = Table("pdbx_serial_crystallography_sample_delivery",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("description", String(255), nullable=True),
    Column("method", String(255))
)


pdbx_serial_crystallography_sample_delivery_injection = Table("pdbx_serial_crystallography_sample_delivery_injection",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("description", String(255), nullable=True),
    Column("injector_diameter", Float, nullable=True),
    Column("injector_temperature", Float, nullable=True),
    Column("injector_pressure", Float, nullable=True),
    Column("flow_rate", Float, nullable=True),
    Column("carrier_solvent", String(255), nullable=True),
    Column("crystal_concentration", Float, nullable=True),
    Column("preparation", String(255), nullable=True),
    Column("power_by", String(255), nullable=True),
    Column("injector_nozzle", String(255), nullable=True),
    Column("jet_diameter", Float, nullable=True),
    Column("filter_size", Float, nullable=True)
)


pdbx_serial_crystallography_sample_delivery_fixed_target = Table("pdbx_serial_crystallography_sample_delivery_fixed_target",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("description", String(255), nullable=True),
    Column("sample_holding", String(255), nullable=True),
    Column("support_base", String(255), nullable=True),
    Column("sample_unit_size", Float, nullable=True),
    Column("crystals_per_unit", Integer, nullable=True),
    Column("sample_solvent", String(255), nullable=True),
    Column("sample_dehydration_prevention", String(128), nullable=True),
    Column("motion_control", String(128), nullable=True),
    Column("velocity_horizontal", Float, nullable=True),
    Column("velocity_vertical", Float, nullable=True),
    Column("details", String(255), nullable=True)
)


pdbx_serial_crystallography_data_reduction = Table("pdbx_serial_crystallography_data_reduction",
    metadata_obj,
    Column("diffrn_id", String(20), primary_key=True),
    Column("frames_total", Integer, nullable=True),
    Column("xfel_pulse_events", Integer, nullable=True),
    Column("frame_hits", Integer, nullable=True),
    Column("crystal_hits", Integer, nullable=True),
    Column("droplet_hits", Integer, nullable=True),
    Column("frames_failed_index", Integer, nullable=True),
    Column("frames_indexed", Integer, nullable=True),
    Column("lattices_indexed", Integer, nullable=True),
    Column("xfel_run_numbers", String(255), nullable=True),
    Column("lattices_merged", Integer, nullable=True)
)


pdbx_audit_support = Table("pdbx_audit_support",
    metadata_obj,
    Column("funding_organization", String(255), nullable=True),
    Column("country", String(128), nullable=True),
    Column("grant_number", String(128), nullable=True),
    Column("details", String(128), nullable=True),
    Column("ordinal", Integer, primary_key=True)
)


pdbx_entity_branch_list = Table("pdbx_entity_branch_list",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("hetero", String(10), nullable=True, default="no"),
    Column("comp_id", String(10), primary_key=True),
    Column("num", Integer, primary_key=True)
)


pdbx_entity_branch_link = Table("pdbx_entity_branch_link",
    metadata_obj,
    Column("link_id", Integer, primary_key=True),
    Column("details", String(255), nullable=True),
    Column("entity_id", String(20)),
    Column("entity_branch_list_num_1", Integer),
    Column("entity_branch_list_num_2", Integer),
    Column("comp_id_1", String(20)),
    Column("comp_id_2", String(20)),
    Column("atom_id_1", String(6)),
    Column("leaving_atom_id_1", String(6)),
    Column("atom_stereo_config_1", String(10), nullable=True, default="N"),
    Column("atom_id_2", String(6)),
    Column("leaving_atom_id_2", String(6)),
    Column("atom_stereo_config_2", String(10), nullable=True, default="N"),
    Column("value_order", String(10), nullable=True, default="sing")
)


pdbx_entity_branch = Table("pdbx_entity_branch",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("type", String(20))
)


pdbx_branch_scheme = Table("pdbx_branch_scheme",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("hetero", String(10), nullable=True, default="no"),
    Column("asym_id", String(20), primary_key=True),
    Column("mon_id", String(10), primary_key=True),
    Column("num", Integer, primary_key=True),
    Column("pdb_asym_id", String(20)),
    Column("pdb_seq_num", String(20)),
    Column("pdb_ins_code", String(20), nullable=True),
    Column("pdb_mon_id", String(20)),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_seq_num", String(20), nullable=True),
    Column("auth_mon_id", String(20), nullable=True)
)


pdbx_chem_comp_related = Table("pdbx_chem_comp_related",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("related_comp_id", String(10), primary_key=True),
    Column("relationship_type", String(128), primary_key=True),
    Column("details", String(255), nullable=True)
)


pdbx_chem_comp_atom_related = Table("pdbx_chem_comp_atom_related",
    metadata_obj,
    Column("comp_id", String(10), primary_key=True),
    Column("related_comp_id", String(10), primary_key=True),
    Column("ordinal", Integer, primary_key=True),
    Column("atom_id", String(6)),
    Column("related_atom_id", String(6), nullable=True),
    Column("related_type", String(128))
)


pdbx_refln_signal_binning = Table("pdbx_refln_signal_binning",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("upper_threshold", Float)
)


pdbx_sifts_xref_db = Table("pdbx_sifts_xref_db",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("seq_id_ordinal", Integer, primary_key=True),
    Column("seq_id", Integer, primary_key=True),
    Column("mon_id", String(10)),
    Column("mon_id_one_letter_code", String(10)),
    Column("unp_res", String(10), nullable=True),
    Column("unp_num", Integer, nullable=True),
    Column("unp_acc", String(128), nullable=True),
    Column("unp_segment_id", Integer, nullable=True),
    Column("unp_instance_id", Integer, nullable=True),
    Column("res_type", String(128), nullable=True),
    Column("observed", String(2)),
    Column("mh_id", Integer, nullable=True),
    Column("xref_db_name", String(20), nullable=True),
    Column("xref_db_acc", String(20), nullable=True),
    Column("xref_domain_name", String(128), nullable=True),
    Column("xref_db_segment_id", Integer, nullable=True),
    Column("xref_db_instance_id", Integer, nullable=True)
)


pdbx_sifts_xref_db_segments = Table("pdbx_sifts_xref_db_segments",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("asym_id", String(20), primary_key=True),
    Column("xref_db", String(128), primary_key=True),
    Column("xref_db_acc", String(20), primary_key=True),
    Column("domain_name", String(128), nullable=True),
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
    Column("unp_start", Integer),
    Column("unp_end", Integer),
    Column("seq_id_start", Integer),
    Column("seq_id_end", Integer),
    Column("best_mapping", String(2)),
    Column("identity", Float)
)


pdbx_data_usage = Table("pdbx_data_usage",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(20)),
    Column("details", String(255)),
    Column("url", String(20), nullable=True),
    Column("name", String(128), nullable=True)
)


pdbx_entity_remapping = Table("pdbx_entity_remapping",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("orig_entity_id", String(20))
)


pdbx_chain_remapping = Table("pdbx_chain_remapping",
    metadata_obj,
    Column("entity_id", String(20), primary_key=True),
    Column("label_asym_id", String(20), primary_key=True),
    Column("auth_asym_id", String(20)),
    Column("orig_label_asym_id", String(20)),
    Column("orig_auth_asym_id", String(20)),
    Column("applied_operations", String(20))
)


pdbx_initial_refinement_model = Table("pdbx_initial_refinement_model",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("entity_id_list", String(255), nullable=True),
    Column("type", String(128)),
    Column("source_name", String(20), nullable=True),
    Column("accession_code", String(128), nullable=True),
    Column("details", String(128), nullable=True)
)


pdbx_investigation = Table("pdbx_investigation",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("type", String(128)),
    Column("resource_name", String(20)),
    Column("resource_accession", String(20)),
    Column("details", String(255), nullable=True)
)


pdbx_chem_comp_pcm = Table("pdbx_chem_comp_pcm",
    metadata_obj,
    Column("pcm_id", Integer, primary_key=True),
    Column("comp_id", String(10)),
    Column("modified_residue_id", String(50), nullable=True),
    Column("type", String(128)),
    Column("category", String(128)),
    Column("position", String(128)),
    Column("polypeptide_position", String(128)),
    Column("comp_id_linking_atom", String(6), nullable=True),
    Column("modified_residue_id_linking_atom", String(6), nullable=True),
    Column("uniprot_specific_ptm_accession", String(20), nullable=True),
    Column("uniprot_generic_ptm_accession", String(20), nullable=True),
    Column("first_instance_model_db_code", String(128), nullable=True)
)


pdbx_modification_feature = Table("pdbx_modification_feature",
    metadata_obj,
    Column("ordinal", Integer, primary_key=True),
    Column("label_comp_id", String(10)),
    Column("label_asym_id", String(20)),
    Column("label_seq_id", Integer, nullable=True),
    Column("label_alt_id", String(20), nullable=True),
    Column("modified_residue_label_comp_id", String(10), nullable=True),
    Column("modified_residue_label_asym_id", String(20), nullable=True),
    Column("modified_residue_label_seq_id", Integer, nullable=True),
    Column("modified_residue_label_alt_id", String(20), nullable=True),
    Column("auth_comp_id", String(20), nullable=True),
    Column("auth_asym_id", String(20), nullable=True),
    Column("auth_seq_id", String(20), nullable=True),
    Column("PDB_ins_code", String(20), nullable=True),
    Column("symmetry", String(10), nullable=True),
    Column("modified_residue_auth_comp_id", String(20), nullable=True),
    Column("modified_residue_auth_asym_id", String(20), nullable=True),
    Column("modified_residue_auth_seq_id", String(20), nullable=True),
    Column("modified_residue_PDB_ins_code", String(20), nullable=True),
    Column("modified_residue_symmetry", String(10), nullable=True),
    Column("comp_id_linking_atom", String(6), nullable=True),
    Column("modified_residue_id_linking_atom", String(6), nullable=True),
    Column("modified_residue_id", String(50), nullable=True),
    Column("ref_pcm_id", Integer, nullable=True),
    Column("ref_comp_id", String(10), nullable=True),
    Column("type", String(128)),
    Column("category", String(128))
)


pdbx_diffrn_batch = Table("pdbx_diffrn_batch",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("diffrn_id", String(20), nullable=True),
    Column("cell_id", String(20), nullable=True),
    Column("wavelength_id", String(20), nullable=True),
    Column("space_group_id", String(20), nullable=True),
    Column("detector_id", String(20), nullable=True, default="1"),
    Column("orientation_id", String(20), nullable=True)
)


pdbx_diffrn_cell = Table("pdbx_diffrn_cell",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("angle_alpha", Float, nullable=True, default=90.0),
    Column("angle_alpha_esd", Float, nullable=True),
    Column("angle_beta", Float, nullable=True, default=90.0),
    Column("angle_beta_esd", Float, nullable=True),
    Column("angle_gamma", Float, nullable=True, default=90.0),
    Column("angle_gamma_esd", Float, nullable=True),
    Column("length_a", Float),
    Column("length_a_esd", Float, nullable=True),
    Column("length_b", Float),
    Column("length_b_esd", Float, nullable=True),
    Column("length_c", Float),
    Column("length_c_esd", Float, nullable=True)
)


pdbx_diffrn_orientation = Table("pdbx_diffrn_orientation",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("matrix[1][1]", Float, nullable=True),
    Column("matrix[1][2]", Float, nullable=True),
    Column("matrix[1][3]", Float, nullable=True),
    Column("matrix[2][1]", Float, nullable=True),
    Column("matrix[2][2]", Float, nullable=True),
    Column("matrix[2][3]", Float, nullable=True),
    Column("matrix[3][1]", Float, nullable=True),
    Column("matrix[3][2]", Float, nullable=True),
    Column("matrix[3][3]", Float, nullable=True),
    Column("type", String(128), nullable=True)
)


pdbx_diffrn_batch_scan = Table("pdbx_diffrn_batch_scan",
    metadata_obj,
    Column("batch_id", String(20), primary_key=True),
    Column("scan_id", String(20))
)


pdbx_diffrn_detector_panel_mapping = Table("pdbx_diffrn_detector_panel_mapping",
    metadata_obj,
    Column("id", String(20), primary_key=True),
    Column("detector_id", String(20), default="1"),
    Column("array_id", String(20), default="1"),
    Column("array_section_id", String(20))
)


diffrn_scan = Table("diffrn_scan",
    metadata_obj,
    Column("date_end", DateTime, nullable=True),
    Column("date_end_estimated", DateTime, nullable=True),
    Column("date_start", DateTime, nullable=True),
    Column("integration_time", Float, nullable=True),
    Column("frame_id_start", String(20)),
    Column("frame_id_end", String(20)),
    Column("frames", Integer, nullable=True),
    Column("time_period", Float, nullable=True),
    Column("time_rstrt_incr", Float, nullable=True)
)


diffrn_scan_axis = Table("diffrn_scan_axis",
    metadata_obj,
    Column("scan_id", String(20), primary_key=True),
    Column("axis_id", String(20), primary_key=True),
    Column("angle_start", Float, nullable=True, default=0.0),
    Column("angle_range", Float, nullable=True, default=0.0),
    Column("angle_increment", Float, nullable=True, default=0.0),
    Column("angle_rstrt_incr", Float, nullable=True, default=0.0),
    Column("displacement_start", Float, nullable=True, default=0.0),
    Column("displacement_range", Float, nullable=True, default=0.0),
    Column("displacement_increment", Float, nullable=True, default=0.0),
    Column("displacement_rstrt_incr", Float, nullable=True, default=0.0),
    Column("reference_angle", Float, nullable=True, default=0.0),
    Column("reference_displacement", Float, nullable=True)
)


diffrn_scan_collection = Table("diffrn_scan_collection",
    metadata_obj,
    Column("details", String(255), nullable=True),
    Column("scan_id", String(20), primary_key=True, nullable=True),
    Column("type", String(255), nullable=True, default="rotation"),
    Column("translation_width", Float, nullable=True, default=0.0)
)


diffrn_scan_frame = Table("diffrn_scan_frame",
    metadata_obj,
    Column("date", DateTime, nullable=True),
    Column("frame_id", String(20), primary_key=True),
    Column("frame_number", Integer, nullable=True),
    Column("integration_time", Float),
    Column("polarizn_Stokes_I", Float, nullable=True, default=1.0),
    Column("scan_id", String(20), primary_key=True),
    Column("time_period", Float, nullable=True),
    Column("time_rstrt_incr", Float, nullable=True)
)


diffrn_scan_frame_axis = Table("diffrn_scan_frame_axis",
    metadata_obj,
    Column("axis_id", String(20), primary_key=True),
    Column("angle", Float, nullable=True, default=0.0),
    Column("angle_increment", Float, nullable=True, default=0.0),
    Column("angle_rstrt_incr", Float, nullable=True, default=0.0),
    Column("displacement", Float, nullable=True, default=0.0),
    Column("displacement_increment", Float, nullable=True, default=0.0),
    Column("displacement_rstrt_incr", Float, nullable=True, default=0.0),
    Column("frame_id", String(20), primary_key=True),
    Column("reference_angle", Float, nullable=True, default=0.0),
    Column("reference_displacement", Float, nullable=True)
)


array_intensities = Table("array_intensities",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, nullable=True, default="1"),
    Column("binary_id", Integer, primary_key=True, nullable=True, default=1),
    Column("details", String(255), nullable=True),
    Column("gain", Float),
    Column("gain_esd", Float),
    Column("linearity", String(20)),
    Column("offset", Float, nullable=True),
    Column("overload", Float, nullable=True),
    Column("pixel_fast_bin_size", Float, nullable=True, default=1.0),
    Column("pixel_slow_bin_size", Float, nullable=True, default=1.0),
    Column("pixel_binning_method", String(20), nullable=True, default="unspecified"),
    Column("scaling", Float, nullable=True),
    Column("undefined_value", Float, nullable=True),
    Column("underload", Float, nullable=True)
)


array_structure = Table("array_structure",
    metadata_obj,
    Column("byte_order", String(10)),
    Column("compression_type", String(10), nullable=True, default="none"),
    Column("compression_type_flag", String(10), nullable=True),
    Column("encoding_type", String(50))
)


array_data = Table("array_data",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, nullable=True, default="1"),
    Column("data", String(255)),
    Column("external_data_id", String(20), nullable=True, default="1"),
    Column("header_contents", String(255), nullable=True),
    Column("header_convention", String(20), nullable=True)
)


array_structure_list = Table("array_structure_list",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, nullable=True, default="1"),
    Column("array_section_id", String(20), nullable=True, default="1"),
    Column("dimension", Integer),
    Column("direction", String(20)),
    Column("precedence", Integer)
)


array_structure_list_axis = Table("array_structure_list_axis",
    metadata_obj,
    Column("axis_id", String(20), primary_key=True),
    Column("axis_set_id", String(20), primary_key=True, nullable=True),
    Column("angle", Float, nullable=True, default=0.0),
    Column("angle_increment", Float, nullable=True, default=0.0),
    Column("displacement", Float, nullable=True, default=0.0),
    Column("fract_displacement", Float, nullable=True, default=0.0),
    Column("displacement_increment", Float, nullable=True, default=0.0),
    Column("fract_displacement_increment", Float, nullable=True, default=0.0),
    Column("angular_pitch", Float, nullable=True, default=0.0),
    Column("radial_pitch", Float, nullable=True, default=0.0),
    Column("reference_angle", Float, nullable=True),
    Column("reference_displacement", Float, nullable=True)
)


array_structure_list_section = Table("array_structure_list_section",
    metadata_obj,
    Column("array_id", String(20), primary_key=True, nullable=True, default="1"),
    Column("end", Integer, nullable=True),
    Column("id", String(20), primary_key=True),
    Column("index", Integer, primary_key=True, nullable=True),
    Column("start", Integer, nullable=True),
    Column("stride", Integer, nullable=True, default=1)
)


diffrn_data_frame = Table("diffrn_data_frame",
    metadata_obj,
    Column("array_id", String(20), nullable=True, default="1"),
    Column("array_section_id", String(20), nullable=True),
    Column("binary_id", Integer, nullable=True, default=1),
    Column("center_fast", Float, nullable=True),
    Column("center_slow", Float, nullable=True),
    Column("center_derived", String(10), nullable=True, default="yes"),
    Column("center_units", String(20), nullable=True),
    Column("detector_element_id", String(20), primary_key=True),
    Column("details", String(255), nullable=True)
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
    Column("reference_center_fast", Float, nullable=True),
    Column("reference_center_slow", Float, nullable=True),
    Column("reference_center_units", String(20), nullable=True)
)


def create_all_tables(engine):
    with engine.connect() as conn:
        with conn.begin():
            metadata_obj.create_all(conn)


def create_tables(engine, categories):
    with engine.connect() as conn:
        with conn.begin():
            for category in categories:
                if category in metadata_obj.tables:
                    metadata_obj.tables[category].create(conn)
