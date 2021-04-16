self.CreateBranch_Templete ={
    'single' : 'ana.tx.createBranch<{0}>                  ("{1}");',\
    'vector' : 'ana.tx.createBranch<vector<{0}>>                  ("{1}");',\
}
self.FillBranch_Templete = {
    'vector':'ana.tx.pushbackToBranch<{0}>("{1}", nt.{2}()[{3}]);',\
    'single':'ana.tx.setBranch<{0}>("{1}", nt.{2});',\
}
self.Variable_Matching_Gen = {
    'pt' : 'GenPart_pt[]',
    'eta' : 'GenPart_eta[]',
    'phi' : 'GenPart_phi[]',
    'mass' : 'GenPart_p4()[].mass()',
    'pdg' : 'GenPart_pdgId()[]',
    'energy' : 'nt.GenPart_p4()[].energy()', 
}
self.CreateBranch = {
    'ana.tx.setBranch': (re.compile(r'ana.tx.setBranch<(\w*)>\((\s*)"(\w*)"') , 'ana.tx.createBranch<{0}>                  ("{1}");'),
    'ana.tx.pushbackToBranch': (re.compile(r'ana.tx.pushbackToBranch<(\w*)>\((\s*)"(\w*)"') , 'ana.tx.createBranch<vector<{0}>>                  ("{1}");'),
}

self.miniAOD = {
    'filename' : {
        'www':'/eos/user/q/qiguo/B2G/1lep/NanoAOD/TestFile/Xvdong/NTuple/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8.root',
#         '':''
    },
}

self.nanoAOD = {
    'filename' : {
        'debug':'/eos/user/q/qiguo/B2G/1lep/NanoAOD/VVVNanoLooper/debug.root',
#         '':''
    },
}

self.fileName = {
    'miniAOD':{
        'www':'/eos/user/q/qiguo/B2G/1lep/NanoAOD/TestFile/Xvdong/NTuple/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8.root',
    },
    'nanoAOD':{
        'debug':'/eos/user/q/qiguo/B2G/1lep/NanoAOD/VVVNanoLooper/debug.root',
    }
}

self.filelabel = {
    'miniAOD' : 'www',
    'nanoAOD' : 'debug'
}


self.Preselection = {
    'event_list' : {
        'common' : [],
        'miniAOD_only' : [],
        'nanoAOD_only' : [],
    },
    'Preselection_cut' : '1Lepton_Preselection'
}

self.treeName = {
    'miniAOD' : 'treeDumper/EDBRCandidates',
    'nanoAOD' : 't'
}

self.vector = {}
self.vector['miniAOD'] = {
    'ptgenwl' : 5,
#     '' : 0,
#     '' : 0,
}
self.vector['nanoAOD'] = {
    'ptgenwl' : 5,
#     '' : 0,
#     '' : 0,
}
self.vector_len = {
    'Common_lep_idxs':0,
}

self.DisplayBranch = {}
self.DisplayBranch['nanoAOD'] = [
    'Common_evt',
    'ptgenwl_0', 'ptgenwl_1', 'ptgenwl_2', 'ptgenwl_3', 'ptgenwl_4',
    'ptlep1', 'etalep1', 'lep', 
    'Common_lep_idxs_num',
    'jetAK8puppi_pt', 'jetAK8puppi_eta', 'jetAK8puppi_pt_2', 'jetAK8puppi_eta_2', 'IDLoose', 'IDLoose_2',
    'Common_lep_p4.fCoordinates.fPt', 'Common_lep_pdgid',
]

self.DisplayBranch['miniAOD'] = [
    'event',
    'ptlep1', 'etalep1', 'lep', 
    'jetAK8puppi_ptJEC', 'jetAK8puppi_ptJEC_2',
    'ptgenwl_0', 'ptgenwl_1', 'ptgenwl_2', 'ptgenwl_3', 'ptgenwl_4',
]

