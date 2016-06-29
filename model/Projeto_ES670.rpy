I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 49ba43cf-c5df-4d8c-a39f-c46ed211b619;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 1;
			- value = 
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPredefinedPackage";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
				}
			}
		}
	}
	- _name = "Projeto_ES670";
	- _objectCreation = "501734128020161520781650";
	- _umlDependencyID = "2725";
	- _lastID = 28;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Final_Project.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Final_Project";
		- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "FRDM_KL25Z.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "FRDM_KL25Z";
		- _id = GUID 97403057-80a5-4323-8421-7b4a31e27ebf;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 0;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 3;
		- value = 
		{ ISubsystem 
			- fileName = "Final_Project";
			- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
		}
		{ ISubsystem 
			- fileName = "Requirements";
			- _id = GUID 83b232d5-cbf5-48de-bd01-d866eaf248e9;
		}
		{ ISubsystem 
			- fileName = "Sources";
			- _id = GUID e3d05d8d-af84-4ac5-b2b3-3db9ce3b399f;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IDiagram 
			- _id = GUID b199a12f-d6a2-434c-8c28-e03ad146546a;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Requirement";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Size@Child.NameCompartment@Stereotype";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "grid_display";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "ObjectModelGe";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Requirement";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Compartments";
										- _Value = "";
										- _Type = MultiLine;
									}
									{ IProperty 
										- _Name = "RequirementNotation";
										- _Value = "Note_Style";
										- _Type = Enum;
										- _ExtraTypeInfo = "Note_Style,Box_Style";
									}
									{ IProperty 
										- _Name = "ShowAnnotationContents";
										- _Value = "Description";
										- _Type = Enum;
										- _ExtraTypeInfo = "Name,Specification,Description,Label";
									}
									{ IProperty 
										- _Name = "ShowForm";
										- _Value = "Note";
										- _Type = Enum;
										- _ExtraTypeInfo = "Plain,Note,Pushpin";
									}
									{ IProperty 
										- _Name = "ShowName";
										- _Value = "Relative";
										- _Type = Enum;
										- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
									}
									{ IProperty 
										- _Name = "ShowStereotype";
										- _Value = "Label";
										- _Type = Enum;
										- _ExtraTypeInfo = "Label,Bitmap,None";
									}
								}
							}
						}
					}
				}
			}
			- _name = "requirement_diagram";
			- _objectCreation = "501734328020161520779650";
			- _umlDependencyID = "3612";
			- _description = { IDescription 
				- _textRTF = "{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1046{\\fonttbl{\\f0\\fnil\\fcharset0 Arial;}}
\\viewkind4\\uc1\\pard\\fs20 Diagrama de requisitos de sistema do projeto pr\\'e1tico da ES670 \\par
\\par
}";
			}
			- _lastModifiedTime = "6.28.2016::4:33:1";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 2fe99eb3-10f9-42d0-adf7-80beaef157a7;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID b199a12f-d6a2-434c-8c28-e03ad146546a;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 10;
				{ CGIClass 
					- _id = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 0d5184b0-4db2-4cdb-a85e-27b5b9b2898f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 32c27ec7-2ced-47c0-bd63-73a9b3f85834;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "comment_0";
						- _id = GUID 28f0689a-ecff-4bb0-941d-4a8badc4b580;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.568266 0 0 0.0879121 54 31.7363 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID fbc087bd-42f5-463a-89cf-87362a3d0d65;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Italic";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "CONTROL_SPEED";
						- _id = GUID 166aaab7-cf5c-4481-a4d3-665ede382195;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "CONTROL_SPEED";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.308118 0 0 0.115362 29 138.678 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=31%,69%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 957a0848-69a8-4ca6-a987-1a9f43b61b6c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "CONTROL_SETTLING";
						- _id = GUID ac7c8af3-17dd-4d76-b0be-04c3795263c9;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "CONTROL_SETTLING";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.306273 0 0 0.113553 31 277.659 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=34%,66%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 354dfa17-ff97-48f4-bea6-90701b76db18;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HMI_OUTPUT_POSITION";
						- _id = GUID f955129c-5a6e-4c50-b3c4-a546def9576e;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "HMI_OUTPUT_POSITION";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.302583 0 0 0.125393 32 555.695 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID aa2a6d3c-135e-4ecd-9ab5-8bd8722e9a10;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HMI_INPUT_SPEED";
						- _id = GUID 0b53c1e4-b7fc-476c-8788-696ee3c1a74c;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "HMI_INPUT_SPEED";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.307196 0 0 0.110869 384 418.599 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 84fca68f-31da-4052-baef-97ffeea9c672;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HMI_OUTPUT_ACTUATION";
						- _id = GUID eaa58628-4ade-4046-9928-56f257060a65;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "HMI_OUTPUT_ACTUATION";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.307196 0 0 0.111797 382 279.582 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID e044cd3f-2700-4f17-bcbd-c2445107406c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HMI_INPUT_PID";
						- _id = GUID f230e846-fc6a-4648-bf73-e3e8f72330e2;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "HMI_INPUT_PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.304428 0 0 0.122868 382 559.46 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=40%,60%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 44d1d204-0b1f-4fbe-811c-45efc8bed9b6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HMI_OUTPUT_SPEED";
						- _id = GUID 14f38fe2-4ee6-4a1e-950b-e3f37eef0a0a;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "HMI_OUTPUT_SPEED";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.305351 0 0 0.11451 382 140.611 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=48%,52%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID d663e66e-1a42-4ce1-ae6d-936a23238e61;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HARDWARE_VOLTAGE";
						- _id = GUID a4b54609-cfab-4ccc-9983-191f2968bcf3;
					}
					- m_pParent = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
					- m_name = { CGIText 
						- m_str = "HARDWARE_VOLTAGE";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.303506 0 0 0.113553 32 418.659 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 21c3de7b-5b1e-4ece-8aeb-2d905c26c54f;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Final_Project.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Final_Project";
				- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
			}
		}
		{ IDiagram 
			- _id = GUID 604328de-2202-48b3-9d1a-353bbeb75331;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "package_diagram";
			- _objectCreation = "501734528020161520777650";
			- _umlDependencyID = "3127";
			- _lastModifiedTime = "6.28.2016::3:13:20";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 84c7ed09-6a53-4e4a-925b-6e70d2f9ea4a;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 604328de-2202-48b3-9d1a-353bbeb75331;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 35;
				{ CGIClass 
					- _id = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 0d5184b0-4db2-4cdb-a85e-27b5b9b2898f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 58f20f87-53df-4801-9589-c23f9c68ea4e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "comment_21";
						- _id = GUID ff49df2e-66b1-405c-9a1d-efad749c7d2c;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.48524 0 0 0.100733 30 75.6978 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIPackage 
					- _id = GUID 8170eadf-d7c3-4067-af4b-adc22e878882;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Final_Project.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Final_Project";
						- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "Final_Project";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.143914 0 0 0.0894874 30 206.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID ae6ed687-c19d-4d04-a6f4-88d5055596d0;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Requirements.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Requirements";
						- _id = GUID 83b232d5-cbf5-48de-bd01-d866eaf248e9;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "Requirements";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0894874 31 320 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "main.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "main";
						- _id = GUID a9bfd00a-eefd-40b0-8807-d7abb8ac9870;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "main";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0894874 353 342 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID b0d8b494-ac18-4555-9929-1964be7662a2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Sources.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Sources";
						- _id = GUID e3d05d8d-af84-4ac5-b2b3-3db9ce3b399f;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "Sources";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.086881 31 445.768 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "hal.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "hal";
						- _id = GUID bf69319c-0115-404a-8fb0-0dd5c03e27cc;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.0920938 352 457.854 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID d9f6ce42-10cc-45c1-ae79-450517767813;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "mcg";
						- _id = GUID 781104c1-6e40-456c-aac2-977cc9591044;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.091225 747 49.0066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID 6b7739cc-a598-401d-830d-254b806ed666;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "main";
						- _id = GUID 74ce8837-bf60-4cad-a5a6-47bf23345d3f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "main";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b0d8b494-ac18-4555-9929-1964be7662a2;
					- m_sourceType = 'F';
					- m_pTarget = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 288 323 ;
						- m_nHorizontalSpacing = 36;
						- m_nVerticalSpacing = -90;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 300 513  300 390  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1165 774 ;
					- m_TargetPort = 118 536 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 96145601-ef44-42a3-a0cd-dfe483ad3107;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "hal";
						- _id = GUID 3440e3ae-780c-4f0c-8efa-f279198b5a28;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b0d8b494-ac18-4555-9929-1964be7662a2;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 288 496 ;
						- m_nHorizontalSpacing = 22;
						- m_nVerticalSpacing = 18;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 300 513  300 523  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1165 774 ;
					- m_TargetPort = 372 707 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID ae45c99a-ab44-499a-ad2f-af0e869c32a0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "";
						- _name = "Final_Project";
						- _id = GUID 1e839be9-0179-4e83-86d3-67a59cd9d185;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "_Projeto_Pratico";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d9f6ce42-10cc-45c1-ae79-450517767813;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8170eadf-d7c3-4067-af4b-adc22e878882;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 679 79 ;
						- m_nHorizontalSpacing = 109;
						- m_nVerticalSpacing = -205;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 637 90  637 269  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 68 449 ;
					- m_TargetPort = 1084 701 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 55325106-7f69-4ba4-b3b9-5684b5be9ad2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "mcg";
						- _id = GUID 9d0c673b-b29e-4056-894a-7aa51c9f89cb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_sourceType = 'F';
					- m_pTarget = GUID d9f6ce42-10cc-45c1-ae79-450517767813;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1 0 0 1.11111 683 106 ;
						- m_nHorizontalSpacing = 47;
						- m_nVerticalSpacing = -207;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 683 415  683 114  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1205 816 ;
					- m_TargetPort = 34 712 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 5656bff3-39ab-457d-b3c4-8ecdad144322;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "comment_34";
						- _id = GUID 3700625d-bd7c-4fde-a679-6601254455fc;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.210332 0 0 0.0879121 209 579.736 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIInheritance 
					- _id = GUID aee001b5-bc13-40d5-91e4-13c48a77a941;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "mcg";
						- _id = GUID f6a7b9f1-70f4-4ac1-8ba9-b45d22e2813b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_sourceType = 'F';
					- m_pTarget = GUID d9f6ce42-10cc-45c1-ae79-450517767813;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 691 146 ;
						- m_nHorizontalSpacing = 74;
						- m_nVerticalSpacing = -210;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 660 518  660 133  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1171 653 ;
					- m_TargetPort = 11 921 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIPackage 
					- _id = GUID ea247004-7343-46e2-ac4c-b10b30c0de89;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "uart.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "uart";
						- _id = GUID 390aecce-51f2-4698-8566-b75bbe83ec6d;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "uart";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.168586 0 0 0.103388 750 702.874 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID 03819201-b9a6-4211-b300-a2b9b8e3fe29;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "uart_0";
						- _id = GUID 807af86c-513f-4606-94d6-93700b3a3e0b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "uart_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_sourceType = 'F';
					- m_pTarget = GUID ea247004-7343-46e2-ac4c-b10b30c0de89;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 691 799 ;
						- m_nHorizontalSpacing = 74;
						- m_nVerticalSpacing = 172;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 660 518  660 789  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1210 653 ;
					- m_TargetPort = 107 833 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 60669178-aee6-4b0d-a02c-dcf8ff4cf2d4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "uart";
						- _id = GUID f792a8e0-7163-4731-8c8b-0f96374c60ca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "uart";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_sourceType = 'F';
					- m_pTarget = GUID ea247004-7343-46e2-ac4c-b10b30c0de89;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 687 735 ;
						- m_nHorizontalSpacing = 51;
						- m_nVerticalSpacing = 204;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 683 415  683 743  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1216 816 ;
					- m_TargetPort = 12 388 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIPackage 
					- _id = GUID 30a73e0e-c5b2-4ede-9767-671aea3ce0ec;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "controller.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "controller";
						- _id = GUID 646e750e-ef3b-4914-8ac3-e9d6ce4ad79f;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.112945 747 160.199 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID e863d790-3469-483f-9db4-3f2f8a0ce90d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "hmi";
						- _id = GUID b943c6c3-a525-4c75-afa3-a53760c76b26;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "hmi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.108601 748 297.96 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID de388d98-18f7-4347-89a4-1d7ebefb9dec;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "encoder";
						- _id = GUID f0ae7402-b9af-4cd3-b0e0-eea47f903b41;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.111207 749 430.341 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID b434f767-1e09-439c-a6f5-22ed626d0b26;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "driver";
						- _id = GUID d14797a1-62b1-47af-a5cf-3f27b0cdbe1f;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.112076 750 567.351 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID fd491382-1d5d-4cbe-b7cc-67f91eb811eb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "util";
						- _id = GUID f5d6f4c4-ca70-4386-9866-389eed46d9b7;
					}
					- m_pParent = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
					- m_name = { CGIText 
						- m_str = "util";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.107732 751 828.946 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID fcd28c8d-d471-430f-84d8-be227a58d919;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "hmi";
						- _id = GUID f4904ca8-f0cd-4211-b0b7-39479bab44ea;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "hmi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_sourceType = 'F';
					- m_pTarget = GUID e863d790-3469-483f-9db4-3f2f8a0ce90d;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 685 359 ;
						- m_nHorizontalSpacing = 49;
						- m_nVerticalSpacing = -71;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 683 415  683 374  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1177 816 ;
					- m_TargetPort = 68 700 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 6665173c-f572-4127-8804-cd752c70609c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "encoder";
						- _id = GUID cfed128e-4c11-4be9-aff6-77698567400b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_sourceType = 'F';
					- m_pTarget = GUID de388d98-18f7-4347-89a4-1d7ebefb9dec;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 684 473 ;
						- m_nHorizontalSpacing = 35;
						- m_nVerticalSpacing = 43;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 683 415  683 484  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1171 816 ;
					- m_TargetPort = 265 483 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 3059d15e-0afa-46a0-9144-467bea57e621;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "driver";
						- _id = GUID 94af8cc6-9fb6-4553-a99d-36c6be5ceff4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_sourceType = 'F';
					- m_pTarget = GUID b434f767-1e09-439c-a6f5-22ed626d0b26;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 686 609 ;
						- m_nHorizontalSpacing = 50;
						- m_nVerticalSpacing = 135;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 683 415  683 619  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1177 816 ;
					- m_TargetPort = 96 461 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID c46af51c-9e91-4a3c-bb17-774812d65167;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "util_0";
						- _id = GUID 4f42dfae-2a41-4590-bd5c-db86473e074f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "util_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_sourceType = 'F';
					- m_pTarget = GUID fd491382-1d5d-4cbe-b7cc-67f91eb811eb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 688 895 ;
						- m_nHorizontalSpacing = 52;
						- m_nVerticalSpacing = 288;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 683 415  683 908  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1177 816 ;
					- m_TargetPort = 28 734 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 1fcbf4ab-104b-41fe-b50e-ebe3ba1b91b1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "controller";
						- _id = GUID a8ba9bb5-229b-4833-ab9c-7f4865dcb77b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_sourceType = 'F';
					- m_pTarget = GUID 30a73e0e-c5b2-4ede-9767-671aea3ce0ec;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 687 258 ;
						- m_nHorizontalSpacing = 70;
						- m_nVerticalSpacing = -149;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 660 518  660 247  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1193 653 ;
					- m_TargetPort = 0 769 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 09219bcc-dd2e-4abc-a770-40f52f57a7ad;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "encoder";
						- _id = GUID d06e6cd5-f702-47c2-8aac-a6b397b28740;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_sourceType = 'F';
					- m_pTarget = GUID de388d98-18f7-4347-89a4-1d7ebefb9dec;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 686 543 ;
						- m_nHorizontalSpacing = 59;
						- m_nVerticalSpacing = 10;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 660 518  660 530  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1182 653 ;
					- m_TargetPort = 79 896 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 534b9db9-3924-43e5-a3e4-8b4aaaa46adc;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "driver";
						- _id = GUID 49a54130-5580-47fc-ab49-b9e326f1a0d2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_sourceType = 'F';
					- m_pTarget = GUID b434f767-1e09-439c-a6f5-22ed626d0b26;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 690 675 ;
						- m_nHorizontalSpacing = 73;
						- m_nVerticalSpacing = 102;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 660 518  660 665  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1188 653 ;
					- m_TargetPort = 0 871 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 466c2bbb-ce48-498e-98bb-cea034136586;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "util_0";
						- _id = GUID 5b29309b-8393-44e2-a051-a154fd45ab89;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "util_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_sourceType = 'F';
					- m_pTarget = GUID fd491382-1d5d-4cbe-b7cc-67f91eb811eb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 685 937 ;
						- m_nHorizontalSpacing = 68;
						- m_nVerticalSpacing = 244;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 660 518  660 925  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1188 653 ;
					- m_TargetPort = 39 892 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 29f59778-7671-4843-8daa-8b84f8b26a39;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "hmi_0";
						- _id = GUID 9ab12bd4-50da-44c1-a6fd-bd84ea458c9f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "hmi_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3491a290-109b-4bc5-a479-4347de71fd6d;
					- m_sourceType = 'F';
					- m_pTarget = GUID e863d790-3469-483f-9db4-3f2f8a0ce90d;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Folder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 688 404 ;
						- m_nHorizontalSpacing = 71;
						- m_nVerticalSpacing = -67;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 660 518  660 390  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1188 653 ;
					- m_TargetPort = 45 848 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 33ce76ad-d1f7-4dd8-89d5-ef9190b3e415;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "controller_0";
						- _id = GUID 24b07e89-940a-402d-b0bd-b6bed8a9219d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "controller_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da40b410-5e50-466d-9af2-5f16d8833e86;
					- m_sourceType = 'F';
					- m_pTarget = GUID 30a73e0e-c5b2-4ede-9767-671aea3ce0ec;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 680 201 ;
						- m_nHorizontalSpacing = 44;
						- m_nVerticalSpacing = -157;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 683 415  683 210  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1182 816 ;
					- m_TargetPort = 129 441 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 174bf348-23c1-472e-8af0-429bed26ee83;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "";
						- _name = "Final_Project_0";
						- _id = GUID 963562a2-d461-4c46-819e-7a0a397bd47d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Final_Project_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID de388d98-18f7-4347-89a4-1d7ebefb9dec;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8170eadf-d7c3-4067-af4b-adc22e878882;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 684 513 ;
						- m_nHorizontalSpacing = 83;
						- m_nVerticalSpacing = 229;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 637 504  637 269  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 23 662 ;
					- m_TargetPort = 903 701 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 93cf6588-c436-4146-8fcc-ea0134fa5fc3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "";
						- _name = "Final_Project";
						- _id = GUID 9939e89e-8096-4a8b-a3a7-c9c6c6ec52c9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Final_Project";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b434f767-1e09-439c-a6f5-22ed626d0b26;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8170eadf-d7c3-4067-af4b-adc22e878882;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 684 635 ;
						- m_nHorizontalSpacing = 94;
						- m_nVerticalSpacing = 291;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 637 643  637 269  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 158 675 ;
					- m_TargetPort = 1049 701 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 07cbab96-cfe7-4560-a5e3-ba42d14f4b9a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "uart.sbs";
						- _subsystem = "Sources::hal::uart";
						- _class = "";
						- _name = "Final_Project";
						- _id = GUID ada7819e-db0e-4906-ac6c-138bb442baf2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Final_Project";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ea247004-7343-46e2-ac4c-b10b30c0de89;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8170eadf-d7c3-4067-af4b-adc22e878882;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 682 772 ;
						- m_nHorizontalSpacing = 92;
						- m_nVerticalSpacing = 364;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 637 764  637 269  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 326 591 ;
					- m_TargetPort = 1008 701 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 8b281bd3-f1f5-4938-b9c6-5a6107121e5f;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Final_Project.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Final_Project";
				- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
			}
		}
		{ IDiagram 
			- _id = GUID f53d507c-79b1-4f7f-850a-0c96a124e9bd;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 9;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Attribute";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,108,73";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Component";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,276,180";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Object";
								- Properties = { IRPYRawContainer 
									- size = 9;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Underline@Child.NameCompartment@Name";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "PrimitiveOperation";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,108,73";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,90,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Type";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,108,73";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "definition_diagram";
			- _objectCreation = "501734728020161520775650";
			- _umlDependencyID = "3476";
			- _lastModifiedTime = "6.28.2016::19:0:29";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 338e6526-0699-499c-b6b4-93ea64c72097;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID f53d507c-79b1-4f7f-850a-0c96a124e9bd;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 52;
				{ CGIClass 
					- _id = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 0d5184b0-4db2-4cdb-a85e-27b5b9b2898f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 6654c7a7-4f32-4645-a17d-e5044dc8b43a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Comment";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "12";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "comment_14";
						- _id = GUID dec1f94f-1152-46e1-904d-55660096766c;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.346864 0 0 0.100733 1808 242.698 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIClass 
					- _id = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "Attribute,PrimitiveOperation,";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "es670";
						- _id = GUID 24edaf1f-6db0-4e29-bf9d-2cfd75f2e63c;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::main::es670";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.282342 0 0 0.138146 456.436 404.549 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=42%,58%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "es670";
							- _name = "CYCLIC_EXECUTIVE_PERIOD";
							- _id = GUID 21dd1dc6-ce7a-4bcf-a30d-f581e9ee3021;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "es670";
							- _name = "uiFlagNextPeriod";
							- _id = GUID f55eb207-7ee2-4e66-8a88-76b514d000b5;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "es670";
							- _name = "boardInit()";
							- _id = GUID 96ad7817-8150-4f17-ac8c-173f02ad5176;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "es670";
							- _name = "main()";
							- _id = GUID 26278d1f-734c-4aa3-8518-81c21ec1ac06;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "es670";
							- _name = "peripheralInit()";
							- _id = GUID d8b0602d-dffb-46a3-99e3-849d71247762;
						}
					}
				}
				{ CGIClass 
					- _id = GUID bc238bad-ba12-4b6b-9622-2b1ab455cfe0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "MKL25Z4";
						- _id = GUID d32248dd-74d9-479b-b8a9-cc8ac7ccc303;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "MKL25Z4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0799773 0 0 0.0597148 1698.15 294.354 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 2f46c2d8-50fc-4b85-a2de-3ff9893d36e9;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "";
						- _name = "mcg";
						- _id = GUID b328f2a4-36c1-47cd-adc9-e8a711ddaf3e;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::hal::mcg::mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.268178 0 0 0.122104 456.464 267.828 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=66%,34%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "mcg.sbs";
							- _subsystem = "Sources::hal::mcg";
							- _class = "mcg";
							- _name = "OSC0_XTAL_FREQ";
							- _id = GUID bde5aa2f-750f-4a7b-9ec8-a0b78957d180;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "mcg.sbs";
							- _subsystem = "Sources::hal::mcg";
							- _class = "mcg";
							- _name = "RTC_XTAL_FREQ";
							- _id = GUID 07770090-e871-4c14-8f9c-17999343a537;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "mcg.sbs";
							- _subsystem = "Sources::hal::mcg";
							- _class = "mcg";
							- _name = "CLOCK_INIT_CONFIG";
							- _id = GUID 228be423-abba-4b93-8725-604483deeaf4;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "mcg.sbs";
							- _subsystem = "Sources::hal::mcg";
							- _class = "mcg";
							- _name = "mcg_clockInit()";
							- _id = GUID 85d6ea0e-ec1e-4b67-9e57-5ee60ce91e12;
						}
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID cfb1c5e9-f24f-4ed8-b4f5-790a16758987;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Association";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Size@Label.Target_Multiplicity";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "es670";
						- _name = "itsMcg";
						- _id = GUID 367d839a-3117-4267-b43f-953704385a62;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f46c2d8-50fc-4b85-a2de-3ff9893d36e9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 437 533  437 412  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 13 930 ;
					- m_TargetPort = 28 1181 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  18 -9  18 13  -6 13  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 438 518 ;
						- m_nHorizontalSpacing = -2;
						- m_nVerticalSpacing = -4;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID 3d0f2957-76c3-4ec8-961e-c7dde8787a16;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_clock_manager";
						- _id = GUID 08c1aede-ca9f-4ad1-a5c3-258b424cd52a;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.121813 0 0 0.0632799 773.757 288.181 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID b5edeb8c-a413-4194-85c6-9bff4e34b5e7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_port_hal";
						- _id = GUID 1ea38ca5-80a9-4f47-80f1-d13c37181ab9;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0944287 0 0 0.0632798 907.811 289.181 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 4a20bdf7-b9fd-48ff-a38c-191d69ef3a20;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_smc_hal";
						- _id = GUID 82bdbb67-6156-4f36-8fde-ac0769bfa6a1;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_smc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0868744 0 0 0.0632799 1011.83 289.181 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 94b89819-5430-41a4-a819-75b4e194bfe4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Depends";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Size@Label.Stereotype";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "mcg";
						- _name = "fsl_clock_manager";
						- _id = GUID 20d06864-0a83-4569-bfe1-b5bb4c473150;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f46c2d8-50fc-4b85-a2de-3ff9893d36e9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3d0f2957-76c3-4ec8-961e-c7dde8787a16;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 757 407 ;
						- m_nHorizontalSpacing = -8;
						- m_nVerticalSpacing = -24;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 843 415  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 259 1213 ;
					- m_TargetPort = 568 945 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 2d3af4e2-2020-4582-9ad7-1f6a35a0ca87;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Depends";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Size@Label.Stereotype";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "mcg";
						- _name = "fsl_port_hal";
						- _id = GUID f4a0195d-af1f-4e0c-9250-6e7b8ef66e7e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f46c2d8-50fc-4b85-a2de-3ff9893d36e9;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5edeb8c-a413-4194-85c6-9bff4e34b5e7;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 959 407 ;
						- m_nHorizontalSpacing = 137;
						- m_nVerticalSpacing = -24;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 957 416  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 259 1213 ;
					- m_TargetPort = 521 1261 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 5994b199-b0f0-4831-83c3-542130c3da22;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Depends";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "11";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Size@Label.Stereotype";
												- _Value = "11";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "mcg";
						- _name = "fsl_smc_hal";
						- _id = GUID 29241265-3501-4089-8d2b-56201c5087d6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_smc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f46c2d8-50fc-4b85-a2de-3ff9893d36e9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4a20bdf7-b9fd-48ff-a38c-191d69ef3a20;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  63 -9  63 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1061 408 ;
						- m_nHorizontalSpacing = 191;
						- m_nVerticalSpacing = -23;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1054 415  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 259 1213 ;
					- m_TargetPort = 485 1167 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID e68fc81e-ebae-45a8-9710-4ef11e20e051;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal::util";
						- _class = "";
						- _name = "tc_hal";
						- _id = GUID 80e4883c-b27b-44e0-b729-869519879a36;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::hal::util::tc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.497639 0 0 0.0668449 813.005 206.008 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=12%,88%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "util.sbs";
							- _subsystem = "Sources::hal::util";
							- _class = "tc_hal";
							- _name = "installLptmr0(unsigned int,lptmr_callback_t)";
							- _id = GUID 9532ef55-b05c-4166-9c06-c09b69057c0a;
						}
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID c9f3c436-048f-43ac-aa96-4b059e324dac;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "es670";
						- _name = "itsTc_hal";
						- _id = GUID 50b117e2-36f7-4e8d-a8bc-e486287500f5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID e68fc81e-ebae-45a8-9710-4ef11e20e051;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 437 533  437 254  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 13 930 ;
					- m_TargetPort = 8 718 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "";
						- _name = "encoder";
						- _id = GUID 0cd2ce1f-f607-4ee5-8014-e6ddcd5d3fbc;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::hal::encoder::encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.492918 0 0 0.361854 456.014 613.95 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=31%,69%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "ENCODER_MAX_PULSE_COUNT";
							- _id = GUID 73fe5c0d-bad2-480f-a59f-c727ad1bd6e6;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "ENCODER_ACQ_PERIOD_MS";
							- _id = GUID 63455f32-56ff-437c-bf01-c8ca92bfd1d1;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "uiEncoderPulsesPerSecond";
							- _id = GUID 2e5252fd-b10e-49ca-bb57-41a49c514e64;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "iEncoderDirection";
							- _id = GUID 02dfe7d0-c3ed-44a3-b015-f17e97c430f7;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "ENCODER_PULSE_COUNT";
							- _id = GUID fc28ab12-ddab-4f9c-9c99-4142a1936c18;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "uiEncoderPosition";
							- _id = GUID 20960c05-8a96-47b5-9e23-55a85b865774;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 14;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "initEncoder()";
							- _id = GUID bc92d3c2-ccb5-4713-b501-39461ef7fcd4;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "enableCounter()";
							- _id = GUID d80062e2-2409-4350-82ad-12b441592ef8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "disableCounter()";
							- _id = GUID fa321fd8-481b-4afc-8fcc-f75cb1cdb612;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "resetCounter()";
							- _id = GUID 4b7c608a-01ac-4b0d-834b-e4f628475a77;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "enableChOInterrupt()";
							- _id = GUID fd55591b-3760-4d1a-b408-d3b2685fa6f8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "disableChOInterrupt()";
							- _id = GUID 9a97c2c4-aaaa-460a-adca-854c82c4c39d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularVelocityRPM()";
							- _id = GUID 5cc3e5ef-3343-4dfd-bfc2-caed4b0419a0;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularVelocityRad()";
							- _id = GUID 2621c965-c72d-4905-8156-77bdbb0b4606;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularPositionDegree()";
							- _id = GUID 84edff4b-12a6-4ba7-b8ad-d00e939e49f4;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularPositionRad()";
							- _id = GUID fa299620-4add-4ef5-aad9-ed8f56d6a0ce;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getDirection()";
							- _id = GUID 08235fa4-dc56-4b55-b6d8-98e1e98083be;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "ENCODER_CHO_IRQ_HANDLER()";
							- _id = GUID 96ca0020-461c-4f15-a7c3-d7f4c7f5a655;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "takeMeasurement()";
							- _id = GUID b0ee0d38-738b-40be-83e2-d845e3d6f6fc;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularVelocity()";
							- _id = GUID c7c600fa-9d00-4892-9a29-f0e58e3fc88a;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "";
						- _name = "driver";
						- _id = GUID 6d1ecd99-1e58-4719-9111-1d503deeb30b;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::hal::driver::driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.452314 0 0 0.195187 456.096 1081.78 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=26%,74%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "DRIVER_FREQUENCY";
							- _id = GUID 57b3bb4e-39dd-4706-9543-556507b712ae;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "DRIVER_PRESCALER";
							- _id = GUID 066bc244-3eab-4691-8a22-7ecd52e2d356;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 7;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "initDriver()";
							- _id = GUID 51c9a440-f22a-445a-9e55-cd6d7fdcd142;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "disableDriver()";
							- _id = GUID ec23fd2f-9190-405f-a2d2-b34484fe2f34;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "enable_driver()";
							- _id = GUID 4b27493f-8f9e-4323-b270-33c74c18afad;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setChannelADutyCycle(unsigned int)";
							- _id = GUID a2d1e3b2-f30b-4b5a-accb-f8a20649ea1c;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setChannelBDutyCycle(unsigned int)";
							- _id = GUID 687ff029-3b33-494c-8505-f7f463d9d4c1;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setHBridgeDutyCycle(unsigned int)";
							- _id = GUID 8e143082-c5cf-404c-bb33-4a06cb207739;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setDriver(int)";
							- _id = GUID 5c257627-d5ab-4854-8417-178a70b0232f;
						}
					}
				}
				{ CGIClass 
					- _id = GUID ff2ee028-366e-4146-a07b-70267a5ef516;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_debug_console";
						- _id = GUID 8f05cbf7-9821-4d46-8dd7-e280a936a2f0;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_debug_console";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.117092 0 0 0.057041 1108.76 291.234 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=60%,40%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID f4f5df41-a956-4c56-8a03-e80c304ef931;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "controller.sbs";
						- _subsystem = "Sources::hal::controller";
						- _class = "";
						- _name = "controller";
						- _id = GUID fb323a9c-d3b6-4780-8f47-c32f8f60d53f;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::hal::controller::controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.52219 0 0 0.164884 454.957 1313.75 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=13%,87%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "initPID(t_PID_Data)";
							- _id = GUID 617664a2-85f4-4ff2-bbb0-ac568557943d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setMaxSumError(t_PID_Data,double)";
							- _id = GUID d4c9517b-1724-411f-86a0-77771eb9e90b;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setKp(t_PID_Data,double)";
							- _id = GUID b92966d2-73b6-4332-8314-037c78f84680;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setKd(t_PID_Data,double)";
							- _id = GUID e2cc2b45-2db4-4052-8cf3-72f98b7a503d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setKi(t_PID_Data,double)";
							- _id = GUID 7220d655-a616-4653-868f-8d37f2aef2eb;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "PIDupdate(t_PID_Data,double,double)";
							- _id = GUID 0df4bd5b-5ec1-4976-8b5c-368ee1d544e2;
						}
					}
				}
				{ CGIClass 
					- _id = GUID e850b3c9-ea6e-473e-9aea-f90e192a3990;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "target_definitions.sbs";
						- _subsystem = "Sources::hal::target_definitions";
						- _class = "";
						- _name = "target_pins";
						- _id = GUID 74626c5b-12fe-4812-8292-c72f81e79564;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::hal::target_definitions::target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2120;
					- m_transform = 0.468367 0 0 0.842246 1700.06 264.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=99%,1%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 52;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHA_INSTANCE";
							- _id = GUID d0ff23a4-31ff-4466-aff8-d6ef5cf0e2a7;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHA_PIN_NUMBER";
							- _id = GUID df7c4240-a86a-4703-bc94-1b6fd6da5777;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHA_PORT_ALT";
							- _id = GUID ad6932be-c24c-496c-9be0-7129787eafaf;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHA_PORT_BASE";
							- _id = GUID 6a735562-2b0f-48a8-85b1-3254fd9a0019;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHA_PORT_INSTANCE";
							- _id = GUID af26c586-d113-40f4-bbed-3ec69f00325f;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHB_INSTANCE";
							- _id = GUID 492ed8ce-b404-4831-928a-325a74a188af;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHB_PIN_NUMBER";
							- _id = GUID 4a734549-98c6-4acf-8089-9107b2f2f29d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHB_PORT_ALT";
							- _id = GUID 4136237b-bb69-46f4-a1aa-fb68c968405c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHB_PORT_BASE";
							- _id = GUID 6b3ca4b9-1ac7-475f-a3f6-551a1d51d7f1;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_CHB_PORT_INSTANCE";
							- _id = GUID 298a95f8-219a-43fe-bad7-af940bd30cd1;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_EN_GPIO_BASE";
							- _id = GUID 46796fad-bbeb-4a49-9385-1b32b34aef64;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_EN_PIN_NUMBER";
							- _id = GUID 114ad472-400e-408c-bd9e-bf3228f41c0d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_EN_PORT_ALT";
							- _id = GUID e3bde043-1e81-48f8-bb96-348d2dd48089;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_EN_PORT_BASE";
							- _id = GUID d30897ef-ca9c-4a6a-9167-65a4ead0d032;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_EN_PORT_INSTANCE";
							- _id = GUID e18255db-180b-41b8-abaf-b06aab64b662;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_TPM_BASE";
							- _id = GUID f160c292-5c3b-43fb-88bf-e30a44d7250b;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_TPM_INSTANCE";
							- _id = GUID a62cc741-725c-4f0e-a359-c4faf4742e17;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_PIN_NUMBER";
							- _id = GUID 23293b67-00d9-4208-bfbe-4943171a9885;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_PORT_ALT";
							- _id = GUID 48c02a64-ca5d-4647-993a-8ba187241b0a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_PORT_BASE";
							- _id = GUID d00ffe47-989c-45d8-96b4-f85a877fc7c1;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_PORT_INSTANCE";
							- _id = GUID 0557cbcb-6819-44a0-b9f1-d352881077a9;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_TPM_BASE";
							- _id = GUID dc864a75-caf5-4880-bc0b-49734813e168;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_TPM_INSTANCE";
							- _id = GUID 00dbf04e-36a3-4488-9e45-528382dd6464;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHB_PIN_NUMBER";
							- _id = GUID 967bdf0e-d846-444f-bdce-31c8c351b985;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHB_PORT_ALT";
							- _id = GUID 7deec664-f9cd-4dd1-9277-4050f289aef5;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHB_PORT_BASE";
							- _id = GUID 01439b12-adb7-4d9f-9f86-b436e13940c9;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHB_PORT_INSTANCE";
							- _id = GUID 83332b22-fc4f-465b-a071-5f6e0ded667f;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHB_TPM_BASE";
							- _id = GUID 14a6dfa7-ec42-4f48-888b-a6bc58d5659c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHB_TPM_INSTANCE";
							- _id = GUID 71b9cee1-ea59-450d-91a9-1ecd1c02625a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_FTM_CLKIN";
							- _id = GUID c314ae65-c66a-4706-8b10-375663989c79;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHB_FTM_CLKIN";
							- _id = GUID 98d78b5e-19db-4318-94b3-8a4aabfaa184;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHO_PORT_INSTANCE";
							- _id = GUID 51c0b521-a35e-4588-9784-25ad7d6a39b6;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHO_PORT_BASE";
							- _id = GUID 615523e3-de9d-4209-82d0-c058d27f91ec;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHO_PIN_NUMBER";
							- _id = GUID 1274b3e5-157c-4ad0-8866-b9cdf8d0f89c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_IRQ_HANDLER";
							- _id = GUID ca8a9244-ec9b-4eed-949b-395df30ad569;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHO_IRQ_HANDLER";
							- _id = GUID 62d75671-5818-41c9-a286-4b625289eb8c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHO_IRQn";
							- _id = GUID 2112c2d5-112f-4f3e-b4bc-4406b2a70428;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "GPIO_OUTPUT";
							- _id = GUID fdaeb1de-3a3f-454d-adce-e5494756cda6;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "GPIO_INPUT";
							- _id = GUID 16b41642-a395-492a-a700-96c982a1444d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "CONST_2PI";
							- _id = GUID 45dc27c7-e57c-44bc-8730-3dbad1f506fd;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "MAX_MOTOR_VELOCITY_RAD";
							- _id = GUID b965179f-80da-4a28-9357-aab2f151d904;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "CYCLIC_EXECUTIVE_PERIOD";
							- _id = GUID c9cb1317-46cc-4af3-919d-6885c44e0396;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_EN_PIN_DIR";
							- _id = GUID 32c981bd-4da5-4734-bb01-9dc19bb43220;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_CHA_IRQn";
							- _id = GUID 38bde85e-2437-4299-9970-5c5a231e0554;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PORT_INSTANCE";
							- _id = GUID b54e1d1b-4eb4-4ad1-be58-4d066a198215;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PORT_BASE";
							- _id = GUID 56b3e972-507a-4fc8-9b5b-2b7959154eee;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PIN_RX";
							- _id = GUID de983826-697d-4804-a322-a77529bde0b1;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PIN_TX";
							- _id = GUID e5146495-17be-46e9-9356-0a51d13c8ff3;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_INSTANCE";
							- _id = GUID d107e660-ef4d-4195-99c8-9243a42ee542;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_BASE";
							- _id = GUID c5d529e1-3652-424e-bd42-08724a088342;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_BAUD";
							- _id = GUID d1765114-2756-4ca5-994d-76b05f2a396b;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PIN_ALT";
							- _id = GUID 6b81bb5c-0c4d-4ecc-806f-a40d1d9f7303;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 02945d2c-e413-4710-8566-e5c5ed08d0a4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_gpio_hal";
						- _id = GUID eaf96d3b-6e84-4516-8c0c-f3ce97a4d67b;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0783758 0 0 0.0588235 1235.84 290.647 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 2239125a-6c0e-48ed-b523-a592fc9a08d5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_interrupt_manager";
						- _id = GUID b57f139d-e8b1-4031-89ee-0cc10bfebb00;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_interrupt_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133144 0 0 0.057041 1322.73 292.234 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=44%,56%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID f296bdc9-1b1f-4a31-8321-7dcab64c2489;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "9";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_pwm_driver";
						- _id = GUID 28b0b50e-d670-4ee0-bc7a-7962c3756450;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_pwm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0859301 0 0 0.0561497 1529.83 437.527 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 708c2b32-39d4-40cb-acb7-5b4fb84cd264;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_tpm_driver";
						- _id = GUID 12d4b1b6-2ee8-43a3-8b4b-366f6cdb0cdf;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.119924 0 0 0.0552585 1467.76 293.82 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 55e606a5-4d18-4c2a-b8f5-81ef80ee8673;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "fsl_tpm_hal";
						- _id = GUID adc41eed-069a-487b-8384-888b18b15826;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.102927 0 0 0.0579323 1503.79 361.94 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "";
						- _name = "hmi";
						- _id = GUID 0da5d265-2989-4cfe-abe9-0446de8ee4ba;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "Sources::hal::hmi::hmi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.406988 0 0 0.103387 456.186 575.986 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=17%,83%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "initHmi()";
							- _id = GUID b158ff24-e0e1-4554-9b1d-ac5ce67b2eee;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "receive()";
							- _id = GUID c84a1a4d-56d7-487f-a2ab-35824975c900;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "transmit(double,double,double)";
							- _id = GUID 1f61e0bc-6ec8-4980-b526-f7e0ca306d1f;
						}
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID b282a89d-2f19-4bb9-9c67-2800c154737b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "es670";
						- _name = "itsEncoder";
						- _id = GUID 330291ad-95f6-446b-a5c4-bd51bcae0deb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 437 533  437 850  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 9 930 ;
					- m_TargetPort = 16 652 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  14 -9  14 9  -6 9  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 443 834 ;
						- m_nVerticalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID bb0f8bf6-bb52-44fa-80b6-6029f1a1d64a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "es670";
						- _name = "itsDriver";
						- _id = GUID d9a9d8f1-081b-415a-96f6-3e69c4012f48;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 437 533  437 1248  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = -2 930 ;
					- m_TargetPort = 13 852 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  14 -9  14 9  -6 9  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 441 1130 ;
						- m_nHorizontalSpacing = -1;
						- m_nVerticalSpacing = -11;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 8b36c4f6-374d-4b71-9d55-261fe0fbade2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "es670";
						- _name = "itsController";
						- _id = GUID 2c1fbab4-fc7f-41de-93b4-68c5b7f55fd0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID f4f5df41-a956-4c56-8a03-e80c304ef931;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 437 533  437 1444  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 6 930 ;
					- m_TargetPort = 12 790 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  14 -9  14 9  -6 9  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 442 1356 ;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 094ade1d-1fbc-4612-a1a5-328e03ad0332;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "es670";
						- _name = "itsHmi";
						- _id = GUID c037dc25-5567-42ec-8154-86d30d765d6f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 437 533  437 681  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 9 930 ;
					- m_TargetPort = 2 1016 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  14 -9  14 9  -6 9  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 440 1509 ;
						- m_nHorizontalSpacing = -2;
						- m_nVerticalSpacing = -2;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIInheritance 
					- _id = GUID 3b0926ed-b21d-4fff-937b-80d9838643da;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_clock_manager";
						- _id = GUID dd83798d-5190-4f23-8bc7-0b4066a59003;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3d0f2957-76c3-4ec8-961e-c7dde8787a16;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 794 584 ;
						- m_nHorizontalSpacing = -21;
						- m_nVerticalSpacing = 78;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 987 958 ;
					- m_TargetPort = 692 1388 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID bd37e241-eb14-42b3-84ca-f84ee0b30979;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_port_hal";
						- _id = GUID a6bfb4e7-53c3-4ab6-b15e-be34a1a60d36;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5edeb8c-a413-4194-85c6-9bff4e34b5e7;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 866 583 ;
						- m_nHorizontalSpacing = -17;
						- m_nVerticalSpacing = 20;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 926 675  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1049 958 ;
					- m_TargetPort = 193 1261 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 30e123ad-9ddc-405a-9976-42aeef457e06;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_smc_hal";
						- _id = GUID 71ec37c4-eb43-48f5-bb55-42f0c364ffe0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_smc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4a20bdf7-b9fd-48ff-a38c-191d69ef3a20;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 952 581 ;
						- m_nHorizontalSpacing = -37;
						- m_nVerticalSpacing = -41;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1032 675  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1054 958 ;
					- m_TargetPort = 232 1340 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4f634468-8e21-4519-82d1-63d22873e889;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_debug_console";
						- _id = GUID 56127ab3-2c53-4ef0-8917-730fa33eca2a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_debug_console";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- m_sourceType = 'F';
					- m_pTarget = GUID ff2ee028-366e-4146-a07b-70267a5ef516;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1118 585 ;
						- m_nHorizontalSpacing = -7;
						- m_nVerticalSpacing = -105;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1170 675  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1044 958 ;
					- m_TargetPort = 523 1188 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 13963142-407a-4ed7-819b-a2a6496ede83;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "stdlib";
						- _id = GUID 579689f1-435b-460b-9240-949970fdee53;
					}
					- m_pParent = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
					- m_name = { CGIText 
						- m_str = "stdlib";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0793201 0 0 0.0579323 1601.84 292.94 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 02dabf70-0b3e-4a53-a6cc-f5f4d35feb4e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_clock_manager";
						- _id = GUID 0d3edbc4-5bd4-425d-b32f-cbd694b2ae6c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3d0f2957-76c3-4ec8-961e-c7dde8787a16;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 904 730 ;
						- m_nHorizontalSpacing = 42;
						- m_nVerticalSpacing = 151;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 895 343 ;
					- m_TargetPort = 1012 1103 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 6a04335d-0a8a-4838-a952-74195c36657c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_port_hal";
						- _id = GUID 0015dbc8-8d6e-4337-934d-d07dcf456a9d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5edeb8c-a413-4194-85c6-9bff4e34b5e7;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 952 725 ;
						- m_nHorizontalSpacing = 48;
						- m_nVerticalSpacing = 150;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 996 335 ;
					- m_TargetPort = 415 1277 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b516ea47-f086-41c9-9d62-4e4276512487;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_gpio_hal";
						- _id = GUID a082384f-6397-45e0-a051-6516d7197ad4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 02945d2c-e413-4710-8566-e5c5ed08d0a4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1221 922 ;
						- m_nHorizontalSpacing = -21;
						- m_nVerticalSpacing = 56;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1285 959  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1049 954 ;
					- m_TargetPort = 627 1315 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 77d57c8a-9948-402b-9c0f-f5580c2c2601;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_interrupt_manager";
						- _id = GUID 35852667-21a0-4dc3-b2ae-1cd8f77c377e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_interrupt_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2239125a-6c0e-48ed-b523-a592fc9a08d5;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1345 920 ;
						- m_nHorizontalSpacing = -17;
						- m_nVerticalSpacing = -10;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1405 959  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1057 954 ;
					- m_TargetPort = 618 1433 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID c7f9b8e6-4a20-422e-91ee-e0f25b780220;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_tpm_driver";
						- _id = GUID 1bc53f19-2516-46bd-af2a-455a65c09c96;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 708c2b32-39d4-40cb-acb7-5b4fb84cd264;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1419 919 ;
						- m_nHorizontalSpacing = -19;
						- m_nVerticalSpacing = -55;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1476 959  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1049 954 ;
					- m_TargetPort = 69 1198 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 2d2a1890-34a3-4924-9f33-f3fe6b9b04c4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_tpm_hal";
						- _id = GUID 199ce57f-e9b0-47fe-9457-63c5d062e2aa;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 55e606a5-4d18-4c2a-b8f5-81ef80ee8673;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1522 920 ;
						- m_nHorizontalSpacing = 98;
						- m_nVerticalSpacing = -54;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1510 959  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1049 954 ;
					- m_TargetPort = 60 968 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 185da7ac-ecac-4f00-a83d-4622f2b7af0d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "target_pins";
						- _id = GUID cfd3b46f-da50-4123-b330-e5c788768332;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a0012a51-9ebe-457d-b917-c05271d4707c;
					- m_sourceType = 'F';
					- m_pTarget = GUID e850b3c9-ea6e-473e-9aea-f90e192a3990;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1638 948 ;
						- m_nHorizontalSpacing = 362;
						- m_nVerticalSpacing = -26;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1049 954 ;
					- m_TargetPort = 151 824 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 08cc6852-39bb-4909-8e6d-acd8dbebe421;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "target_pins";
						- _id = GUID 7c148855-6fcc-4de3-b49a-84d6b6ddd766;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- m_sourceType = 'F';
					- m_pTarget = GUID e850b3c9-ea6e-473e-9aea-f90e192a3990;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1635 1262 ;
						- m_nHorizontalSpacing = 383;
						- m_nVerticalSpacing = -31;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1021 1005 ;
					- m_TargetPort = 388 1203 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID a475d822-22fa-421e-a754-8e0e40afed76;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_gpio_hal";
						- _id = GUID d700ca62-390e-40f2-983a-255eca9b9ac5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 02945d2c-e413-4710-8566-e5c5ed08d0a4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1260 1235 ;
						- m_nHorizontalSpacing = -19;
						- m_nVerticalSpacing = 156;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1292 1278  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1048 1005 ;
					- m_TargetPort = 717 1332 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b33cb811-ed1d-48b9-8dd3-2c279b2a6479;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_interrupt_manager";
						- _id = GUID 36827d06-7831-4455-9390-a4083ac0f37e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_interrupt_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2239125a-6c0e-48ed-b523-a592fc9a08d5;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1350 1224 ;
						- m_nHorizontalSpacing = -20;
						- m_nVerticalSpacing = 90;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1413 1278  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1048 1005 ;
					- m_TargetPort = 678 1223 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 883455ba-58d9-4668-ae76-ec1b3f6b60a8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_tpm_driver";
						- _id = GUID 8c425c7b-8068-44b6-aabe-3a9106eb3a33;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 708c2b32-39d4-40cb-acb7-5b4fb84cd264;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1423 1220 ;
						- m_nHorizontalSpacing = -17;
						- m_nVerticalSpacing = 50;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1483 1278  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1041 1005 ;
					- m_TargetPort = 127 1342 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 95ebf757-761a-4347-8120-b620ac4661ac;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_tpm_hal";
						- _id = GUID e9d90fd1-e31c-4e51-9517-c6eb5bb1d0f0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 55e606a5-4d18-4c2a-b8f5-81ef80ee8673;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1493 1186 ;
						- m_nHorizontalSpacing = 18;
						- m_nVerticalSpacing = -42;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1518 1278  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1041 1005 ;
					- m_TargetPort = 138 1278 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 8cab812f-685b-4010-8cb9-42e7f41a77dd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_pwm_driver";
						- _id = GUID fdb21b84-ef6c-494e-8917-7ce02a1dea0c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_pwm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7c6aaf8e-2742-4e48-9574-69fb9d0a309a;
					- m_sourceType = 'F';
					- m_pTarget = GUID f296bdc9-1b1f-4a31-8321-7dcab64c2489;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1521 1232 ;
						- m_nHorizontalSpacing = -15;
						- m_nVerticalSpacing = -61;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1577 1278  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1039 1005 ;
					- m_TargetPort = 549 1380 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 80614ad5-f78d-43a2-bfab-067b5664462f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "target_pins";
						- _id = GUID 4075bc96-76e9-42e7-8839-b1857807818f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- m_sourceType = 'F';
					- m_pTarget = GUID e850b3c9-ea6e-473e-9aea-f90e192a3990;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1635 659 ;
						- m_nHorizontalSpacing = 419;
						- m_nVerticalSpacing = -31;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1032 958 ;
					- m_TargetPort = 169 487 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 69bdc20a-7606-4430-9802-083935e38c5b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "controller";
						- _id = GUID d8656b20-861f-489f-9d63-3286312721ca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ac8778fe-6638-4df1-b59a-e0fdb340d07f;
					- m_sourceType = 'F';
					- m_pTarget = GUID f4f5df41-a956-4c56-8a03-e80c304ef931;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1115 1465 ;
						- m_nHorizontalSpacing = 56;
						- m_nVerticalSpacing = 520;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1102 675  1102 1470  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1049 958 ;
					- m_TargetPort = 1048 948 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b95e7444-3115-42fd-b0bf-04a7d0560324;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "controller.sbs";
						- _subsystem = "Sources::hal::controller";
						- _class = "controller";
						- _name = "stdlib";
						- _id = GUID 45ee7074-52e4-407a-8e80-289d5bd15701;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "stdlib";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID f4f5df41-a956-4c56-8a03-e80c304ef931;
					- m_sourceType = 'F';
					- m_pTarget = GUID 13963142-407a-4ed7-819b-a2a6496ede83;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1716 1502 ;
						- m_nHorizontalSpacing = -16;
						- m_nVerticalSpacing = 77;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1632 1529  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1040 1305 ;
					- m_TargetPort = 380 1296 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4d114f07-98b7-4711-b491-cb0d99d82333;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "es670";
						- _name = "target_pins";
						- _id = GUID 2f5cdd95-ede5-4c33-8525-7d2880f9066b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74124fb5-979b-4e9a-8b0e-3c0cafd61e28;
					- m_sourceType = 'F';
					- m_pTarget = GUID e850b3c9-ea6e-473e-9aea-f90e192a3990;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1636 584 ;
						- m_nHorizontalSpacing = 483;
						- m_nVerticalSpacing = -30;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 997 1408 ;
					- m_TargetPort = 62 397 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID cdeb20ee-25e2-4970-a921-84c4eb6e4ccb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "target_definitions.sbs";
						- _subsystem = "Sources::hal::target_definitions";
						- _class = "target_pins";
						- _name = "MKL25Z4";
						- _id = GUID 4c2b9253-e39f-4552-85b3-34068094d243;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "MKL25Z4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID e850b3c9-ea6e-473e-9aea-f90e192a3990;
					- m_sourceType = 'F';
					- m_pTarget = GUID bc238bad-ba12-4b6b-9622-2b1ab455cfe0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1755 466 ;
						- m_nHorizontalSpacing = 54;
						- m_nVerticalSpacing = -4;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 94 329 ;
					- m_TargetPort = 573 1116 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID cbe743a9-93d8-4b8d-93fe-5a38658f4c13;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Final_Project.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Final_Project";
				- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
			}
		}
		{ IDiagram 
			- _id = GUID faa5f56b-4d52-441e-886b-10954aeebd61;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 9;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,26,84,168";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Component";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,276,180";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Constraint";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Flow";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Note";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Object";
								- Properties = { IRPYRawContainer 
									- size = 9;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Underline@Child.NameCompartment@Name";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Port";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,68,73";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "systemwide_diagram";
			- _objectCreation = "501734928020161520773650";
			- _umlDependencyID = "3513";
			- _lastModifiedTime = "6.28.2016::18:58:24";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 5ccbc7d1-7b7f-4929-a403-7d2cf765299f;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID faa5f56b-4d52-441e-886b-10954aeebd61;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 26;
				{ CGIClass 
					- _id = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 0d5184b0-4db2-4cdb-a85e-27b5b9b2898f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIComponent 
					- _id = GUID fbc1281d-d90b-4f58-821a-a4f342b7e860;
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Driver.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Driver";
						- _id = GUID 213206af-015c-41b0-acff-d119203c9abf;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "Driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.233503 0 0 0.147905 523.766 242.852 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 2d47c49f-f744-49ff-b411-e3a36b9d8ac2;
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Encoder.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Encoder";
						- _id = GUID ebbcc1e1-fba1-4c18-b67f-93b3441ed079;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "Encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.233503 0 0 0.147905 58.766 504.852 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 1c196ad4-0034-4193-bdf6-85b2c7edbc75;
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Motor.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Motor";
						- _id = GUID 74ce5ee9-edd0-4a4d-a765-5319cad6aa8e;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "Motor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.233503 0 0 0.147905 59.767 243.852 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 90eb0133-fa98-4775-a41a-c064c93f88db;
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "FRDM_KL25Z.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "FRDM_KL25Z";
						- _id = GUID 97403057-80a5-4323-8421-7b4a31e27ebf;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "FRDM_KL25Z";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.233503 0 0 0.147905 1053.77 244.852 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInformationFlow 
					- _id = GUID 04bda125-9b65-4286-b1c5-88f25e668aaa;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "Driver_Motor";
						- _id = GUID e34bdf4e-b250-4c45-8ab6-acb9ecc5150e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fbc1281d-d90b-4f58-821a-a4f342b7e860;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1c196ad4-0034-4193-bdf6-85b2c7edbc75;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 52 643 ;
					- m_TargetPort = 947 637 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Power_PWM";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -24 -8  70 -8  70 10  -24 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 447 326 ;
						- m_nHorizontalSpacing = -40;
						- m_nVerticalSpacing = 4;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 04a7f6c2-b251-49b7-a207-50cbb9902a49;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "Motor_Encoder";
						- _id = GUID 60f917c2-258e-486c-a3d4-611803d6f9ee;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1c196ad4-0034-4193-bdf6-85b2c7edbc75;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2d47c49f-f744-49ff-b411-e3a36b9d8ac2;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 549 1191 ;
					- m_TargetPort = 553 271 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Rotation";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  61 -9  61 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 200 466 ;
						- m_nHorizontalSpacing = -9;
						- m_nVerticalSpacing = 1;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 76440685-2ad1-434f-86eb-ee519cde9b05;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "FRDM_KL25Z_Driver";
						- _id = GUID 94c40593-55ff-463d-92ff-bb88af890914;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 90eb0133-fa98-4775-a41a-c064c93f88db;
					- m_sourceType = 'F';
					- m_pTarget = GUID fbc1281d-d90b-4f58-821a-a4f342b7e860;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 27 623 ;
					- m_TargetPort = 1114 637 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Control_Signals";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -48 -7  67 -7  67 11  -48 11  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 863 315 ;
						- m_nHorizontalSpacing = -48;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID c47c5caf-c929-4bd7-ae63-5ff22cf1581b;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "Encoder_FRDM_KL25Z";
						- _id = GUID 53c0c05d-2321-4e0c-8ffe-ad98ef373f5b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2d47c49f-f744-49ff-b411-e3a36b9d8ac2;
					- m_sourceType = 'F';
					- m_pTarget = GUID 90eb0133-fa98-4775-a41a-c064c93f88db;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1186 611  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1162 718 ;
					- m_TargetPort = 566 1211 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 763 631 ;
						- m_nHorizontalSpacing = -37;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Encoder_Signals";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -55 -8  67 -8  67 10  -55 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 783 599 ;
						- m_nHorizontalSpacing = -93;
						- m_nVerticalSpacing = 4;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIAnnotation 
					- _id = GUID 47d3a7df-1e58-4433-9f41-df814f853e21;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "comment_44";
						- _id = GUID 448c9640-463c-4cad-bc6b-2becd6cef306;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.501845 0 0 0.0531136 450 102.841 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 91e9d5eb-db78-4ac9-9837-a8382d1e8ace;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "User";
						- _id = GUID b67ae536-8378-4891-accd-8a8599ea6dfb;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 509.89 771.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAnnotation 
					- _id = GUID d2ebf246-7f54-46e9-967a-41d97dc7c283;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "Encoder signals:
Channel A
Channel B
Channel O";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.140221 0 0 0.0629562 747 638.811 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 152ec107-28c0-44e4-a4a7-05751ef0632f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "Driver control signals:
PWM channel A
PWM channel B
Enable signal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.140221 0 0 0.0629562 857 369.811 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 62b18e39-aec7-46cd-8ca6-30e668e2d9e7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "User defined parameters:
Angular velocity
Settling time
Direction of rotation

Output:
Current angular velocity
Current angular position";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.156826 0 0 0.130474 639 895.608 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 664439ad-1ec8-4c1f-8c41-6c397b20d909;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "12V bipolar PWM";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.140221 0 0 0.0456204 358 369.863 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 4052e1e4-20e6-48e8-bd46-2721c07dd6cc;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "Direct coupling of motor shaft and encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.140221 0 0 0.0456204 251 438.863 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIComponent 
					- _id = GUID 2468f9a0-2e13-4c4e-83ab-9968a7a53c96;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "PowerSupply_12V.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "PowerSupply_12V";
						- _id = GUID 88a7a51b-355c-4870-906d-9393f79cf1fe;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "PowerSupply_12V";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.117597 0 0 0.0616269 134.882 122.938 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInformationFlow 
					- _id = GUID 1022599e-fa25-4fbb-90a9-77c6dcb671e3;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "PowerSupply_12V_Motor";
						- _id = GUID 84b25fa3-7939-4aa2-a6fc-68b9e4c953c9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2468f9a0-2e13-4c4e-83ab-9968a7a53c96;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1c196ad4-0034-4193-bdf6-85b2c7edbc75;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 503 1121 ;
					- m_TargetPort = 575 258 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 149 221 ;
						- m_nHorizontalSpacing = -4;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 88b9a65e-fcbe-4500-b106-65a44ee63f0c;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "PowerSupply_12V_Encoder";
						- _id = GUID dd28681f-2189-4849-a59e-c38dfa979705;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2468f9a0-2e13-4c4e-83ab-9968a7a53c96;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2d47c49f-f744-49ff-b411-e3a36b9d8ac2;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 24 172  24 599  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 44 796 ;
					- m_TargetPort = 14 637 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 70 185 ;
						- m_nHorizontalSpacing = 87;
						- m_nVerticalSpacing = -162;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID bfdaf0d8-3103-4a5d-b1fe-eb564791c718;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "PowerSupply_12V_Driver";
						- _id = GUID 50121778-5d84-451e-a9fc-1594114a67b4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2468f9a0-2e13-4c4e-83ab-9968a7a53c96;
					- m_sourceType = 'F';
					- m_pTarget = GUID fbc1281d-d90b-4f58-821a-a4f342b7e860;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 620 176  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1132 861 ;
					- m_TargetPort = 412 42 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 288 187 ;
						- m_nHorizontalSpacing = -173;
						- m_nVerticalSpacing = -9;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID dc42e814-c6ab-4aaf-8b28-106af0d179c3;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "PowerSupply_12V_FRDM_KL25Z";
						- _id = GUID f44604c7-22aa-4bde-ae16-3fca4b60902d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2468f9a0-2e13-4c4e-83ab-9968a7a53c96;
					- m_sourceType = 'F';
					- m_pTarget = GUID 90eb0133-fa98-4775-a41a-c064c93f88db;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1187 176  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1081 861 ;
					- m_TargetPort = 571 15 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 840 187 ;
						- m_nHorizontalSpacing = 91;
						- m_nVerticalSpacing = -9;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIComponent 
					- _id = GUID fcab19b3-848d-444f-80b5-333f2f521445;
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Host_Interface.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Host_Interface";
						- _id = GUID 0e52124a-e789-4058-8ffe-313e31fb1a1a;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "Host_Interface";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.233503 0 0 0.147905 886.766 787.852 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInformationFlow 
					- _id = GUID 8038d258-2d54-41a8-b828-39844d2b18aa;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "User_Host_Interface";
						- _id = GUID 2db5fbe9-d116-496a-a12b-176d252462a9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 91e9d5eb-db78-4ac9-9837-a8382d1e8ace;
					- m_sourceType = 'F';
					- m_pTarget = GUID fcab19b3-848d-444f-80b5-333f2f521445;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 620 823 ;
					- m_TargetPort = 117 576 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 699 887 ;
						- m_nHorizontalSpacing = 17;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "User_Input";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -35 -7  45 -7  45 11  -35 11  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 717 856 ;
						- m_nHorizontalSpacing = -21;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 24af4bab-e93a-4ea3-bc76-e5f8539b4e05;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "Host_Interface_FRDM_KL25Z";
						- _id = GUID 5de46eb6-a581-42f2-b5d0-407401492f31;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fcab19b3-848d-444f-80b5-333f2f521445;
					- m_sourceType = 'F';
					- m_pTarget = GUID 90eb0133-fa98-4775-a41a-c064c93f88db;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1275 885  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1055 657 ;
					- m_TargetPort = 947 1130 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1226 732 ;
						- m_nHorizontalSpacing = -8;
						- m_nVerticalSpacing = -1;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Serial_UART";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -37 -7  60 -7  60 11  -37 11  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1321 731 ;
						- m_nHorizontalSpacing = -6;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIAnnotation 
					- _id = GUID 8e5aa85e-88a3-4271-894a-739895783d27;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "comment_65";
						- _id = GUID e01b1da6-bc44-4d1b-9587-1e332e5b4139;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.111624 0 0 0.0860806 1279 755.742 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 90ae2b08-c12b-44aa-b05a-ae0c6491997f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Final_Project.sbs";
						- _subsystem = "Final_Project";
						- _class = "";
						- _name = "comment_66";
						- _id = GUID c8232653-5a5c-48f3-b575-7993e2695822;
					}
					- m_pParent = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.23155 0 0 0.047619 899 974.857 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 3446a7de-a157-49db-b7f8-d2b2d78eaca0;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Final_Project.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Final_Project";
				- _id = GUID 20246198-4c47-4bfe-9397-a7aa14ffd20f;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 6;
		- value = 
		{ IComponent 
			- fileName = "FRDM_KL25Z";
			- _id = GUID 97403057-80a5-4323-8421-7b4a31e27ebf;
		}
		{ IComponent 
			- fileName = "Driver";
			- _id = GUID 213206af-015c-41b0-acff-d119203c9abf;
		}
		{ IComponent 
			- fileName = "Encoder";
			- _id = GUID ebbcc1e1-fba1-4c18-b67f-93b3441ed079;
		}
		{ IComponent 
			- fileName = "Motor";
			- _id = GUID 74ce5ee9-edd0-4a4d-a765-5319cad6aa8e;
		}
		{ IComponent 
			- fileName = "PowerSupply_12V";
			- _id = GUID 88a7a51b-355c-4870-906d-9393f79cf1fe;
		}
		{ IComponent 
			- fileName = "Host_Interface";
			- _id = GUID 0e52124a-e789-4058-8ffe-313e31fb1a1a;
		}
	}
}

