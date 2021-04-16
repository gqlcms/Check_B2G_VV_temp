self.columns_for_variables_comparison = { }
# this part is for event num
self.columns_for_variables_comparison['event_0'] = {
        0:{'Common_evt':'event_nanoAOD'},
        1:{'event':'event_miniAOD'}
}
self.columns_for_variables_comparison['event_1'] = {
        0:{'Common_lumi':'lumi_nanoAOD'},
        1:{'ls':'lumi_miniAOD'}
}
self.columns_for_variables_comparison['event_2'] = {
        0:{'Common_run':'run_nanoAOD'},
        1:{'run':'run_miniAOD'}
}

# this part is for lepton
self.columns_for_variables_comparison['lepton_0'] = {
        0:{'ptlep1':'ptlep1_nanoAOD'},
        1:{'ptlep1':'ptlep1_miniAOD'}
}

self.columns_for_variables_comparison['lepton_1'] = {
        0:{'etalep1':'etalep1_nanoAOD'},
        1:{'etalep1':'etalep1_miniAOD'}
}

# this part is for the fatJets
self.columns_for_variables_comparison['fatJets_0'] = {
        0:{'jetAK8puppi_pt':'jetAK8puppi_pt_nanoAOD'},
        1:{'jetAK8puppi_ptJEC':'jetAK8puppi_pt_miniAOD'}
}
self.columns_for_variables_comparison['fatJets_1'] = {
        0:{'jetAK8puppi_eta':'jetAK8puppi_eta_nanoAOD'},
        1:{'jetAK8puppi_eta':'jetAK8puppi_eta_miniAOD'}
}
self.columns_for_variables_comparison['fatJets_2'] = {
        0:{'jetAK8puppi_sd':'jetAK8puppi_sd_nanoAOD'},
        1:{'jetAK8puppi_sd':'jetAK8puppi_sd_miniAOD'}
}
self.columns_for_variables_comparison['fatJets_3'] = {
        0:{'jetAK8puppi_dnnDecorrW':'jetAK8puppi_dnnDecorrW_nanoAOD'},
        1:{'jetAK8puppi_dnnDecorrW':'jetAK8puppi_dnnDecorrW_miniAOD'}
}

# this part if for Gen
self.columns_for_variables_comparison['Gen_0'] = {
        0:{'ptgenwl_1':'ptgenwl_1_nanoAOD'},
        1:{'ptgenwl_1':'ptgenwl_1_miniAOD'}
}
self.columns_for_variables_comparison['Gen_1'] = {
        0:{'ptgenwl_2':'ptgenwl_2_nanoAOD'},
        1:{'ptgenwl_2':'ptgenwl_2_miniAOD'}
}
self.columns_for_variables_comparison['Gen_2'] = {
        0:{'ptgenwl_3':'ptgenwl_3_nanoAOD'},
        1:{'ptgenwl_3':'ptgenwl_3_miniAOD'}
}
self.columns_for_variables_comparison['Gen_3'] = {
        0:{'ptgengl_1':'ptgengl_1_nanoAOD'},
        1:{'ptgengl_1':'ptgengl_1_miniAOD'}
}
self.columns_for_variables_comparison['Gen_4'] = {
        0:{'ptgengl_2':'ptgengl_2_nanoAOD'},
        1:{'ptgengl_2':'ptgengl_2_miniAOD'}
}


self.Variables_for_compare = {}

# this part is for lepton
self.Variables_for_compare['letpon_0'] = {
    'Allow_Difference' : 0.05, # % different 
    'column1' : 'ptlep1_nanoAOD' ,
    'column2' : 'ptlep1_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}
self.Variables_for_compare['letpon_1'] = {
    'Allow_Difference' : 0.05, # % different 
    'column1' : 'etalep1_nanoAOD' ,
    'column2' : 'etalep1_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}

# this part is for fatJets
self.Variables_for_compare['fatJets_0'] = {
    'Allow_Difference' : 0.01, # % different 
    'column1' : 'jetAK8puppi_pt_nanoAOD' ,
    'column2' : 'jetAK8puppi_pt_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}
self.Variables_for_compare['fatJets_1'] = {
    'Allow_Difference' : 0.01, # % different 
    'column1' : 'jetAK8puppi_eta_nanoAOD' ,
    'column2' : 'jetAK8puppi_eta_nanoAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}
self.Variables_for_compare['fatJets_2'] = {
    'Allow_Difference' : 0.05, # % different 
    'column1' : 'jetAK8puppi_sd_nanoAOD' ,
    'column2' : 'jetAK8puppi_sd_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}
self.Variables_for_compare['fatJets_3'] = {
    'Allow_Difference' : 0.1, # % different 
    'column1' : 'jetAK8puppi_dnnDecorrW_nanoAOD' ,
    'column2' : 'jetAK8puppi_dnnDecorrW_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}


# this part is for Gen
self.Variables_for_compare['Gen_0'] = {
    'Allow_Difference' : 0.01, # % different 
    'column1' : 'ptgenwl_1_nanoAOD' ,
    'column2' : 'ptgenwl_1_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}

self.Variables_for_compare['Gen_1'] = {
    'Allow_Difference' : 0.01, # % different 
    'column1' : 'ptgenwl_2_nanoAOD' ,
    'column2' : 'ptgenwl_2_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}

self.Variables_for_compare['Gen_2'] = {
    'Allow_Difference' : 0.01, # % different 
    'column1' : 'ptgenwl_3_nanoAOD' ,
    'column2' : 'ptgenwl_3_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}

self.Variables_for_compare['Gen_3'] = {
    'Allow_Difference' : 0.01, # % different 
    'column1' : 'ptgengl_1_nanoAOD' ,
    'column2' : 'ptgengl_1_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}

self.Variables_for_compare['Gen_4'] = {
    'Allow_Difference' : 0.01, # % different 
    'column1' : 'ptgengl_2_nanoAOD' ,
    'column2' : 'ptgengl_2_miniAOD' ,
    'event_column1' : 'event_nanoAOD' ,
    'event_column2' : 'event_miniAOD' ,
}