self.Selection['necessary variable'] = {
    'miniAOD':[
        'event','ls','run', 
        'jetAK8puppi_ptJEC', 'jetAK8puppi_ptJEC_2', 
        'ptVlepJEC', 
        'ptgenwl',
        'ptlep1', 'etalep1', 'lep', 
    ],
    'nanoAOD':[
        'Common_evt','Common_lumi','Common_run', 
        'jetAK8puppi_pt', 'jetAK8puppi_eta', 'jetAK8puppi_pt_2', 'jetAK8puppi_eta_2', 'IDLoose', 'IDLoose_2',
        'ptVlep', 
        'ptgenwl',
        '1Lepton_Preselection',
        'Common_lep_idxs', 'Common_lep_p4.fCoordinates.fPt', 'Common_lep_pdgid',
        'ptlep1', 'etalep1', 'lep', 
    ],
    'miniAOD_eventNumber':'event',
    'nanoAOD_eventNumber':'Common_evt',
}


    
self.comparison = {
    '1':('event','Common_evt'),
    '2':('ls','Common_lumi'),
    '3':('run','Common_run'),
}

self.cuts = {
    'cuts_1' : 'Common_lep_idxs_num == 2' ,
    'cuts_2' : 'Common_lep_pdgid_0 == Common_lep_pdgid_1' ,
    'cuts_3' : 'ptlep1 > 55' ,
    'cuts_4' : 'jetAK8puppi_pt > 200' ,
}

self.Rdataframe_to_Pandas_columns = {
    'miniAOD':[
        'event','ls','run', 
        'jetAK8puppi_ptJEC', 'jetAK8puppi_ptJEC_2',  'jetAK8puppi_eta', 'jetAK8puppi_sd', 'jetAK8puppi_dnnDecorrW',
        'ptVlepJEC', 
#         'ptgenwl',
        'ptlep1', 'etalep1', 'lep', 
        'ptgenwl_1', 'ptgenwl_2', 'ptgenwl_3', 
        'ptgengl_1',  'ptgengl_2',
        'cut1',
    ],
    'nanoAOD':[
        'Common_evt','Common_lumi','Common_run', 
        'jetAK8puppi_pt', 'jetAK8puppi_eta', 'jetAK8puppi_pt_2', 'jetAK8puppi_eta_2', 'IDLoose', 'IDLoose_2', 'jetAK8puppi_sd', 'jetAK8puppi_dnnDecorrW',
        'ptVlep', 
        'ptgenwl_1', 'ptgenwl_2', 'ptgenwl_3', 
        'ptgengl_1',  'ptgengl_2',
        'Lepton1_Preselection',
#         'Common_lep_idxs', 'Common_lep_p4.fCoordinates.fPt', 'Common_lep_pdgid',
        'ptlep1', 'etalep1', 'lep', 
        'cut1','cut2', 'cut3', 'cut4', 'cut5',
        'nlepton', 'lep1', 'lep2',# for debug
        'deltaR1', # for debug
    ],
}

self.Rdataframe_newcolumns = {
    'miniAOD' : {
        'cut1' : 'int cut1 = ((nLooseEle+nLooseMu)==1); return cut1;',
#         'ptgenwl_1' : 'sort(ptgenwl, ptgenwl+5, greater<double>()); return ptgenwl[0];',
        # array in the miniAOD file will be read as vector
        'ptgenwl_1' : 'float ptgenwl_1 = -99.; if( ptgenwl.size() > 0){ sort(ptgenwl.begin(), ptgenwl.end(), greater<float>()); ptgenwl_1 =  ptgenwl[0] ; }; return ptgenwl_1;',
        'ptgenwl_2' : 'float ptgenwl_2 = -99.; if( ptgenwl.size() > 1){ sort(ptgenwl.begin(), ptgenwl.end(), greater<float>()); ptgenwl_2 =  ptgenwl[1] ; }; return ptgenwl_2;',
        'ptgenwl_3' : 'float ptgenwl_3 = -99.; if( ptgenwl.size() > 2){ sort(ptgenwl.begin(), ptgenwl.end(), greater<float>()); ptgenwl_3 =  ptgenwl[2] ; }; return ptgenwl_3;',
        'ptgengl_1' : 'float ptgengl_1 = -99.; if( ptgengl.size() > 0){ sort(ptgengl.begin(), ptgengl.end(), greater<float>()); ptgengl_1 =  ptgengl[0] ; }; return ptgengl_1;',
        'ptgengl_2' : 'float ptgengl_2 = -99.; if( ptgengl.size() > 1){ sort(ptgengl.begin(), ptgengl.end(), greater<float>()); ptgengl_2 =  ptgengl[0] ; }; return ptgengl_2;',
#         '':'',
    },
    'nanoAOD' : {
        'ptgenwl_1' : 'float ptgenwl_1 = -99.; if( ptgenwl.size() > 0){ sort(ptgenwl.begin(), ptgenwl.end(), greater<float>()); ptgenwl_1 =  ptgenwl[0] ; }; return ptgenwl_1;',
        'ptgenwl_2' : 'float ptgenwl_2 = -99.; if( ptgenwl.size() > 1){ sort(ptgenwl.begin(), ptgenwl.end(), greater<float>()); ptgenwl_2 =  ptgenwl[1] ; }; return ptgenwl_2;',
        'ptgenwl_3' : 'float ptgenwl_3 = -99.; if( ptgenwl.size() > 2){ sort(ptgenwl.begin(), ptgenwl.end(), greater<float>()); ptgenwl_3 =  ptgenwl[2] ; }; return ptgenwl_3;',
        'ptgengl_1' : 'float ptgengl_1 = -99.; if( ptgengl.size() > 0){ sort(ptgengl.begin(), ptgengl.end(), greater<float>()); ptgengl_1 =  ptgengl[0] ; }; return ptgengl_1;',
        'ptgengl_2' : 'float ptgengl_2 = -99.; if( ptgengl.size() > 1){ sort(ptgengl.begin(), ptgengl.end(), greater<float>()); ptgengl_2 =  ptgengl[0] ; }; return ptgengl_2;',
        'nlepton' : 'int nlepton = Common_lep_idxs.size(); return nlepton;',
        'lep1' : 'int lep1 = -99; if(Common_lep_idxs.size() > 0){ lep1 = Common_lep_pdgid[0];} return lep1;',
        'lep2' : 'int lep2 = -99; if(Common_lep_idxs.size() > 1){ lep2 = Common_lep_pdgid[1];} return lep2;',
        'deltaR1' : 'float deltaR1 = -99.; if(Common_lep_idxs.size() > 0 && jetAK8puppi_pt > 0){ TLorentzVector fatjet,lepton; fatjet.SetPtEtaPhiM(jetAK8puppi_pt,jetAK8puppi_eta,jetAK8puppi_phi,jetAK8puppi_sd); lepton.SetPtEtaPhiM(Common_lep_p4[0].Pt(),Common_lep_p4[0].Eta(),Common_lep_p4[0].Phi(),Common_lep_p4[0].M());deltaR1 = fatjet.DeltaR(lepton);} return deltaR1;',
        'cut1' : 'int cut1 = (Lepton1_Preselection > 0); return cut1;',
        'cut2' : 'int cut2 = (Lepton1_Preselection > 0 && ptlep1 > 55); return cut2;',
        'cut3' : 'int cut3 = (lep1== lep2); return cut3;',
        'cut4' : 'int cut4 = (lep1!= lep2); return cut4;',
        'cut5' : 'int cut5 (Lepton1_Preselection > 0 && jetAK8puppi_pt>200 && ptlep1 > 55 && lep1!= lep2); return cut5',
    },
    # newcolumns should be add in order because one variable may rely on others
    'column_order' : {
        'nanoAOD' : [
            'ptgenwl_1', 'ptgenwl_2', 'ptgenwl_3', 
            'ptgengl_1',  'ptgengl_2',
            'nlepton', 'lep1', 'lep2', 
            'deltaR1', 
            'cut1', 'cut2', 'cut3', 'cut4', 'cut5',
        ],
        'miniAOD' : [
            'ptgenwl_1', 'ptgenwl_2', 'ptgenwl_3', 
            'ptgengl_1',  'ptgengl_2',
            'cut1', 
        ],
    },
}


